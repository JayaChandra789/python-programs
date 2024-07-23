#program to print simple factorial
def factor(n):
 if n==0 or n==1:
  return 1
 else:
  return n*factor(n-1)
n=int(input("Enter a number: "))
x=factor(n)
print(x)
