import json
import tempfile
import threading
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

import langexp


class LanguageExplorerTests(unittest.TestCase):
	def load_csv_text(self, text):
		with tempfile.TemporaryDirectory() as directory:
			csv_path = Path(directory) / "dataset.csv"
			csv_path.write_text(text, encoding="utf-8")
			return langexp.load_records(csv_path)

	def test_bundled_dataset_has_records_and_required_columns(self):
		records = langexp.load_records()

		self.assertGreater(len(records), 0)
		self.assertTrue(langexp.REQUIRED_COLUMNS.issubset(records[0]))

	def test_valid_csv_is_loaded_and_values_are_trimmed(self):
		csv_text = (
			"austlang_code,primary_name,lat,lon,state_territory,status\n"
			"X1,  Example Language  ,,-, WA ,Confirmed\n"
		)

		records = self.load_csv_text(csv_text)

		self.assertEqual(records[0]["primary_name"], "Example Language")
		self.assertEqual(records[0]["state_territory"], "WA")

	def test_missing_required_column_is_rejected(self):
		with self.assertRaisesRegex(ValueError, "Dataset is missing columns"):
			self.load_csv_text("austlang_code,primary_name\nX1,Example\n")

	def test_empty_csv_without_header_is_rejected(self):
		with self.assertRaisesRegex(ValueError, "no header row"):
			self.load_csv_text("")

	def test_csv_with_header_but_no_records_is_rejected(self):
		header = ",".join(sorted(langexp.REQUIRED_COLUMNS)) + "\n"

		with self.assertRaisesRegex(ValueError, "contains no records"):
			self.load_csv_text(header)

	def test_state_counts_split_locations_and_deduplicate_names(self):
		records = [
			{"primary_name": "Language A", "state_territory": "WA, NSW"},
			{"primary_name": "language a", "state_territory": "WA"},
			{"primary_name": "Language B", "state_territory": "NSW"},
		]

		self.assertEqual(
			langexp.count_languages_by_state(records),
			{"NSW": 2, "WA": 1},
		)

	def test_state_counts_ignore_blank_values_and_handle_empty_input(self):
		records = [
			{"primary_name": "", "state_territory": "WA"},
			{"primary_name": "No state", "state_territory": ""},
		]

		self.assertEqual(langexp.count_languages_by_state(records), {})
		self.assertEqual(langexp.count_languages_by_state([]), {})

	def test_http_serves_page_records_summary_and_not_found(self):
		server = langexp.create_server()
		thread = threading.Thread(target=server.serve_forever)
		thread.start()
		base_url = "http://127.0.0.1:{}".format(server.server_port)
		try:
			with urlopen(base_url + "/") as response:
				page = response.read().decode("utf-8")
			with urlopen(base_url + "/api/records") as response:
				records = json.loads(response.read())
			with urlopen(base_url + "/api/languages-by-state") as response:
				counts = json.loads(response.read())
			with self.assertRaises(HTTPError) as error:
				urlopen(base_url + "/missing")
		finally:
			server.shutdown()
			thread.join()
			server.server_close()

		self.assertIn("Australian Aboriginal Language Explorer", page)
		self.assertIn("state-language-chart", page)
		self.assertGreater(len(records), 0)
		self.assertEqual(len(counts), 9)
		self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
	unittest.main()