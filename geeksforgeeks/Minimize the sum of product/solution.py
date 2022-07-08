#User function Template for python3

class Solution:
    def minValue(self, A,B,n):
        A.sort()
        B.sort()
     
        # Multiplying minimum value of A and maximum
        # value of B
        result = 0
        for i in range(n):
            result += (A[i] * B[n - i - 1])
     
        return result
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends