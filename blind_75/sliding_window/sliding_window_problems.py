

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


def longest_substring_without_rep_chars(input:str):
    i,j = 0,0
    window=set()
    long_len=0
    while j<len(input):
        if input[j] not in window:
            window.add(input[j])
            long_len = max(len(window),long_len)
            j+=1
        else:
            i+=1
            j=i
            window=set()
    return long_len

        

        
         

