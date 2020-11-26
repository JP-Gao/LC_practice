class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if T[j] > T[i]:
                    ans[i] = j-i
                    break
        return ans
    # time O(n2)
    # space O(n)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n
        stack = [] # recording indices instead of temperatures since temperatures will duplicate.
        for i, t in enumerate(T): # use enumerate to loop index and number
            while stack and t > T[stack[-1]]: # while stack is not empty and current number is larger than the number associated with stack top index
                cur = stack.pop() # pop the stack pop index
                ans[cur] = i - cur # store the distance to the ans corresponding index
            stack.append(i) # if stack is none or not larger temperature found, just push the index to the top.
        return ans
    # time O(n)
    # space O(n)??
