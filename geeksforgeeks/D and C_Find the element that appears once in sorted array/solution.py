#User function Template for python3

class Solution:
     def findOnce(self,arr : list, n : int):
       # Complete this function
       if n == 1:
           return arr[0]
       elif n == 0:
           return -1
       
       for i in range(0,n,2):
           if i+1 > n-1:
               if arr[i] != arr[i-1]:
                   return arr[i]  
           if arr[i] != arr[i+1]:
               return arr[i]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends