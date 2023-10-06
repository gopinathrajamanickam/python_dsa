"""
Identify Unique Customer
You have a list of customer IDs in an array called ""customerIDs"".
Each customer ID appears twice except for one unique customer.
Write a function to identify the unique customer ID.
Can you identify a solution that only needs linear run time?
"""
from typing import List

def find_unique_customer_ids(customers: List[int]) -> List[int]:
    """
    Purpose: Find a list of customers that are unique in the given list

    Args:
        customers (List[int]): Given customer list

    Returns:
        unique customers (List[int]) :
    """
    cust_dict = {}

    for cust in customers:
        if cust in cust_dict:
            cust_dict[cust] += 1
        else:
            cust_dict[cust] = 1

    uniq_cust = []

    for key,value in  cust_dict.items():
        if value == 1:
            uniq_cust.append(key)

    return uniq_cust


if __name__ == "__main__":
    ids = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,7,8,9,10]
    print(f"List of unique customer ids are {find_unique_customer_ids(ids)}")
