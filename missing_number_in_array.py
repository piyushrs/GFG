#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        a = set(array)
        for i in range(1, n+1):
            if i not in a:
                return i
                
        if len(array) == 1:
            return 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends