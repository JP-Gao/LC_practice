# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isIdentical(s, t):
            # 注意edge case，当s或者t至少一个或者两个都是None的情况下，需要拎出来单独讨论。
            if s is None and t is not None:
                return False
            if s is not None and t is None:
                return False
            if s is None and t is None:
                return True
            # 当s和t都不为None的时候，需要进行比较node val以及左右分支
            if s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right):
                return True
            else:
                return False
        
        
        # 利用recursion，先给两个condition判断recursion的终止条件
        if isIdentical(s, t): # s t相同
            return True
        if s is None: # s变成None
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) # s的左右children分别于t进行比较，只要有一个成立，就是True
    # time, n is number of node in s, m is number of node in t
    # time, O(mn)
    # space, O(h), h is the height of the s tree; 
    # balanced tree, h = logn, worst case, h = n
    # recursion tree uses stack to store nodes?
                
        
        
        
