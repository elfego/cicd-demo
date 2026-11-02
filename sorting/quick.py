"""Version 2: quicksort, O(n log n) on average."""


def quick_sort(items):
    a = list(items)
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    less = [x for x in a if x < pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
