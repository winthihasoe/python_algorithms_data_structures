def selection_sort(arr):
    print('------ selection sort ------')
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[num], arr[spot_marker] = arr[spot_marker], arr[num]
                print(arr)
        spot_marker += 1


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

selection_sort(l)
