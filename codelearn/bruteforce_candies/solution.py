def divide(a):
    if sum(a) % 2 != 0: return "NO"
    for i in range(4):
        for j in range(4):
            t = sum(a[i:j])
            if sum(a) - t == t: return "YES"
            else:
                for k in range(4):
                    t += a[k]
                    if sum(a) - t == t: return "YES"
    return "NO"
