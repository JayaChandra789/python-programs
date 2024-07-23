x=int(input("Enter a number1:"))
y=int(input("Enter a number2:"))
def add(x,y):
 return x+y
def subtract(x,y):
    return x-y
def mutliply(x,y):
    return x*y
def division(x,y):
 if y==0:
  print("invalid command given cant devide x,y")
 else:
  return x/y
choice=input("enter a number for calculation from 1,2,3,4")
if choice=='1':
 print(x+y)
if choice=='2':
 print(x-y) 
if choice=='3':
 print(x*y) 
if choice=='4':
 print(x/y)
else:
    print("invalid command")
