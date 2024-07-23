class Contact_book:
 def __init__(self,name,email,mobileno):
    self.name=name
    self.email=email
    self.mobileno=mobileno
 def display_info(self):
   print(f"name:{ self.name},email:{self.email},mobileno:{self.mobileno}")

person1=Contact_book("jaya","bagamjaya789@gmail.com",8008304916)
person1.display_info()

# Creating person2 with user inputs
name = input("Enter name: ")
email = input("Enter email: ")
mobileno = input("Enter mobile number: ")

person2 = Contact_book(name, email, mobileno)
person2.display_info()




