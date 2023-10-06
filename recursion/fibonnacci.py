"""
Fib sequence is formed where each number is the sum of
preceeding two numbers
and sequence starts with 0 and 1
0,1,1,2,3,5,8,13,...

Program to generate fibonacci series of n elements

logic :
  Have a list to store the series
  find ith element and append to the list till n numbers attained

but for the purpose of recursion let us just find the nth element
"""

def fib(n):
  # contraints
  assert n >= 0 and int(n) == n,"Input must be a positive integer"
  # base case
  if n in [0,1]:
    return n
  # recursive case
  else:
    return fib(n-1) + fib(n-2)

def fib_series(n):
  assert n >= 0 and int(n) == n, 'Input must be a positive integer'
  res = [0,1]
  for i in range(2,n):
    res.append(res[i-1] + res[i-2])
  return res



if __name__ == "__main__":
  cases = [0,1,3,4,-2,3.5,20]
  for i in cases:
    try:
      print(f'Value of {i} th number in fib series is {fib(i)}')
    except AssertionError as msg:
      print (f'invalid input {i} : {msg}')

  for i in cases:
    try:
      print(f'Fib series upto {i} : {fib_series(i)}')
    except AssertionError as msg:
      print(f'Invalid input {i} : {msg}')

  print('Program completed')


