"""Public API: `sorting.sort` is the implementation we "ship"."""

from .slow import bubble_sort

sort = bubble_sort

__all__ = ["sort", "bubble_sort"]
