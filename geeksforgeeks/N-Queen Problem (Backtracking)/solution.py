def black(i,j,notpos,n):
    #black all positions below i,j
    for ii in range(i,n):
        notpos[ii][j] += 1
    #black diagonally down and right
    for ii in range(j,n):
        if i + ii - j < n:
            notpos[i + ii - j][ii] += 1
    #black diagonally down and left 
    for ii in range(j):
        if i + j - ii < n:
            notpos[i + j - ii][ii] += 1
            
            
def unblack(i,j,notpos,n):
    for ii in range(i,n):
        notpos[ii][j] -= 1
    for ii in range(j,n):
        if i + ii - j < n:
            notpos[i + ii - j][ii] -= 1
    for ii in range(j):
        if i + j - ii < n:
            notpos[i + j - ii][ii] -= 1            
        


def solve(level,pattern,notpos,ans,n):
    if level == n:
        ans.append(pattern)
        return 
    
    for i in range(n):
        if notpos[level][i] == 0:
            black(level,i,notpos,n)
            solve(level + 1,pattern + [i + 1],notpos,ans,n)
            unblack(level,i,notpos,n)

class Solution:
    def nQueen(self, n):
        # code here
        notpos = [[0]*n for _ in range(n)]
        ans = []
        solve(0,[],notpos,ans,n)
        return ans 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends