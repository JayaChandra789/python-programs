def add(x,y):
  return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def devide(x,y):
 if y==0:
  return "invalid command"
 else:
  return x/y

x=float(input("Enter a number1:"))
y=float(input("Enter a number2:"))

choice=int(input("choose a number 1.(Add),2.(Subtract),3.(Multiple),4.(Devide): "))
if choice==1:
 print("Addition is =",add(x,y))
elif choice==2:
 print("Subtraction is =",subtract(x,y))
elif choice==3:
 print("multiple is =",multiply(x,y))
elif choice==4:
 print("devide is =",devide(x,y))
else:
 print("invalid command")
 


