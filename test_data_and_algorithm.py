"""
test_data_and_algorithm.py
Automated tests for the data loading/cleaning and similarity algorithm.
Run with: pytest test_data_and_algorithm.py -v
"""

from similarity import levenshtein_distance, similarity_score, fuzzy_search
from data_loader import load_austlang, parse_regions, parse_float, filter_by_region, strip_html


# ---------- Algorithm tests ----------

def test_levenshtein_identical_strings_is_zero():
    assert levenshtein_distance("Noongar", "Noongar") == 0


def test_levenshtein_completely_different_strings():
    assert levenshtein_distance("cat", "dog") == 3


def test_levenshtein_empty_string_edge_cases():
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance("", "abc") == 3
    assert levenshtein_distance("abc", "") == 3


def test_similarity_score_is_normalised_between_0_and_1():
    score = similarity_score("Noongar", "Nyoongar")
    assert 0.0 <= score <= 1.0
    assert similarity_score("same", "same") == 1.0


def test_fuzzy_search_handles_typo():
    records = [
        {"code": "W1", "name": "Noongar", "lat": None, "lon": None,
         "regions": ["WA"], "has_coordinates": False, "description": ""},
        {"code": "W2", "name": "Wajarri", "lat": None, "lon": None,
         "regions": ["WA"], "has_coordinates": False, "description": ""},
    ]
    results = fuzzy_search("Nyoongar", records, min_score=0.5)
    assert len(results) >= 1
    assert results[0][0]["name"] == "Noongar"


def test_fuzzy_search_empty_query_returns_empty_list():
    records = [{"code": "W1", "name": "Noongar", "lat": None, "lon": None,
                "regions": ["WA"], "has_coordinates": False, "description": ""}]
    assert fuzzy_search("", records) == []


# ---------- Data cleaning tests ----------

def test_parse_regions_handles_multiple_and_missing():
    assert parse_regions("NT,WA") == ["NT", "WA"]
    assert parse_regions("") == ["Unknown"]
    assert parse_regions(None) == ["Unknown"]


def test_parse_float_handles_missing_and_invalid_values():
    assert parse_float("") is None
    assert parse_float(None) is None
    assert parse_float("not-a-number") is None
    assert parse_float("-16.69") == -16.69


def test_strip_html_removes_tags():
    raw = '<p>Hello <a href="x">world</a></p>'
    assert strip_html(raw) == "Hello world"


def test_load_austlang_cleans_real_file():
    records = load_austlang()  # uses the built-in default path - no hardcoded string
    assert len(records) > 200  # confirms the dataset clears the 200-record minimum
    for key in ("code", "name", "lat", "lon", "regions", "has_coordinates", "description"):
        assert key in records[0]


def test_filter_by_region_returns_only_matching_region():
    records = load_austlang()
    wa_records = filter_by_region(records, "WA")
    assert all("WA" in r["regions"] for r in wa_records)
    assert len(wa_records) > 0
