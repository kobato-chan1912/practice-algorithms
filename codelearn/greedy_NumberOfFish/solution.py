def minimumNumberOfFish(w,k):
    count=0
    w.sort()
    if k < w[0]:
        count = -1
    elif k > w[-1]:
        count=0
    else:
        while k <= w[-1]:
            for i in range(len(w),0,-1):
                if k >= w[i-1]:
                    k += w[i-1]
                    count+=1
                    break
    return count