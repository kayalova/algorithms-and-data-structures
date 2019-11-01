def quick_sort(arr: list):
    if len(arr) < 2:
        return arr

    chosen = arr[0]
    right, left = [], []
    for j in range(1, len(arr)):
        if arr[j] < chosen:
            left.append(arr[j])
        else:
            right.append(arr[j])
    return [*quick_sort(left), chosen, *quick_sort(right)]
