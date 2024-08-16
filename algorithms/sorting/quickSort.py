def exchange(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

def partition(arr, p , r):
    i = p - 1 # starting index of elements less than pivot
    for j in range(p, r):
        if arr[j] <= arr[r]:
            i += 1
            exchange(arr, i, j)
    exchange(arr, i + 1, r)
    return i + 1       


def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        # q = index of the pivot.
        quickSort(arr,p, q - 1)
        quickSort(arr, q + 1, r)
    return arr

if __name__ == "__main__":
    arr = [5,3,66,7,8,2,4]
    res = quickSort(arr, 0, len(arr) - 1)
    print(res) 