'''que:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows
'''
'''approach
the most important thing is getting the pattern correct.
the pattern of "main" rows to "mid" rows is n, n-2, n, n-2, ...but this is not the right approach.
write out the row of each letter in the string. For numRows = 4, it became:

P  A  Y  P  A  L  I  S  H  I  R  I  N  G
-----------------------------------------
1  2  3  4  3  2  1  2  3  4  3  2  1  2
For numRows = 3, it became:

P  A  Y  P  A  L  I  S  H  I  R  I  N  G
-----------------------------------------
1  2  3  2  1  2  3  2  1  2  3  2  1  2
instead of worrying about "main" rows vs. "mid" rows, it easily maps into moving the index from 
1 -> numRows, and then from numRows -> 1. We don't even need to think about a matrix and worrying
about rows vs. columns.

algo:
how to make the different rows as strings? use array to store them
how would we make sure that we are going up and down in the correct pattern? 
The easiest way was to use a going_up flag to make sure to switch the direction of the index.


'''
def convert_string(s,numRows):
    if numRows==1:
            return s
    row_arr=[""]*numRows
    row_idx=1
    going_up_flag=True

    for ch in s:
        row_arr[row_idx-1]+=ch
        if row_idx==numRows:
            going_up=False
        elif row_idx==1:
            going_up=True
        
        if going_up:
            row_idx+=1
        else:
            row_idx-=1
        
    return "".join(row_arr)

s = "PAYPALISHIRING"
numRows = 4
result=convert_string(s,numRows)
print(result)

'''
Time: O(n)

We run through the whole string once: O(n)
everything we do inside the for loop: O(1)
Finally we join the whole array int a string: O(n)
Space: O(n)

We are creating a new array: O(n)
We are using join to put it back into a string: O(n)
'''