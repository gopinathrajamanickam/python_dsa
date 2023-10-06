"""
Find the sum of digits in a given number

logic recursively divide and add the remainders till the quotient becomes single digit

"""
def sumOfDigits(num):
  # constraint case
  assert num >= 0 and int(num) == num, "Input must be a positive integer"
  # base case
  if int(num//10) == 0:
    return int(num)
  else:
    # recursive case
    return int(num%10) + sumOfDigits(int(num//10))

if __name__ == "__main__":
  cases = [0,1,10,22,1039,33,-1]

  for i in cases:
    try:
      print(f'Sum of Digits in {i} is {sumOfDigits(i)}')
    except AssertionError as msg:
      print(f'Invalid input {i} : {msg}')

