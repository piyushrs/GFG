#User function Template for python3
from itertools import combinations

class Solution():
    def countSubstring(self, S):
        #your code here
        num = int(S)
        l = set()
        if num == 0:
            return 0
            
        total_count = 0
        
        for i in range(1, len(S)+1):
            a = combinations(S, i)
            for j in a:
                l.add("".join(j))
                
        for i in l:
            count_0, count_1 = 0, 0
            if len(i) > 1:
                for j in i:
                    if int(j) == 0:
                        count_0 += 1
                    else:
                        count_1 += 1
            else:
                if int(i) == 1:
                    count_1 += 1
                elif int(i) == 0:
                    count_0 += 1
            if count_1 >= count_0:
                total_count += 1
                
        return total_count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(Solution().countSubstring(s))
# } Driver Code Ends