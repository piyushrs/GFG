#User function Template for python3

from typing import List
from queue import Queue
from collections import deque

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        bfs_traversal = []
        vis = [False]*V
        q = deque()
        q.append(0)
        vis[0] = True

        while q:
            g_node = q.popleft()
            bfs_traversal.append(g_node)
            for k in adj[g_node]:
                if(vis[k] == False):
                    vis[k] = True
                    q.append(k)
        return bfs_traversal


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends