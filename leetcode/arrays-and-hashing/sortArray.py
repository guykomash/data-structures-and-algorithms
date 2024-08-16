"""
912. Sort an Array
https://leetcode.com/problems/sort-an-array/description/

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""

    
def sortArray(nums):
    

    def merge(arr, l, m, r):
        left, right = arr[l:m+1], arr[m+1:r+1]
        lLen = len(left)
        rLen = len(right)

        i, j, k = l, 0, 0
        while j < lLen and k < rLen:
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        while j < lLen:
            arr[i] = left[j]
            j += 1
            i += 1
        while k < rLen:
            arr[i] = right[k]
            k += 1
            i += 1 

    def mergeSort(arr, l, r):
        if l == r:
            return arr

        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        return arr

    return mergeSort(nums, 0, len(nums) - 1)    


if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    res = sortArray(nums)
    print(res)