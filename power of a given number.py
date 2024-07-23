def power(x,n):
    if n==0:
     return n
    elif n==1:
     return x
    else:
     return x*power(x,n-1)#def ane function ikkaditho close{indicating with giving space},ippudu input ivvali def ni use cheyali

x=int(input("Enter number base"))
n=int(input("Enter number power"))
result=power(x,n)
print(f"The power of given number is: {result}")
