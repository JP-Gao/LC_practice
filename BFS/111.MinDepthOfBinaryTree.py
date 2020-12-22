# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# 理解题目：叶子节点leaf是指有数字val 并且children都是none。如果一个none，另一个不是，那么这个就不是叶子结点。

class Solution:
    # 1, DFS recursion
    def minDepth(self, root: TreeNode) -> int:
        #适合用level order traversal， BFS来做
        #因为如果用DFS，很可能左边到了很深的底部，但是右边只有一层，左边就白白search。
        
        #先用DFS做做试试
        if root is None:
            return 0
        if root.right is None:
            return self.minDepth(root.left) + 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    # time O(N), N is number of nodes
    # space, very unbalanced tree, O(N), pretty balanced tree, O(logN)
    # bad thing is all nodes need to be visited to ensure that the minimum depth would be found, 
        
        
    # 2, BFS iteration
    def minDepth(self, root: TreeNode) -> int:
        #再用BFS做做试试
        #use level order traversal, first leaf we reach corresponds to the mim depth
        # we do not need to iterate all nodes
        #BFS一般都是用deque来实现的
        if root is None:
            return 0
        depth = 1
        node_deque = deque()
        node_deque.append((depth, root))
        while node_deque:
            depth, root = node_deque.popleft()
            if root.left == None and root.right == None: # this means we reached a leaf
                return depth
            if root.left is not None:
                node_deque.append((depth+1, root.left))
            if root.right is not None:
                node_deque.append((depth+1, root.right))
    
    
    # 3, DFS iteration
    # DFS iteration就是用stack来
    def minDepth(self, root:TreeNode):
        if root is None:
            return 0
        else:
            depth = 1
            stack = [(depth, root)]
            min_depth = float('inf')
        while stack:
            depth, root = stack.pop()
            if root.left is None and root.right is None: # root is a leaf
                min_depth = min(depth, min_depth)
            if root.left is not None:
                stack.append((depth+1, root.left))
            if root.right is not None:
                stack.append((depth+1, root.right))
        return min_depth
            
