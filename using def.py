'''def sum_of_odd_even(x,y):
    if x==0 or x%2==0:
     return x+y
    elif y%2!=0:
     return x+y
    else:
     return none

x=int(input("enter a number:"))
y=int(input("enter a number:"))
result=sum_of_odd_even(x,y)

print(result)
if result%2==0:
    print(f"Number is Even: {result}")
elif result%2!=0:
     print(f"Number is Odd: {result}")'''

def sum_of_odd_even(x, y):
 if x == 0 or x % 2 == 0:
  return x + y
 elif y % 2 != 0:
  return x + y
  return x + y  # Ensure the function always returns a value
x = int(input("Enter a number: "))# Input from the user
y = int(input("Enter a number: "))
result = sum_of_odd_even(x, y)# Compute the result

print(result)# Print the result
if result % 2 == 0:# Determine if the result is odd or even and print
    print(f"Number is Even: {result}")
else:
    print(f"Number is Odd: {result}")



