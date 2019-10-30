def binary_search(array, left, right, elem):
    if left > right:
        return -1

    middle = (right + left) // 2
    if elem == array[middle]:
        return middle
    elif elem < array[middle]:
        return binary_search(array, left, middle - 1, elem)
    else:
        return binary_search(array, middle + 1, right, elem)
