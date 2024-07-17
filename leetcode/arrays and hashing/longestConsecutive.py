'''
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


def longestConsecutive(nums):
    # brute force...
    # sort the array to ascending order
    # maintain global 'longest' variable and a numToSeq hashmap.
    # for each n in nums: check if n - 1 is in the hashmap. if so than map n to numToSeq[n - 1] + 1.

    nums.sort()
    numToSeq = {}
    longest = 0
    print(nums)
    for n in nums:
        if n - 1 in numToSeq:
            seqLength = numToSeq[n - 1] + 1
            longest = max(longest, seqLength)
            numToSeq[n] = seqLength
        else:
            numToSeq[n] = 1
            longest = max(longest, 1)
    return longest


def longestConsecutiveNOSORT(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in numSet:
            # n is start of sequence.
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length,longest)
    return longest




if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    res = longestConsecutive(nums)
    print(res)