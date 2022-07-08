def secondChar(s):  
        D ={}
        S =set()
        for i in range(0,len(s)):
            t = 0
            for j in range(0,len(s)): 
                if s[j] == s[i]: 
                    t +=1 
            D.setdefault(t, s[i] )
            S.add(t)
        S.remove(max(S))
        if len(S) >=1:
            x = max(S)
            y = D[x]
            return y
        if len(S) == 0: 
            return '?'