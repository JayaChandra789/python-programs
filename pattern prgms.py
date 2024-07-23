'''#1st method
for i in range(0,5):  #2.outer loop
 for j in range(0,5): #1.inner loop
  print("*",end=" ")#indentation should be perfect in python especailly in pattern programs(inner loop print)
 print()''' #outerloop print
'''
#2nd method(easy) #ex: print("Hello")
                       print("World") #output will print in 2 lines but to print in same line we use end="" in python
                       or By using
                       print("Hello",end="")
                       print("World") #output will print in same line dont go for next 2nd line by using end=" "
                       and use print() to break lines into coloumns
n=5
for i in range(n):
 print(" * "*n)'''

'''#3rd method
n=5
print(" * "*n) #print 5 times to get sqaure(idea)'''

'''#4th method
n=5
for i in range(n):
 for j in range(n):
  print(" * ",end="")  
 print()'''

'''#for right triangle
n=5
for i in range(n):
 for j in range(i+1): #increament from 0 to 4
  print(" * ",end="")  
 print()''' 
