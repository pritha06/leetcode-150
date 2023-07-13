'''//Approach 1 : 
//time complexity - O(1) since the algorithm always iterates through a constant number of values (13 in this case).
//O(1) since the amount of extra space used is constant (the size of the storeIntRoman vector, which is also 13 in this case

The approach used here is to store the Roman numeral values and their corresponding symbols in a vector of pairs. The algorithm then iterates through the vector and repeatedly adds the corresponding symbols to the result string while subtracting the corresponding value from the input integer until the input integer becomes zero.
Initialize an empty string called Roman to store the resulting Roman numeral.
Create a vector of pairs called storeIntRoman, to store the Roman numeral values and their corresponding symbols.
Iterate through the storeIntRoman vector using a for loop.
For each pair, check if the input integer is greater than or equal to the Roman numeral value.
If it is, add the corresponding symbol to the Roman string and subtract the corresponding value from the input integer.
Repeat steps 4-5 until the input integer becomes zero.
Return the Roman string.
'''
'''
code
'''


def intToRoman(num):
    strList=[[1000,"M"],[900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
    res=""
    for i in range(len(strList)):
        while num>=strList[i][0]:
            res+=strList[i][1]
            num-=strList[i][0]
    return res


'''consider all the cases where numbers can be different so include them in list as well
make nested lists from smallest to largest in a sequential order,
not using hashmap because we will run the loop on the list in reversed order
so first we will check by dividing the number with 1000 if found we will append the count with symbol 
in the result.
take mod of num to follow the same steps for numbers remaining.
code-
strList=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
    res=""
    for sym,val in strList[::-1]:
        if num//val:
            count=num//val
            r=sym*count
            res+=r
            num=num%val
    return res
'''            
    
    

num=33
result=intToRoman(num)
print(result)