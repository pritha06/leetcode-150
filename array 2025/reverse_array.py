#input Geeks
#output skeeG
#use slicing [start index:end index:steps]
#python has reverse func which only works on list
#join func runs like "*".join(l) so each element in list l will get into string mixed with *
#list(l)-> ['g','e','e','k']
#l.reverse()->['k','e','e','g']
#if you join by * then k*e*e*g would be output

def reverse_words(s):
    # return s[::-1] #skeeG
    s=list(s)
    print(s) #['G', 'e', 'e', 'k', 's']
    s.reverse()
    print(s) #['s', 'k', 'e', 'e', 'G']
    k="".join(s)
    print(type(k)) #<class 'str'>
    return k

s="Geeks"
print(reverse_words(s))