"""
Decimal to binary can be acheived by '
1. Divide the decimal by 2 -
2. Get the reminder
3. Divide the quotient by 2
4. Repeat the steps till the quotient becomes 0

All the reminders  in above operation will be in binary

Reversion the sequence of reminder will get us the binary equivalent

To form it as a recursive problem
We have recursively diveide the quotient by 2
base case will be quotient becomes 0

We know that binary of 0 is 0
1 is 1
2 is 10
3 is 11
4 is 100
5 is 101


base case if n == 0 return 0

recursive case
f(n) = n mod 2 + 10 * f(n//2)

"""
def dec2bin(n):

  assert isinstance(n,int),'Input must be an integer'

  if n == 0:
    return 0
  else:
    return n%2 + 10 * dec2bin(n//2)


print(dec2bin(2.3))
