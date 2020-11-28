class StockSpanner:

    """
    use a stack to contain both the price and the span
    only store the last price in a increasing subarray and the number of counts for the subarray.
    """
    def __init__(self):
        self.stack = []
        
    def next(self, price):
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            count += self.stack.pop()[1]
        self.stack.append([price, count])
        return count
        
        

        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
