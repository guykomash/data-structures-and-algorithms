'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


'''

from collections import Counter 
import heapq
def topKFrequent(nums, k):
    # brute force : iterate over array, counting frequencies.
    # map frequency to array of numbers with this frequency.
    # init max heap of the frequencies.
    # while k > 0, pop from the heap the frequency array, if its empty pop again, else, remove one element and return it, decrease k

    numToFreq = Counter(nums)
    freqToNum = {}
    for n,f in numToFreq.items():
        if f in freqToNum:
            freqToNum[f].append(n)
        else:
            freqToNum[f] = [n]
    
    freqsVals = [- k for k in freqToNum.keys()]
    heapq.heapify(freqsVals)

    res = []
    while k > 0:
        curFreq = - heapq.heappop(freqsVals)
        numbers = freqToNum[curFreq]
        while numbers and k > 0:
            res.append(numbers.pop())
            k -= 1

    return res
    

def topKFrequentNOHEAP(nums, k):
    numToFreq = Counter(nums)

    freqs = [[] for i in range(len(nums) + 1)] # 0 ..... len(nums) = possible frequencies of number in nums.
    for n, f in numToFreq.items():
        freqs[f].append(n)
    
    
    res = []
    i = len(freqs) - 1
    
    while i >= 0:
        if not freqs[i]:
            i -= 1
            continue
        while k > 0 and freqs[i]:
            res.append(freqs[i].pop())
            k -= 1
        i -= 1
        if k == 0:
            break
    return res


'''
    NO Heap by neetcode
        countMap = {}
        for n in nums:
            countMap[n] = 1 + countMap.get(n,0)
        
        freq = [[] for i in range(len(nums) + 1)]
        
        for n,c in countMap.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,-1,-1):
            if not freq[i]: continue
            while k > 0 and freq[i]:
                res.append(freq[i].pop(0))
                k -= 1
            if k == 0: return res


'''

if __name__ == "__main__":
    nums = nums = [1,1,1,2,2,3]
    k = 3
    res = topKFrequentNOHEAP(nums, k)
    print(res)