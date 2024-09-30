def quick_sort(array):
    if len(array) <= 1:     #Базис рекурсии
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([25, 425, 4, 856, 5, 7, 12, 85, 12, 9, 45, 3, 1, 10]))