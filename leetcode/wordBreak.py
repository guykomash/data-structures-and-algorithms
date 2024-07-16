'''
139. Word Break
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
def wordBreak(s, wordDict):
    
    def f(s):
        if not s:
            return True
        for word in wordDict:
            i = 0 
            while i < len(s) and i < len(word) and s[i] == word[i]:
                i += 1
            
            if i == len(word):
               res = f(s[i:])
               if res: return True
        
        return False
    return f(s)

def wordBreakDP(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(dp)):
        for word in wordDict:
            print(i, word)
            if i - len(word) >= 0 and s[i - len(word): i] == word:
                dp[i] = dp[i - len(word)]
    print(dp)
    return dp[-1]




if __name__ == "__main__":
    res = wordBreakDP("leetcode", ["leet","code"])
    print(res)