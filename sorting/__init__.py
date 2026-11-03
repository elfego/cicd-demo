"""Public API: `sorting.sort` is the implementation we "ship"."""

from .quick import quick_sort
from .slow import bubble_sort

sort = quick_sort

__all__ = ["sort", "bubble_sort", "quick_sort"]
