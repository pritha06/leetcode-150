def hIndex(citations):
    N=len(citations) #calculate total length
    tmp=[0]*(N+1) #use tmp variable to store values
    for idx,val in enumerate(citations): #run a loop if value > total length, increase end index by 1
        if val>N:
            tmp[N]+=1
        else: #else increment index for 1 
            tmp[val]+=1
    total=0 #run a backward loop to keep track of total whenever it equals to index return the index
    for i in range(N,-1,-1):
        total+=tmp[i]
        if total>=i:
            return i


'''O(n) TC and SC approach'''
citations = [3,0,6,1,5]
result=hIndex(citations)
print(result)