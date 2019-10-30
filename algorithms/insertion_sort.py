def insertion_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1):
            if arr[j] > arr[i + 1]:
                elem = arr[i + 1]
                arr.remove(elem)
                arr.insert(j, elem)
    return arr
