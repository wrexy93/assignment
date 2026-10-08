"""Stage 1: inspect a supplied CSV before designing the application.

Run: python lang4.py path/to/dataset.csv
This reports dataset structure only; it does not infer cultural information,
data provenance, or permission to reuse the data.
"""

import csv
import sys
from collections import Counter
from pathlib import Path


def inspect_dataset(file_path):
	"""Return record/column counts, missing values, duplicates and candidates.

	Candidate filter columns are suggested from actual header names and must
	be checked against the dataset documentation before being used.
	"""
	path = Path(file_path)
	if not path.is_file():
		raise ValueError("Dataset file does not exist or is not a regular file.")

	try:
		with path.open("r", encoding="utf-8-sig", newline="") as source:
			reader = csv.DictReader(source)
			if not reader.fieldnames:
				raise ValueError("CSV is empty or has no header row.")
			original_headers = reader.fieldnames
			headers = [header.strip() for header in original_headers]
			if any(not header for header in headers) or len(set(headers)) != len(headers):
				raise ValueError("CSV headers must be non-empty and unique after trimming.")
			records = [
				{header: (row.get(original) or "").strip()
				 for original, header in zip(original_headers, headers)}
				for row in reader
			]
	except (OSError, UnicodeError, csv.Error) as error:
		raise ValueError("Could not read CSV: " + str(error)) from error

	if not records:
		raise ValueError("CSV contains a header but no data records.")

	missing = {header: sum(not row[header] for row in records) for header in headers}
	unique_rows = {tuple(row[header] for header in headers) for row in records}
	data_types = {}
	for header in headers:
		values = [row[header] for row in records if row[header]]
		data_types[header] = (
			"integer-like text" if values and all(value.isdigit() for value in values)
			else "text"
		)

	candidates = [
		header for header in headers
		if any(term in header.casefold()
			   for term in ("region", "language", "status", "name", "area"))
	]
	case_inconsistencies = {}
	for header in headers:
		values = [row[header] for row in records if row[header]]
		counts = Counter(values)
		variants = sorted(value for value in counts if value.casefold() in {
			other.casefold() for other in counts if other != value
		})
		if variants:
			case_inconsistencies[header] = variants

	return {
		"record_count": len(records),
		"columns": headers,
		"data_types": data_types,
		"missing_values": missing,
		"duplicate_records": len(records) - len(unique_rows),
		"filter_candidates": candidates,
		"possible_case_inconsistencies": case_inconsistencies,
	}


def main():
	if len(sys.argv) != 2:
		print("Dataset not supplied. Usage: python lang4.py path/to/dataset.csv")
		print("Provide the actual dataset before application-specific planning.")
		return
	try:
		report = inspect_dataset(sys.argv[1])
	except ValueError as error:
		print("Dataset inspection failed:", error)
		return

	print("DATASET INSPECTION — Stage 1")
	for key, value in report.items():
		print(key.replace("_", " ").title() + ":", value)
	print("Original source: not established by inspecting CSV contents; check provider documentation.")
	print("Licence/access conditions: not established; verify before reuse or deployment.")


if __name__ == "__main__":
	main()
