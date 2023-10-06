"""
This program is to find the maximum profit possible based on the given list of stock
prices for each day

Contraints:
    1. For each day we can buy or sell or do nothing
    2. Can hold only one stock at a time

Happy path:
    1. input : [7,1,5,3,6,4], expected output is 6 because if we buy at $1 and sell
                              at 6$ then we get $5 profit
    2. input : [7,6,4,3,1] , Expected output is 0 as price is in downward trend and
                             it will be only loss

Edge cases :
    1. length of input is 0 or 1 . Then 0

"""
from typing import List

def get_max_profit(prices: List[float]) -> float:
    """

    Args:
        prices (List[float]): List of stock prices indexed on day

    Returns:
        float: maximum profit possible
    """

    # initialize variables
    max_profit, diff = 0, 0

    for i,val in enumerate(prices):
        # print(f"Value on day {i} is {val}")
        if i < len(prices)-1:
            diff = max(prices[i+1:]) - val
            # print (f"Diff is {diff}")
            if max_profit < diff:
                max_profit = diff

    # print(f"Max poffit is {max_profit}")
    return (max_profit*1.0)

if __name__ == "__main__":
    ## Testing
    prices = [7, 1, 5, 3, 6, 4]
    print(get_max_profit(prices))
    assert get_max_profit(prices) == 5.0

    prices = [7, 6, 4, 3, 1]
    print(get_max_profit(prices))
    assert get_max_profit(prices) == 0.0
