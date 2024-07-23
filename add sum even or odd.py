#program to print sum of even and sum of odd numbers
'''
x=int(input("Enter a number x:"))
y=int(input("Enter a number y:"))
if x==0:
 print(0)
elif y==0:
 print(0)
elif x%2==0 and y%2==0:
 print("Even number",x+y)
else:
 print("Odd number",x+y)'''

def sumof_even_odd(x,y):
    if x==0 and y==0:
     return 0
    elif x%2==0 and y%2==0:
     return x+y
    elif x%2!=0 and y%2!=0:
     return x+y
    else:
      return "Enter any two even or odd numbers for sum"  
x=int(input("Enter number1: "))
y=int(input("Enter number2: "))
result=sumof_even_odd(x,y)
print(result)
if x%2==0 and y%2==0:
 print(f"The sum of even numbers is: {sumof_even_odd(x,y)}")
else:
 print(f"The sum of odd numbers is: {sumof_even_odd(x,y)}")   

