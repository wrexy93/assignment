"""
similarity.py
Core algorithm for the Language and Country Explorer app.

Implements edit distance (Levenshtein distance) from scratch, no library used,
and reuses it for two features:
  1. fuzzy_search()       - typo-tolerant search over language names/codes.
  2. find_similar_names() - ranks languages by how similar their name is to
                             a target language's name.

IMPORTANT NOTE ON DATA SCOPE:
The AustLang extract used in this project (austlang.csv) only contains
language NAMES, codes and locations - it does not contain individual
vocabulary words. This algorithm therefore compares language NAMES, not word
meanings. If a real wordlist (word, meaning, language) is sourced later from
a language centre, these same functions can be pointed at that word data
instead, with no change needed to the algorithm itself.
"""


def levenshtein_distance(a, b):
    """
    Compute the Levenshtein (edit) distance between two strings: the minimum
    number of single-character insertions, deletions, or substitutions needed
    to turn `a` into `b`. Case-insensitive. Written from scratch as the
    project's core algorithm (no library call does the whole task).
    """
    a, b = a.lower(), b.lower()
    n, m = len(a), len(b)

    if n == 0:
        return m
    if m == 0:
        return n

    previous_row = list(range(m + 1))

    for i in range(1, n + 1):
        current_row = [i] + [0] * m
        for j in range(1, m + 1):
            delete_cost = previous_row[j] + 1
            insert_cost = current_row[j - 1] + 1
            substitute_cost = previous_row[j - 1] + (0 if a[i - 1] == b[j - 1] else 1)
            current_row[j] = min(delete_cost, insert_cost, substitute_cost)
        previous_row = current_row

    return previous_row[m]


def similarity_score(a, b):
    """
    Convert edit distance into a 0-1 similarity score, where 1.0 means
    identical and 0.0 means completely different. Normalised by the length
    of the longer string so scores are comparable across name lengths.
    """
    if a == "" and b == "":
        return 1.0
    distance = levenshtein_distance(a, b)
    longest = max(len(a), len(b))
    return 1 - (distance / longest)


def find_similar_names(target_name, records, top_n=5, exclude_exact=True):
    """
    Given a target language name, rank all other languages in `records` by
    how similar their name is to the target. Returns the top_n most similar
    as (record, score) tuples, sorted highest score first.
    """
    scored = []
    for record in records:
        if exclude_exact and record["name"].lower() == target_name.lower():
            continue
        score = similarity_score(target_name, record["name"])
        scored.append((record, score))

    scored.sort(key=lambda pair: pair[1], reverse=True)
    return scored[:top_n]


def fuzzy_search(query, records, top_n=10, min_score=0.4):
    """
    Typo-tolerant search over language names and codes. Returns the top_n
    best matches with a similarity score at or above min_score, so a user
    typing "Nyoongar" can still find "Noongar".
    """
    if not query or not query.strip():
        return []

    query = query.strip()
    scored = []
    for record in records:
        name_score = similarity_score(query, record["name"])
        code_score = similarity_score(query, record["code"])
        best_score = max(name_score, code_score)

        # Boost direct substring matches, which covers partial/incomplete typing
        if query.lower() in record["name"].lower():
            best_score = max(best_score, 0.9)

        if best_score >= min_score:
            scored.append((record, best_score))

    scored.sort(key=lambda pair: pair[1], reverse=True)
    return scored[:top_n]
