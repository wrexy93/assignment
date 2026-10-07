"""
analysis.py
Summary statistics from the cleaned AustLang records, for the Region Stats screen.

NOTE: The AustLang extract used in this project does not include a language
"status" field (e.g. active/sleeping/revival) - that column doesn't exist in
austlang.csv, so that stat from the original plan isn't available from this
file alone. Two real, data-backed stats are provided instead: language count
per region, and location-data completeness (how many languages have known
coordinates) - which is itself a genuine finding worth reporting, since it
shows real gaps in the public location data.
"""

from collections import Counter


def count_languages_per_region(records):
    """
    Count how many languages are linked to each region. A language listed
    under more than one region (e.g. "NT,WA") is counted once for each
    region it touches. Returns a dict {region_code: count}, sorted by count
    descending.
    """
    counter = Counter()
    for record in records:
        for region in record["regions"]:
            counter[region] += 1
    return dict(counter.most_common())


def coordinate_completeness(records):
    """
    Returns how many records have known coordinates vs missing coordinates,
    plus the percentage complete. Useful as a data-quality insight for the report.
    """
    total = len(records)
    with_coords = sum(1 for r in records if r["has_coordinates"])
    without_coords = total - with_coords
    percent_complete = round((with_coords / total) * 100, 1) if total else 0.0

    return {
        "total": total,
        "with_coordinates": with_coords,
        "without_coordinates": without_coords,
        "percent_complete": percent_complete,
    }


def top_regions(records, n=10):
    """Return the n regions with the most languages, as (region, count) tuples."""
    counts = count_languages_per_region(records)
    return list(counts.items())[:n]
