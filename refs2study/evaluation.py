from __future__ import annotations

from itertools import combinations
from typing import Iterable

IGNORED_STUDY_IDS = {"x"}


def clusters_to_duplicate_pairs(clusters: dict[str, list[str]]) -> set[frozenset[str]]:
    duplicate_pairs: set[frozenset[str]] = set()
    for ids in clusters.values():
        if len(ids) > 1:
            for pair in combinations(ids, 2):
                duplicate_pairs.add(frozenset(pair))
    return duplicate_pairs


def evaluate_duplicates(
    found_dupes: set[frozenset[str]], true_dupes: set[frozenset[str]]
) -> dict[str, float | int]:
    true_positives = found_dupes.intersection(true_dupes)
    false_positives = found_dupes.difference(true_dupes)

    precision = (
        0.0 if not found_dupes else len(true_positives) / float(len(found_dupes))
    )
    recall = 0.0 if not true_dupes else len(true_positives) / float(len(true_dupes))

    return {
        "found_duplicates": len(found_dupes),
        "true_positives": len(true_positives),
        "precision": precision,
        "recall": recall,
    }


def references_to_clusters(
    reference_rows: Iterable[object], study_id_attr: str = "study_id", reference_id_attr: str = "reference_id"
) -> dict[str, list[str]]:
    clusters: dict[str, list[str]] = {}
    for row in reference_rows:
        study_id = getattr(row, study_id_attr)
        if not study_id or study_id in IGNORED_STUDY_IDS:
            continue
        clusters.setdefault(str(study_id), []).append(str(getattr(row, reference_id_attr)))
    return clusters
