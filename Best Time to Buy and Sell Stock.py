class Solution:
    def maxProfit2(self, prices: list):
        m = 0
        for i in range(len(prices)):
            x = max(prices[i+1:],default=0) - min(prices[:i+1],default=0)
            m = max(x,m)
        return m # order problem
    
    def maxProfit(self, prices: list):
        mi = prices[0]
        ma = prices[0]
        l_max = 0
        for i in range(len(prices)):
            if prices[i]>ma:
                ma = prices[i]
            if prices[i] < mi:
                if l_max < ma - mi:
                    l_max = ma - mi
                ma = mi = prices[i]         
        return max(ma - mi,l_max)

x = Solution()
# print(x.maxProfit([1]))
# print(x.maxProfit([1,4]))
# print(x.maxProfit([6,4]))
# print(x.maxProfit([7,1,5,3,6,4]))
# print(x.maxProfit([7,6,4,3,1]))
print(x.maxProfit([2,4,1,5]))
        