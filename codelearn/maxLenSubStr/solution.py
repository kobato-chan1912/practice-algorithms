def maxLenSubStr(string):
    dct = {}
    m = 0
    for i in range(len(string)):
        char = string[i]
        if char in dct.keys():
            a = i - dct[char]
            if a > m:
                m = a
        else:    
            dct.setdefault(char, i)
    return m + 1