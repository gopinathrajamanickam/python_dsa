def gcd(a, b):
  assert isinstance(a,int) and isinstance(b,int), 'The numbers must be integers'

  if b == 0:
    return a
  else:
    return gcd(abs(b),abs(a%b))

if __name__ == "__main__":
  cases = [(6,3),(12,4),(-4,12),(48,9.4)]
  for i,j in cases:
    try:
      print(f'GCD for {i} and {j} is : {gcd(i,j)}')
    except AssertionError as msg:
      print(f'Invalid input {i, j}  : {msg}')
  print('program completed')

