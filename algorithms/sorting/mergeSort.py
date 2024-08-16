

def merge(arr, l, m, r):
    left, right = arr[l : m + 1], arr[m + 1 : r + 1]
    i, j, k = l, 0, 0
    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            arr[i] = left[j]
            j += 1
        else:
            arr[i] = right[k]
            k += 1
        i += 1
    while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1
    while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1

def mergeSort(arr, l, r):
    if l == r:
        return arr
    m = l + (r - l ) // 2
    mergeSort(arr,l,m) # Left
    mergeSort(arr,m + 1,r) # Right
    merge(arr,l,m,r)
    return arr



if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    res = mergeSort(nums, 0, len(nums) - 1)
    print(res)