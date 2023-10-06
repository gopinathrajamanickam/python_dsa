"""
Purpose : To rotate the array elements by n positions
i.e. given  an array as [1,2,3,4,5] and n as 3
then expected output is [4,5,1,2,3]
"""
# Read the last element and store in first position of a new array
# in other words reverse the array
# Repeat this reversal process every n number of times
# Reversal does not work because on the second iteration the array
# comes back to its oiginal form
# instead let me try  with the two pointer approach
# Let me have 2 pointers , one pointing to the first position
# of the list and second  pointing after nth number
# say if the oiginal list size is 5 and number of positions to shift is 3
# then start should be at index 0 and end to be at index 3
# Create a new array with elements from end point till end of the array
# and place fom  first element till the nth position
# above logic may hold good if n is < length of the array
# in case the n > len(arr) then find the modulus of n/len(arr)


from typing import List

def shift_array(arr: List[int], n: int) -> List[int]:
    # Edge case
    if not arr or n <= 0:
        return  arr

    # Calculate the modulus
    n %= len(arr)

    # By rotating we are just rearranging the elements
    result = arr[-n-1:] + arr[:-n-1]

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 2
    print(shift_array(arr, 2))
