
def wordPattern(pattern, s):
        wordToKey = {}
        keyToWord = {}
        words = s.split()
        pi = 0
        for w in words:
            if pi >= len(pattern): return False
            if w in wordToKey:
                # seen word already.
                key = wordToKey.get(w)
                if key != pattern[pi]:
                    # print(1)
                    return False
                # matching pattern
            else:
                # first time seen word.
                key = pattern[pi]
                if key in keyToWord:
                    # seen key already - not matching this word
                    # print(2)
                    return False
                # first time seeing this key
                wordToKey[w] = key
                keyToWord[key] = w
            pi += 1
        return True if pi == len(pattern) else False


if __name__ == "__main__":
    res = wordPattern("abba","dog cat cat dog")
    print(res)
