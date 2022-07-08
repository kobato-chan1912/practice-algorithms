# where A,B are square matrices
def mul(A, B, MOD):
    K = len(A);
    C = [[0 for i in range(K)] for j in range(K)] ;
    for i in range(1, K):
        for j in range(1, K):
            for k in range(1, K):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
    return C;
 
# Computes A^n
def power( A,  n):
    if (n == 1):
        return A;
    if (n % 2 != 0):
 
        # n is odd
        # A^n = A * [ A^(n-1) ]
        A = mul(A, power(A, n - 1), 1000000007);
    else:
        # n is even
        # A^n = [ A^(n/2) ] * [ A^(n/2) ]
        A = power(A, n // 2);
        A = mul(A, A, 1000000007);
     
    return A;


class Solution:
    #Function to count number of ways to reach the nth stair.

    def countWays(self,n):
        F = [0 for i in range(3)];
        F[1] = 1;
        F[2] = 2;
        K = 2;
        MOD = 1000000007;
     
        # create K*K matrix
        C = [[0 for i in range(K+1)] for j in range(K+1)];
       
        for i in range(1,K):
            C[i][i + 1] = 1;
         
        # Last row is the constants c(k) c(k-1) ... c1
        # f(n) = 1*f(n-1) + 1*f(n-2)
        C[K][1] = 1;
        C[K][2] = 1;
     
        if (n <= 2):
            return F[n];
     
        # f(n) = C^(n-1)*F
        C = power(C, n - 1);
        result = 0;
     
        # result will be the first row of C^(n-1)*F
        for i in range(1,K+1):
            result = (result + C[1][i] * F[i]) % MOD;
         
        return result;

        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends