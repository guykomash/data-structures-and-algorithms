'''
49. Group Anagram
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''

def groupAnagrams(strs):
    # convert each string to a int arry of length 26. each element of the array is a counter represting count of letters a -> z in the string.
    # each int array will used as a key mapping anagrams to it.

    def getAnagramKey(s):
        counters = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            counters[index] += 1

        # returning counters as a hashable key.
        return tuple(counters)
    
    anagrams = {} # key = int array val = string array of anagram (["nat", "tan"]) .. 
    for s in strs:
        key = getAnagramKey(s)
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    
    # the anagram values are the desired grouping of strings to be returned.
    return list(anagrams.values())



if __name__ == "__main__":
    strs = strs = ["eat","tea","tan","ate","nat","bat"]
    res = groupAnagrams(strs)
    print(res)