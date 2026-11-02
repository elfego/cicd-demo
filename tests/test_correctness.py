"""Correctness tests for the shipped `sorting.sort`."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from sorting import sort


# --- Example-based tests: hand-picked cases ---------------------------------
@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([-1, 0, -3], [-3, -1, 0]),
    ],
)
def test_examples(data, expected):
    assert sort(data) == expected


def test_does_not_mutate_input():
    data = [3, 1, 2]
    sort(data)
    assert data == [3, 1, 2]


# --- Property-based tests: Hypothesis generates hundreds of random inputs ---
@given(st.lists(st.integers()))
def test_matches_builtin_sorted(data):
    assert sort(data) == sorted(data)


@given(st.lists(st.integers()))
def test_preserves_length(data):
    assert len(sort(data)) == len(data)
