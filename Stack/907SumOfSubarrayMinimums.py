class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Given [3, 1, 2, 4]
        以3作为minpoint，左边右边的subarray只有[3]， (0+1)*(0+1), 0和0分别是3左边和右边连续比3大于等于的数字，都是0个；
        以1位min，[3, 1], [3, 1, 2], [1]， [1, 2], [1, 2, 4]
        2， [2], [2, 4]
        4, [4]
        
        For arr[i], assume there are L consecutive numbers that are greater than A[i] in range
        A[0]~A[i-1], and therea are R consecutive numbers that are greater than A[i] in range
        A[i+1]~A[n-1]. So A[i] will be the min of (L+1)*(R+1) sequences.
        """
        # brute force (TLE, )
        kmod = 10**9 + 7
        n = len(arr)
        ans = 0
        for i in range(n):
            # init two steps, to left and to right
            left, right = 1, 1
            while i-left>=0 and arr[i-left]>arr[i]: 
                # to prevent duplicates, use > instead of >=
                left += 1
            while i+right<=n-1 and arr[i+right]>=arr[i]:
                right += 1
            ans += arr[i] * left * right
        return ans % kmod
    
    """
    The last thing that needs to be mentioned for handling duplicate elements:
Method: Set strict less and non-strict less(less than or equal to) for finding NLE and PLE respectively. The order doesn't matter.

For example, the above code for finding NLE is strict less, while PLE is actually non-strict less.
Remark: Although in both loop conditions the signs are set as >, for NLE, we make records inside the loop, while for PLE, records are done outside the loop.


    """
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        kmod = 10**9 + 7
        n = len(arr)
        left = [1] * n
        right = [1] * n
        
        stack = [] 
        # init a stack to store the tuple of elements and number of elements on the left that are larger than this element; 
        for i in range(n):
            while stack and stack[-1][0] > arr[i]:
                left[i] += stack.pop()[1]
            stack.append((arr[i], left[i]))
            
        stack = [] 
        # But for the right element, we need to change to larger and equal to this element to include duplicates. But if both >=, there will be double counting.
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= arr[i]:
                right[i] += stack.pop()[1]
            stack.append((arr[i], right[i]))
        ans = sum(a*l*r for a, l, r in zip(arr, left, right)) % kmod
        return ans
