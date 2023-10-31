print('Algorithm file loaded')


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)


def merge_sort(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sort(l1, l2)


def bubblesort(arr):
    swap_happen = True
    while swap_happen:
        swap_happen = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happen = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
