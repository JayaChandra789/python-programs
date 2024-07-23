
def count_elements(s):
         capitals=sum(1 for c in s if c.isupper())
         smalls=sum(1 for c in s if c.islower())
         digits=sum(1 for c in s if c.isdigit())
         words=len(s.split())
         return capitals,smalls,digits,words
s=input("Enter string and number")
caps,smalls,digts,words=count_elements(s)
print(f"Capitals: {caps}, Smalls: {smalls}, Digits: {digts}, Words: {words}")


'''
import pickle
data={'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('data.pkl', 'wb') as file:
 pickle.dump(data, file)
print("Data written to binary file successfully.")'''

