def merge_sorted(arr1, arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):

        if (arr1[i] < arr2[j]):
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


# xxxxxxxxxxxxxxxx Program Execution xxxxxxxxxxxxxxxx
l1 = [1, 4, 6, 8, 10, 11, 12, 14, 13]
l2 = [2, 3, 5, 7, 8, 9]
print(f"Un-merged list: {merge_sorted(l1,l2)}")
