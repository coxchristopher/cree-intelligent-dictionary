import pytest

from search_quality.analyze_results import (
    count_and_annotate_dupes,
    DuplicateAnnotatedSearchResult,
)
from utils.types import FSTTag


def test_count_no_dupes_on_empty_list():
    assert count_and_annotate_dupes([]) == {"total": 0, "unique": 0}


ACÂKHOS_1: DuplicateAnnotatedSearchResult = {
    "matched_cree": "acâhkos",
    "lemma_wordform": {
        "text": "atâhk",
        "inflectional_category": "NA-3",
    },
    "raw_suffix_tags": tuple(map(FSTTag, ["N", "A", "Sg"])),
}
ACÂKHOS_2: DuplicateAnnotatedSearchResult = {
    "matched_cree": "acâhkos",
    "lemma_wordform": {
        "text": "acâhkos",
        "inflectional_category": "NA-1",
    },
    "raw_suffix_tags": tuple(map(FSTTag, ["N", "A", "Sg"])),
}
MISATIM_1: DuplicateAnnotatedSearchResult = {
    "matched_cree": "misatim",
    "lemma_wordform": {
        "text": "misatim",
        "inflectional_category": "NA-3",
    },
    "raw_suffix_tags": tuple(map(FSTTag, ["N", "A", "Sg"])),
}


def test_no_dupes_on_unique_list():
    assert count_and_annotate_dupes([ACÂKHOS_1]) == {"total": 0, "unique": 0}


def test_no_dupes_with_different_results():
    assert count_and_annotate_dupes([ACÂKHOS_1, ACÂKHOS_2]) == {"total": 0, "unique": 0}


def test_dupes_with_one_result_duplicated():
    assert count_and_annotate_dupes([ACÂKHOS_1, ACÂKHOS_1]) == {"total": 1, "unique": 1}


def test_count_dupes_with_multiple_duplicated_results():
    assert count_and_annotate_dupes(
        [ACÂKHOS_1, ACÂKHOS_1, MISATIM_1, MISATIM_1, MISATIM_1]
    ) == {"total": 3, "unique": 2}
