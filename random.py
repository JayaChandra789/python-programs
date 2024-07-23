'''
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)

x=int(input("Enter Base"))
n=int(input("Enter power"))
result=power(x,n)
print(f"The power of a given number is {result}")'''


