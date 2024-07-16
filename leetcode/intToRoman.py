
'''
12. Integer to Roman
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

'''
def intToRoman(num):
    if num < 1 or num > 3999: return "num is no adhereing to the constraints"

    numerals = {1:'I',5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:'IV', 40:'XL', 400:'CD', 9:'IX', 90:'XC', 900:'CM'}

    romanNumerals = ""
    pwr = 1
    while num > 0:
        digit = num % 10
        num = num // 10
        # print(digit, pwr)
        addingNumerals = ""
        numeralValue = digit * pwr
        if numeralValue in numerals:
            addingNumerals = numerals[numeralValue]
        else:
            if digit > 5:
                addingNumerals += numerals[pwr * 5]
                digit -= 5
            baseNumeral = numerals[pwr]
            addingNumerals += baseNumeral * digit
        print(f"digit = {digit}, pwr = {pwr}, adding={addingNumerals}")
        romanNumerals = addingNumerals + romanNumerals
        pwr = pwr * 10
    return romanNumerals
if __name__ == "__main__":
    # res = intToRoman(58)
    # print(res)
    res = intToRoman(3749)
    print(res)
    # res = intToRoman(1994)
    # print(res)