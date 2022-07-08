def check(m,n):
    item=[True]*(n+1)
    key=[]
    for i in range(2,n+1):
        if item[i]:
            for j in range(2*i,n+1,i):item[j]=False
    for k in range(m,n+1):
        if item[k]:key.append(k)
    return key
def quarantinedPrimes(l,r):
    if l==1:l=2
    if r==1:r=2
    item=check(l-10,r+10)
    d=0
    if len(item)==0:return 0
    if len(item)==1:return 1
    if len(item)==2 and item[1]-item[0]>=10:return 1
    for i in range(1,len(item)-1):
        if item[i]-item[i-1]>=10 and item[i+1]-item[i]>=10:d+=1
    return d
