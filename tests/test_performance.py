"""Performance budget: sorting 20k items must finish in under 1 second."""

import random
import time

import pytest

from sorting import sort

N = 20_000
BUDGET_SECONDS = 1.0


@pytest.mark.perf
def test_sorts_20k_within_budget():
    data = [random.randint(0, 1_000_000) for _ in range(N)]
    start = time.perf_counter()
    sort(data)
    elapsed = time.perf_counter() - start
    assert elapsed < BUDGET_SECONDS, f"took {elapsed:.2f}s (budget {BUDGET_SECONDS}s)"
