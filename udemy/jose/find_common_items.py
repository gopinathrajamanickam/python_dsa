"""
This module aims to find the common elements between two lists
Author : Gopinath  Rajamanickam
Date: 6 Oct 2023
"""
from typing import List

def get_common_items(customers: List[int], suppliers: List[int]) -> List[int]:
    """
    To find the common ids between customers and suppliers

    Args:
        customers (List[int]): customer id list
        suppliers (List[int]): supplier id list

    Returns:
        List[int]: common ids
    """
    # for customer_id in customers:
    #     if customer_id in suppliers:
    #         common_ids.append(customer_id)
    # return common_ids

    # custs = set(customers)
    # supps = set(suppliers)

    # common_ids = list(custs.intersection(supps))
    # return common_ids
    return sorted(list(set(customers).intersection(set(suppliers))))

if __name__ == "__main__":
    cust =  [1,2,3,4,5,5,3]
    supp =  [4,5,6,7,8]
    print(f"Partners that are both suppliers and customers"
          f" are {get_common_items(cust,supp)}")
