def myAtoi(s):
    s=s.strip()
    if not s:
        return 0
    negative=False
    i=0
    if s[0]=='-':
        negative=True
        i+=1
    elif s[0]=='+':
        i+=1
    out=0
    while i<len(s) and s[i].isdigit():
        out=out*10+(ord(s[i])-ord("0"))
        if negative and out>(2**31):
            return -(2**31)
        if not negative and out>=((2**31)):
            return (2**31)-1
        i+=1
    return -out if negative else out
    


s="-42"
print(myAtoi(s))