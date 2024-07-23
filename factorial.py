#program  to print factorial of any numbers
'''i=int(input("Enter a number: "))
if i==0:
  print ("invalid command by user")
else:
  print("factorial of given is",i*(i-1))'''
number=int(input("Enter a number: "))
def factorial(i):
 for i in range(2,i+1):
  if i==0:
   print("0")
  elif i==1:
   print("1")
  else:
   print("the factorial of given number is: ",i * factorial(i-1))
 
