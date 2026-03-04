"""
Sorting algorithms — bubble sort, merge sort, and quick sort.
Each function returns a new sorted list and leaves the input unchanged.
"""


def bubble_sort(arr: list) -> list:
    """O(n²) comparison sort. Stable and in-place (operates on a copy here)."""
    a = list(arr)
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def merge_sort(arr: list) -> list:
    """O(n log n) divide-and-conquer sort. Stable but requires O(n) extra space."""
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: list) -> list:
    """O(n log n) average-case sort. In-place variant using last element as pivot."""
    a = list(arr)
    _quick_sort(a, 0, len(a) - 1)
    return a


def _quick_sort(a: list, low: int, high: int) -> None:
    if low < high:
        pivot_idx = _partition(a, low, high)
        _quick_sort(a, low, pivot_idx - 1)
        _quick_sort(a, pivot_idx + 1, high)


def _partition(a: list, low: int, high: int) -> int:
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print("Input:      ", sample)
    print("Bubble sort:", bubble_sort(sample))
    print("Merge sort: ", merge_sort(sample))
    print("Quick sort: ", quick_sort(sample))
