"""Version 1: correct, but slow. Bubble sort is O(n^2)."""


def bubble_sort(items):
    a = list(items)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
