
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize stack, hashmap and ans array
        stack = []
        hashmap = {}
        ans = []
        for i in range(len(nums2)):
            # when there is at least one element and the next number in nums2 is larger than the top of stack, pop out the stack top element, and store the top:nums2[i] into hashmap, this is a successful pair
            while len(stack) > 0 and nums2[i] > stack[-1]:
                hashmap[stack.pop()] = nums2[i]
            # when either of these two condition is met, simply push next element in nums2 to the stack
            stack.append(nums2[i])
            # for element left in stack (no pairs), assign -1 to these elements
        while len(stack) > 0:
            hashmap[stack.pop()] = -1
        # for each of the element in nums1, find the corresponding number in the hashmap.
        for i in range(len(nums1)):
            ans.append(hashmap[nums1[i]])
        return ans
    
    # time: 
