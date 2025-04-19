def buySellStock(prices):
    # DEFINING THE POINTERS FOR PRICES AT INDECIES(which is ith day for price)
    left,right=0,1
    # MAXPROFIT TRACKS THE MAX PROFIT 
    maxProfit=0
    # RUNNING LOOP UNTIL REACHES THE LAST INDEX
    while right<len(prices):
        # IF PRICE OF LEFT IS LOWER THAN RIGHT SUBTRACT RIGHT FROM LEFT AND UPDATE PROFIT
        if prices[left]<prices[right]:
            profit=prices[right]-prices[left]
            maxProfit=max(profit,maxProfit)
        # IF RIGHT IS LOWER THAN LEFT THEN UPDATE LEFT POINTER TO THE INDEX OF RIGHT
        else:
            left=right
        # REGARDLESS OF SITUATION INCREASE THE RIGHT POINTER
        right+=1
    # print(maxProfit)
    return maxProfit
buySellStock([12,4,7,3,4])
buySellStock([10,1,5,6,7,1])

"""
TIME COMPLEXITY  :O(N)
SPACE COMPLEXITY :O(1)
"""
"""
METHOD TO SOLVE :
WE ONLY HAVE TO TRACK THE LOWEST PRICE ON THE iTH DAY AND CHECK IF THE CURRENT IS LOWER(left pointer) THAN FOWARD(right pointer) IF YES THEN CHECK PROFIT
AND COMPARE AND UPDATE IF PROFIT IS GREATER THAN PREVIOUS MAX PROFIT(maxProfit)

------------------------------------------------------------------------------------------------------------------------------------------------
PSUEDO CODE
------------------------------------------------------------------------------------------------------------------------------------------------
1.DEFINE THE POINTERS AND VALUES 0 AND VALUE OF 1
2.DEFINE MAX PROFIT 
3.RUN LOOP UNTIL REACHES THE LAST INDEX
4.CHECK IF LEFT POINTERS IS LOWER THAN RIGHT CHECK PROFIT(by subtracting ) 
5.COMPARE BOTH THE PREVIOUS AND CURRENT PROFIT AND CHANGE ACCRODINGLY(with max()->function)
6.ELSE WHEN RIGHT IS LOWER THAN LEFT UPDATE THE INDEX OF IT TO RIGHT (cause we only track the lowest and we should point the lowest)
7.INCREMENT THE RIGHT (cause we have to check foreward day's prices and compare pricing )
8.RETURN MAXPROFIT(maxProfit)
------------------------------------------------------------------------------------------------------------------------------------------------

"""