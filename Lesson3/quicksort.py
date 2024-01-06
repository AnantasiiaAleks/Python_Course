def quick_sort(array):
    if len(array) <= 1:     # базис
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([500, 8, 3, 0, 2, 7, 10, 75]))