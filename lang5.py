"""Stage 1: inspect the supplied dataset before developing the application.

The dataset has not been supplied yet, so this script does not assume its
columns or contain any cultural, language, or historical claims.
"""

import csv
from pathlib import Path


DATASET_PATH = Path("insert dataset.csv")


def inspect_dataset(file_path):
	"""Return basic CSV structure and quality information.

	CSV values are initially text. The simple type descriptions below only
	identify integer-like values; they do not infer what a column means.
	"""
	path = Path(file_path)
	if not path.is_file():
		raise FileNotFoundError(f"Dataset not found: {path}")

	with path.open("r", encoding="utf-8-sig", newline="") as csv_file:
		reader = csv.DictReader(csv_file)
		columns = reader.fieldnames
		if not columns:
			raise ValueError("The CSV is empty or has no column headings.")
		rows = list(reader)

	missing = {}
	data_types = {}
	for column in columns:
		values = [row.get(column, "").strip() for row in rows]
		missing[column] = sum(value == "" for value in values)
		present_values = [value for value in values if value]
		if present_values and all(value.lstrip("+-").isdigit() for value in present_values):
			data_types[column] = "integer-like text"
		else:
			data_types[column] = "text"

	unique_rows = {tuple(row.get(column, "") for column in columns) for row in rows}
	return {
		"record_count": len(rows),
		"columns": columns,
		"data_types": data_types,
		"missing_values": missing,
		"duplicate_records": len(rows) - len(unique_rows),
	}


def main():
	"""Inspect the configured CSV and report what remains unverified."""
	try:
		report = inspect_dataset(DATASET_PATH)
	except (FileNotFoundError, ValueError) as error:
		print(f"Cannot inspect dataset: {error}")
		print("Stage 1 is pending until the actual dataset is provided.")
		return

	for label, value in report.items():
		print(f"{label.replace('_', ' ').title()}: {value}")
	print(
		"Useful filters and analyses require reviewing the actual columns. "
		"The original source and licensing conditions must be confirmed with "
		"the dataset provider; they cannot be established from CSV structure."
	)


if __name__ == "__main__":
	main()
