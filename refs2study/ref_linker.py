from __future__ import annotations

from .evaluation import clusters_to_duplicate_pairs, evaluate_duplicates, references_to_clusters
from .models import StudyReference


class RefLinker:
    def predict(self, references: list[StudyReference]) -> dict[str, list[str]]:
        clusters: dict[str, list[str]] = {}
        for reference in references:
            key_parts = [
                reference.originalTitle.strip().lower(),
                reference.journalName.strip().lower(),
                reference.date.strip().lower(),
            ]
            cluster_key = "|".join(key_parts).strip("|") or reference.reference_id
            clusters.setdefault(cluster_key, []).append(reference.reference_id)
        return clusters

    def evaluate(
        self, predicted_clusters: dict[str, list[str]], gold_references: list[StudyReference]
    ) -> dict[str, float | int]:
        found_dupes = clusters_to_duplicate_pairs(predicted_clusters)
        gold_clusters = references_to_clusters(gold_references)
        true_dupes = clusters_to_duplicate_pairs(gold_clusters)
        return evaluate_duplicates(found_dupes, true_dupes)
