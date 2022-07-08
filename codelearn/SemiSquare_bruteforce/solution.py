def isSemiSquareFree(n):
    if n == 1: return False
    c = 0
    while n % 2 == 0:
        n = n / 2
        c += 1
    if c % 2 == 0 and c != 0: return False
    c = 0
    for i in range(3,int(n**0.5)+1): 
        c = 0
        while n % i == 0:  
            n = n / i
            c += 1
        if c % 2 == 0 and c != 0: return False
    return True