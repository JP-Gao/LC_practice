class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # brute force
        # TLE, time O(n2), space O(1)
        n = len(A)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if A[i]<=A[j]:
                    res = max(res, j-i)
        return res
    
    # sorting approach
    # time: O(nlogn) due to sorting, space O(n)
    def maxWidthRamp(self, A):
        ans = 0
        maxIdx = len(A) # the right index
        tmp = [(num, i) for i, num in enumerate(A)]
        tmp.sort()
        for i in range(len(tmp)): # loop all the index that is in a increasing order of num values.
            ans = max(ans, tmp[i][i]-maxIdx)
            
            
            
            diff = tmp[i][1] - maxIdx # the distance
            ans = max(ans, diff) # get max ramp
            maxIdx = min(maxIdx, tmp[i][1])
        return ans
    
    
    # 也可以用stack来做
    def maxWidthRamp(self, A):
            stack = []
            res = 0
            n = len(A)
            # use a stack to store start candidates' index of the ramp
            # use a decreasing stack (strictly)
            for i in range(n):
                if not stack or A[i] < A[stack[-1]]:
                    stack.append(i)
            # scan from right to left, compare the current number with the one on the top of the stack, pop if greater(since j-1-i < j-i, so pop no problem)
            for i in reversed(range(n)):
                while stack and A[i] >= A[stack[-1]]:
                    res = max(res, i - stack.pop())

            return res
                
        
        
