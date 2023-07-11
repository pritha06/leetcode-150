'''
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''

def romanToInt(s):
    result=0
    prev=0
    hashmap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    for i in s[::-1]: # rev the s
        if hashmap[i]>=prev:
            result+=hashmap[i] # sum the value iff previous value same or more
        else:
            result-=hashmap[i] ## substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
        prev=hashmap[i]
    return result
'''
        we can do something like this as well
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
'''
# s = "III"
# s = "LVIII"
s = "MCMXCIV"
# s="CDL"
result=romanToInt(s)
print(result)