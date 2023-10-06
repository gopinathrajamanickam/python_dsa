"""
Date : 10/1/2023
Author : Gopinath Rajamanickam

Filename : codes.py
Purpose : This contains code snippets that are efficient

This is a module docsting
"""
def demonstrate_walrus() -> None:
    """
    Name : demonstrate_walrus
    Pupose : To demonstrate the capabilities of Walrus operator " := "
    Parameters : None
    Returns : None
    """
    value = 11
    if value > 10:
        print(value)

    # instead of above we can use
    if (value := 12) > 10:
        print(value)

def demo_fstrings() -> None:
    """
    Name : demo_fstrings
    Purpose : To Demostrate use of fstring notation
    parameters : none
    return : none
    """
    # A typical pint statement would involve spcifying the variable and the data type
    # of each variable being printed.
    # this is not so readable. f stings make it so simple to concatenate
    # variable value with the string
    experience = 10
    rate = 78.5
    company = 'Google'
    # Previuusly it has to be printed like
    print("I have {} years of experience in company {}. My rate is {:.2f}"
          .format(experience,company,rate)
         )

    # With f string it can be simplified as
    print(f"I have {experience} years of experience in company {company}."
          f" My rate is {rate:.2f}")

def demo_list_comprehension() -> None:
    """
    Function name: demo_list_comprehension
    Purpose : To Demostrate use of fstring notation

    Paramters : None
    Return : None
    """
    # IF we want to apply a function or expression on all elements of a list
    nums = [1,2,3,4]
    sq_nums = []
    for num in nums:
        sq_nums.append(num ** 2)
    print(sq_nums)

    # alternatively we can use list comprehension
    sq_nums = [num ** 2 for num in nums]
    print(sq_nums)

    # list comprehension with if conditions
    nums = range(1,100)
    # Create a new list of integer as square of even numbers from the nums list
    sq_even_nums = [num ** 2 for num in nums if num%2 == 0]
    print(sq_even_nums)

def demo_map_filter() -> None:
    """
    Function name: demo_map_filter
    Purpose : To Demostrate use of map and filter notation

    Paramters : None
    Return : None
    """
    # List comprehensions are useful for simple functions but for a complex
    # function we can use the map to apply the function to all the items in
    # iterable and filter can be used to filter the results

    nums = range(1,20)
    sq_nums = list(map(lambda x:x ** 2, nums))
    print(sq_nums)

    # Filter
    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    print(even_nums)

def demo_lazy_loading():
    """
    Function name: demo_lazy_loading
    Purpose : To Demostrate use of lazy loading

    Paramters : None
    Return : None
    """
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1
    counter = count_up_to(5)

    # counter is a generator object
    # use next(counter) to get next value
    print(counter)       # generator object
    print(next(counter)) # 1
    print(next(counter)) # 2
    print(next(counter)) # 3
    print(next(counter)) # 4
    print(next(counter)) # 5
    # print(next(counter)) Errors

# Starting point for this code
if __name__ == "__main__":
    demonstrate_walrus()
    demo_fstrings()
    demo_list_comprehension()
    demo_map_filter()
    demo_lazy_loading()
