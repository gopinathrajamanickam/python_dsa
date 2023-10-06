# import sys

def factorial(n):
  # print(f'input value {n}')
  assert n>=0 and int(n) == n,'The number must be positive integer only'
  if n in [0,1]:
    return 1
  else:
    return n * factorial(n-1)

if __name__ == "__main__":
  # print(sys.getrecursionlimit())
  # by default the limit is 1000 and it tries and exits
  cases = [0,1,3,4,6,-2,2.3]
  for n in cases:
    try:
      print(f'factorial of {n} is {factorial(n)}')
    except AssertionError as msg:
      print(f"Invalid input : {n} : {msg} ")

  print('Completed the program')

