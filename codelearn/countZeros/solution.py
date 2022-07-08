def countZeroDigit(a,b):
  count=0
  for x in range(a,b+1):
    count+=str(x).count('0')
  return count

