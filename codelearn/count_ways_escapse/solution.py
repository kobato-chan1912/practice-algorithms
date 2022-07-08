# Giống bài cầu thang học ở trong lớp
# Basic Quy hoạch động 

def count_ways_escapse(n):
    a,b=0,1
    while n+1>0:
        a,b=b,a+b
        n-=1
    return a