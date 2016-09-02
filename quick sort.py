arr = [int(y) for y in input().split(',')]


def partition(arr, start, end):
    index = start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] < pivot:
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
            index += 1
    temp = arr[index]
    arr[index] = arr[end]
    arr[end] = temp
    return index


def quick_sort(arr, start, end):
    if start < end:
        index = partition(arr, start, end)
        quick_sort(arr, start, index-1)
        quick_sort(arr, index+1, end)

quick_sort(arr,0, len(arr)-1)
print(arr)