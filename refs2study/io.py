from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import rispy

from .models import StudyReference

_REQUIRED_CSV_COLUMNS = {
    "study_id",
    "reference_id",
    "type",
    "volume",
    "source",
    "city",
    "conferenceName",
    "edition",
    "editor",
    "publisher",
    "bookName",
    "date",
    "allAuthors",
    "issue",
    "journalName",
    "originalTitle",
    "pages",
}


def _to_string(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value)


def load_gold_standard_csv(path: str | Path) -> list[StudyReference]:
    frame = pd.read_csv(path)
    missing = sorted(_REQUIRED_CSV_COLUMNS.difference(frame.columns))
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    references: list[StudyReference] = []
    for row in frame.to_dict(orient="records"):
        references.append(
            StudyReference(
                reference_id=_to_string(row.get("reference_id", "")),
                study_id=_to_string(row.get("study_id", "")),
                type=_to_string(row.get("type", "")),
                volume=_to_string(row.get("volume", "")),
                source=_to_string(row.get("source", "")),
                city=_to_string(row.get("city", "")),
                conferenceName=_to_string(row.get("conferenceName", "")),
                edition=_to_string(row.get("edition", "")),
                editor=_to_string(row.get("editor", "")),
                publisher=_to_string(row.get("publisher", "")),
                bookName=_to_string(row.get("bookName", "")),
                date=_to_string(row.get("date", "")),
                allAuthors=_to_string(row.get("allAuthors", "")),
                issue=_to_string(row.get("issue", "")),
                journalName=_to_string(row.get("journalName", "")),
                originalTitle=_to_string(row.get("originalTitle", "")),
                pages=_to_string(row.get("pages", "")),
            )
        )
    return references


def load_ris_file(path: str | Path) -> list[StudyReference]:
    with open(path, encoding="utf-8") as ris_file:
        parsed = rispy.load(ris_file)

    references: list[StudyReference] = []
    for index, item in enumerate(parsed, start=1):
        references.append(
            StudyReference(
                reference_id=str(item.get("id") or f"ris-{index}"),
                study_id="",
                type="Other Reference",
                volume=str(item.get("volume", "") or ""),
                source=str(item.get("primary_title", "") or ""),
                city=str(item.get("place_published", "") or ""),
                conferenceName=str(item.get("conference_name", "") or ""),
                edition=str(item.get("edition", "") or ""),
                editor=", ".join(item.get("editors", []) or []),
                publisher=str(item.get("publisher", "") or ""),
                bookName=str(item.get("secondary_title", "") or ""),
                date=str(item.get("year", "") or ""),
                allAuthors=", ".join(item.get("authors", []) or []),
                issue=str(item.get("number", "") or ""),
                journalName=str(item.get("journal_name", "") or ""),
                originalTitle=str(item.get("title", "") or ""),
                pages=str(item.get("start_page", "") or ""),
            )
        )
    return references
