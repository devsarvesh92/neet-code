

def max_profit(prices:list[int])->int:
    profit = 0
    l,r = 0,1
    while r < len(prices):
        bp= prices[l]
        sp = prices[r]
        profit = max(profit,sp-bp)
        if sp < bp:
            l=r
        r+=1
    return profit
        

    
        



    
