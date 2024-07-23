#program to print squares of given numbers
x=int(input("Enter a number:"))
def squares(x):
 if x==0:
  return 0
 else:
  value=x*x
  return value

result=squares(x)  #Note:after def the program should be ended with space indendent otherwise it wont give output
print(f"Squares of given number is {result}")#to print there 2 types one is ("",..),(f"").[f is used to print more than result]
 
