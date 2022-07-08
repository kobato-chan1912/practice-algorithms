#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        K = [[0 for x in range(W+1)] for y in range(2)]
     
        for i in range(n + 1):
            for w in range(W + 1):
                if (i == 0 or w == 0):
                    K[i % 2][w] = 0
                elif (wt[i - 1] <= w):
                    K[i % 2][w] = max(
                        val[i - 1]
                        + K[(i - 1) % 2][w - wt[i - 1]],
                        K[(i - 1) % 2][w])
     
                else:
                    K[i % 2][w] = K[(i - 1) % 2][w]
     
        return K[n % 2][W]


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends