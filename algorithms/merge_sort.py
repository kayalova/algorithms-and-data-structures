def merge(ar1, ar2):
    i = j = 0
    merged = []
    while i < len(ar1) and j < len(ar2):
        if ar1[i] < ar2[j]:
            merged.append(ar1[i])
            i += 1
        else:
            merged.append(ar2[j])
            j += 1

        if i == len(ar1):
            merged += ar2[j:]

        elif j == len(ar2):
            merged += ar1[i:]
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    return _merge_sort(arr)


def _merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(_merge_sort(left), _merge_sort(right))
    else:
        return arr
