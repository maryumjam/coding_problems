class Solution:
    def best_time_to_buy_and_sell_stock(self,prices):
        best_time_to_buy = 0
        best_time_to_sell = 0
        min_price= prices[0]
        max_profit =0
        min_day=0
        for i in range(1, len(prices)):
            profit = prices[i]-min_price
            if profit> max_profit:
                max_profit = profit
                best_time_to_buy = min_day
                best_time_to_sell = i
            if prices[i] < min_price:
                min_price = prices[i]
                min_day = i
        if max_profit> 0:
            print("Best Day to Buy:" , best_time_to_buy+1)
            print("Best Day to Sell:", best_time_to_sell+1)
            print("Maximum Profit", max_profit)
        else:
            print("No way to gain profit")

if __name__=='__main__':
    print("Hi")
    solution = Solution()
    prices = [10,9,9,9,5]
    solution.best_time_to_buy_and_sell_stock(prices)
