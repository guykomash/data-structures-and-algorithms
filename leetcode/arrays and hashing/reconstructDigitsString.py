'''

423. Reconstruct Original Digits from English
https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

Example 1:
Input: s = "owoztneoer"
Output: "012"

Example 2:
Input: s = "fviefuro"
Output: "45"

zero
one
two
three
four
five
six
seven
eight
nine
'''


from collections import Counter  


# this solution works, but there is a much better way...
def originalDigits(s):
    digits = ['zero','one','two','three','four','five', 'six', 'seven','eight','nine']
    digitMap = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5, 'six':6, 'seven':7,'eight':8,'nine':9}
    counterMap = {}
    
    # init counterMap : digit -> counter array (26)
    for digit in digits:
        count = [0] * 26
        for c in digit:
            index = ord(c) - ord('a')
            count[index] += 1
        counterMap[digit] = count

    counter = [0] * 26
    for c in s:
        index = ord(c) - ord('a')
        counter[index] += 1
    result = ""
    res = []
    def f(counter, i):
        nonlocal result
        # print(counter, i,res)
        zeros = 0
        for c in counter:
            if c == 0:
                zeros += 1

        if zeros == len(counter):
            # print("found", res)
            res.sort()
            for d in res:
                result += str(d)
            return True
        
        if i >= len(digits):
            return False

        digitCounter = counterMap[digits[i]]
        nextCounter = counter[::]
        isPossible = True
        for idx in range(len(nextCounter)):
            if nextCounter[idx] >= digitCounter[idx]:
                nextCounter[idx] -= digitCounter[idx]
            else:
                isPossible = False
        
        if isPossible:
            res.append(digitMap[digits[i]])
            if f(nextCounter, i):
                return True
            res.pop()
            if f(counter, i + 1):
                return True
        else:
            f(counter, i + 1)
    
    f(counter, 0)
    return result
    
def originalDigitsII(s):
    '''
    zero -> z
    two ->  w
    eight -> g
    four -> u
    six -> x
    three -> h - eight
    five  -> f - four
    seven -> s - x
    one -> o - zero - two - four
    nine -> i - ( five + eight + six)
    '''
    count = Counter(s)
    digits = [0] * 10
    digits[0] = count.get('z', 0)
    digits[2] = count.get('w', 0)
    digits[8] = count.get('g', 0)
    digits[4] = count.get('u', 0)
    digits[6] = count.get('x', 0)
    digits[3] = count.get('h', 0) - digits[8]
    digits[5] = count.get('f', 0) - digits[4]
    digits[7] = count.get('s', 0) - digits[6]
    digits[1] = count.get('0', 0) - digits[0] - digits[2] - digits[4]
    digits[9] = count.get('i', 0) - digits[5] - digits[8] - digits[6]

    result = ""
    for i in range(len(digits)):
        while digits[i] > 0:
            result += str(i)
            digits[i] -= 1
    return result
        



if __name__ == "__main__":
    res = originalDigitsII("fivefour")
    print(res)