'''
139. Word Break
https://leetcode.com/problems/word-break/description/


Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''


def wordBreakDP(s, wordDict):
    dp = [False] *(len(s) + 1)
    dp[len(s)] = True
        # 01234567                  0    1      2    3     4     5      6    7     8
    #  s "leetcode" len=8, dp = [False,False,False,False,False,False,False,False,True]

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if i + len(word) < len(dp) and s[i: i + len(word)] == word:
                # found a word.
                dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
    
    return dp[0]
























def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[-1] = True

    for i in range(len(dp) - 1, -1, -1):
        for word in wordDict:
            if i + len(word) < len(dp) and s[i: i + len(word) ] == word:
                print(word)
                print(dp,i, i + len(word))
                dp[i] = dp[i + len(word)]
                print(dp)
                if dp[0] == True:
                    return True
    
    return dp


res = wordBreak("abcd", ["a","abc","b","cd"])
print(res)