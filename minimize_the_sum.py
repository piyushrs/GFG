#User function Template for python3
import heapq

class Solution:
    def minimizeSum(self, N, arr):
        total_sum = 0
        heapq.heapify(arr)
        while len(arr) != 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            running_sum = x+y
            total_sum += running_sum
            heapq.heappush(arr, running_sum)
        return total_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends