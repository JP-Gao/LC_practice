class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        """
        need to notice that, the number such as 1, 11, 111, 1111
        store all remaider to a set, at lost K-1 remainder (1, 2, 3, ..., K-1).
        So if we repeat more than K-1 times, we can safety stop the loop.
        
        
        """
        remainder_seen = set()
        num = 1
        length = 1
        while True:
            if num % K == 0:
                return length
            else:
                remainder = num%K
                num = 1 + num*10
                length += 1
                if remainder in remainder_seen:
                    return -1
                else:
                    remainder_seen.add(remainder)
        return length
