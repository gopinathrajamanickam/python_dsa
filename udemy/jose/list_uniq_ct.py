"""
Program to find the number of unique elements in the integer list
"""
from typing import List

def uniq_ct(database: List[int]) -> int:
    return len(list(set(database)))

print(uniq_ct([1,1,1,1,2,2,2,33,3,3]))
