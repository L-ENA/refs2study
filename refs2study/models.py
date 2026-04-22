from typing import Literal

from pydantic import BaseModel, Field

ReferenceType = Literal[
    "Journal article",
    "Other Reference",
    "Conference Proceedings",
    "Book",
    "Book Section",
    "Correspondence",
    "Unpublished Reference",
]


class StudyReference(BaseModel):
    reference_id: str = Field(default="")
    study_id: str = Field(default="")
    type: ReferenceType
    volume: str = Field(default="")
    source: str = Field(default="")
    city: str = Field(default="")
    conferenceName: str = Field(default="")
    edition: str = Field(default="")
    editor: str = Field(default="")
    publisher: str = Field(default="")
    bookName: str = Field(default="")
    date: str = Field(default="")
    allAuthors: str = Field(default="")
    issue: str = Field(default="")
    journalName: str = Field(default="")
    originalTitle: str = Field(default="")
    pages: str = Field(default="")
