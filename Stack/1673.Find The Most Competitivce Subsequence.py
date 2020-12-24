class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for index, value in enumerate(nums):
            # 当stack不为空，并且stack最顶部的元素大于nums cur 元素，并且stack去掉最后一个之后的元素个数（len(stack)-1）和nums中剩下的元素个数(len(A)-i)之和至少为k个，就可以继续stack pop
            while stack and stack[-1]>value and len(stack)-1+len(nums)-index >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(value)
        return stack
