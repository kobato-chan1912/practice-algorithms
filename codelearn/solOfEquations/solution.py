def solOfEquations(k,a,b,c):
    t = k-(a+b+c);
    if (t<0): return 0
    s = (t+2)*(t+1)/2
    return s
