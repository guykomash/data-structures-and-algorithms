'''
1239. Maximum Length of a Concatenated String with  Unique Characters.
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.



'''
import unittest
class Test(unittest.TestCase):
    def test1(self):
        arr = ["un","iq","ue"]
        res = 4
        self.assertEqual(maxLength(arr), res)
    
    def test2(self):
        arr = ["cha","r","act","ers"]
        res = 6
        self.assertEqual(maxLength(arr), res)
    
    def test3(self):
        arr = arr = ["abcdefghijklmnopqrstuvwxyz"]
        res = 26
        self.assertEqual(maxLength(arr), res)
    def test4(self):
        arr = ["aa","bb"]
        res = 0
        self.assertEqual(maxLength(arr), res)
    def test5(self):
        arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
        res = len(arr)
        self.assertEqual(maxLength(arr), res)

def maxLengthBruteForce(arr):
    longest = 0
    def fn(i, concat, depth):
        # if depth >= 100:
            # return
        nonlocal longest
        if i >= len(arr):
            longest = max(longest, len(concat))
            return
        
        # check if not dups inc concat:
        hasDups = False
        cSet = set()
        for c in concat:
            cSet.add(c)
        for c in arr[i]:
            if c in cSet:
                hasDups = True
                return
            else:
                cSet.add(c)
        if not hasDups:
            fn(i + 1, concat + arr[i], depth + 1)
            fn(i + 1, concat, depth + 1)
    
    fn(0, "", 0)
    return longest

def maxLength(arr):
    cSet = set()
    longest = 0
    def overlap(cSet, s):
        prev = set()
        for c in s:
            if c in cSet or c in prev:
                return False
            else: prev.add(c)
        return prev
    def fn(i):
        nonlocal longest
        if i == len(arr):
            longest = max(longest, len(cSet))
            return
        
        if (toJoin:= overlap(cSet, arr[i])):
            cSet.update(toJoin)
            fn(i + 1)
            for c in arr[i]:
                cSet.discard(c)
        # skip arr[i]
        fn(i + 1)
    fn(0)
    return longest    


# def maxLength(arr):
#     if not arr: return 0
#     if len(arr) == 1:
#         return len(arr[0])
    
#     # remove strings with duplicate chars from arr:
#     i = 0
#     while i < len(arr):
#         s  = arr[i]
#         cSet = set()
#         for c in s:
#             removed = False
#             if c in cSet:
#                 # remove s from arr
#                 arr = arr[:i] + arr[i + 1:]
#                 break
#             else:
#                 cSet.add(c)
#         if not removed:
#             i += 1

#     charGroups = []
#     for c in range(26):
#         char = chr(ord('a') + c)
#         cGroup = []
#         for s in arr:
#             if char in s:
#                 cGroup.append(s)
#         charGroups.append(cGroup)
    
#     word2Uniqs = {}
#     for i in range(len(arr)):
#         word2Uniqs[arr[i]] = arr[:i] + arr[i + 1:]

#     for cGroup in charGroups:
#         for word in cGroup:
#             for w in cGroup:
#                 if w in word2Uniqs[word]:
#                     word2Uniqs[word].remove(w)
#     print(word2Uniqs)
#     longest = 0
#     for k,vals in word2Uniqs.items():
#         for v in vals:
#             longest = max(longest, len(k) + len(v))

#     return longest

# def maxLength(arr):
    
#     # remove strings with duplicate chars from arr:
#     i = 0
#     while i < len(arr):
#         s  = arr[i]
#         cSet = set()
#         for c in s:
#             removed = False
#             if c in cSet:
#                 # remove s from arr
#                 arr = arr[:i] + arr[i + 1:]
#                 break
#             else:
#                 cSet.add(c)
#         if not removed:
#             i += 1

#     # arr has not strings with dups.
#     longest = 0
#     for i in range(len(arr)):
#         cSet = set()
#         hasDups = False
#         for c in arr[i]:
#             if c in cSet:
#                 hasDups = True
#                 break
#             else:
#                 cSet.add(c)
#         if hasDups:
#             continue
        
#         # no dups string, all char in cSet.
#         concatLen = len(arr[i])
#         for j in range(1, len(arr)):
#             # save prev length for restore
#             curLen = concatLen
#             curSet = set()
#             restore = False
#             for c in arr[j]:
#                 if c not in cSet and c not in curSet:
#                     curSet.add(c)
#                     curLen += 1
#                 else:
#                     restore = True
#                     break
#             if not restore:
#                 concatLen += curLen
#                 cSet.update(curSet)
#         longest = max(longest, concatLen)
        # 
    # return longest












if __name__ == "__main__":
    unittest.main()