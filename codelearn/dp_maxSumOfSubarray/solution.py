def maxSumOfBeautifulSubarray(arr):
    n = len(arr)
    arr.extend(arr)
    lst1 = []
    s = 0
    for i in range(n):
        for j in range(i,i+n):
            s += arr[j] 
            if s % 9 == 0 :
                lst1.append(s)
        s = 0      
    tam = -10**9 
    if lst1 != [] :      
        for i in lst1 :
            if i > tam :
                tam = i
        return tam
    else:
        return -1
