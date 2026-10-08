"""
data_loader.py
Loads and cleans the AustLang dataset (AIATSIS) for the Language and Country
Explorer app.

Data source: AIATSIS AustLang database (https://aiatsis.gov.au/austlang)
Columns used: austlang_code, primary_name, lat, lon, state_territory, location_info
"""

import csv
import re
import os

REQUIRED_COLUMNS = ["austlang_code", "primary_name", "lat", "lon", "state_territory", "location_info"]

# The folder this script itself lives in, worked out automatically.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Default location of the data file: same folder as this script.
# Using a path built from __file__ (rather than just "austlang.csv") means
# this works no matter what folder the script is launched FROM - VS Code's
# Run button, a debugger, or pytest can all set a different "current
# directory", which is what caused the FileNotFoundError.
DEFAULT_DATA_PATH = os.path.join(_SCRIPT_DIR, "austlang.csv")

_TAG_RE = re.compile(r"<[^>]+>")  # matches HTML tags like <p> and <a href="...">


def strip_html(text):
    """Remove HTML tags from a text field, leaving plain readable text."""
    if not text:
        return ""
    cleaned = _TAG_RE.sub(" ", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def parse_float(value):
    """Convert a CSV string to a float, returning None for missing/invalid values."""
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def parse_regions(state_territory):
    """
    AustLang sometimes lists more than one region for a language, e.g. "NT,WA".
    Returns a list of region codes, e.g. ["NT", "WA"]. Returns ["Unknown"] if missing.
    """
    if not state_territory or not state_territory.strip():
        return ["Unknown"]
    return [r.strip() for r in state_territory.split(",") if r.strip()]


def load_austlang(filepath=None):
    """
    Load the AustLang CSV and return a list of cleaned language records (dicts).

    Each record:
        {
            "code": str,
            "name": str,
            "lat": float or None,
            "lon": float or None,
            "regions": list[str],
            "has_coordinates": bool,
            "description": str,   # HTML stripped
        }

    Rows missing both a code and a name are skipped, since they can't be
    identified or displayed. All other rows are kept, with missing fields
    represented as None/"Unknown" rather than dropped, so the dataset stays
    well above the 200-record minimum.

    If filepath is not given, defaults to austlang.csv in the same folder as
    this script (see DEFAULT_DATA_PATH above).
    """
    if filepath is None:
        filepath = DEFAULT_DATA_PATH

    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"AustLang data file not found: {filepath}\n"
            f"Make sure austlang.csv is saved in the same folder as data_loader.py: {_SCRIPT_DIR}"
        )

    records = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        missing_cols = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing_cols:
            raise ValueError(f"CSV is missing expected columns: {missing_cols}")

        for row in reader:
            code = (row.get("austlang_code") or "").strip()
            name = (row.get("primary_name") or "").strip()

            if not code or not name:
                continue

            lat = parse_float(row.get("lat"))
            lon = parse_float(row.get("lon"))

            record = {
                "code": code,
                "name": name,
                "lat": lat,
                "lon": lon,
                "regions": parse_regions(row.get("state_territory")),
                "has_coordinates": lat is not None and lon is not None,
                "description": strip_html(row.get("location_info")),
            }
            records.append(record)

    return records


def filter_by_region(records, region_code):
    """Return only records whose region list includes the given region code (e.g. 'WA')."""
    return [r for r in records if region_code in r["regions"]]


if __name__ == "__main__":
    data = load_austlang()  # uses DEFAULT_DATA_PATH automatically
    print(f"Loaded {len(data)} cleaned records")
    wa_only = filter_by_region(data, "WA")
    print(f"Records linked to WA: {len(wa_only)}")
