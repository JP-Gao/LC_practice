class Solution:
    # Brute Force
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numsDup = nums + nums
        ans = [-1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i+1, len(numsDup)):
                if numsDup[j] > nums[i]:
                    ans[i] = numsDup[j]
                    break
        return ans
    # time: O(n2), space: O(n)
    
    
        # Use Stack
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        
        for i in range(len(nums) * 2):
            while stack and (nums[stack[-1]] < nums[i%len(nums)]):
                ans[stack.pop()] = nums[i%len(nums)]
            stack.append(i%len(nums))
        return ans    
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        numsDup = nums + nums
        ans = [-1] * n * 2
        for i in range(2*n):
            while stack and numsDup[stack[-1]] < numsDup[i]:
                ans[stack.pop()] = numsDup[i]
            stack.append(i)
        res = []
        for i in range(n):
            if ans[i] == -1:
                res.append(ans[i+n])
            elif ans[i+n] == -1:
                res.append(ans[i])
            else:
                res.append(min(ans[i], ans[i+n]))
        return res
