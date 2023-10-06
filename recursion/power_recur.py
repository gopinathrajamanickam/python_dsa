"""
power or exponential of a number base by another number exp is
obtained by recursively multiplying the same number base , exp number of times

"""

def power(base, exp):
  # contraint case
  assert isinstance(base,int) and base >= 0 and int(base) == base,f'Base {base} should be a positive integer'
  assert isinstance(exp,int) and exp >= 0 and int(exp) == exp,f'Exponent {exp} should be a positive integer'
  # base case
  if exp == 0:
    return 1
  if exp == 1:
    return base
  # recursive case
  return base * power(base,exp-1)

if __name__ == "__main__":
  cases = [(6,0),(1,3),(3,1),(4,2),(3.2,2),(2,3.4),(4, -1),('s','s')]
  for i,j in cases:
    try:
      print(f'{i} to the power of {j} is {power(i,j)}')
    except AssertionError as msg:
      print(msg)
  print('Program completed')



