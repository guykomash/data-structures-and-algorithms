'''
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.

'''
from collections import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children.get(c)
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:
        
        q = deque()
        q.append(self.root)
        for i in range(len(word)):
            c = word[i]
            qLen = len(q)
            while qLen > 0:
                node = q.popleft()
                if c == '.':
                    for child in node.children.values():
                        q.append(child)
                        if i == len(word) - 1:
                            if child.eow == True:
                                return True
                    # check if node is 
                elif c in node.children:
                    child = node.children[c]
                    q.append(child)
                    if i == len(word) - 1:
                        if child.eow == True:
                            return True
                qLen -= 1
        return False
            





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == "__main__":
    wd  =  WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad")) # return False
    print(wd.search("bad")) # return True
    print(wd.search(".ad")) # return True
    print(wd.search("b..")) # return True
