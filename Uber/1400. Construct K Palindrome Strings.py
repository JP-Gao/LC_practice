import collections
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        count = collections.Counter(s)
        
        odd = 0
        for key, val in count.items():
            odd += val % 2
        even = len(count) - odd
        
        if odd <= k:
            return True
        else:
            return False
            
