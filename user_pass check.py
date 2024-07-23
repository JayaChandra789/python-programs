username=(input("Enter username"))
password=(input("Enter password"))
def user_pass_verify(usr,pswd):
    if usr=="jaya" and pswd=="chandra":
        return "Accept"
    else:
        return "Dont Accept"

verify=user_pass_verify(username, password)
if verify=="Accept":
 print("Access granted")
else:
 print("Access denied")

'''username = input("Enter username: ")
password = input("Enter password: ")
def user_pass_verify(usr, pswd):
    if usr == "jaya" and pswd == "chandra":
        return "Accept"
    else:
        return "Don't Accept"

verify = user_pass_verify(username, password)

if verify == "Accept":
    print("Access granted")
else:
    print("Access denied")'''
#my own
def pass_verify(usern,passw):
  if  usern=="jaya" and passw=="12345":
   return "True"
  else:
    return "False"  
usern=input("Enter username: ")
passw=input("Enter password: ")
result=pass_verify(usern,passw)
print(result)
if result=="True":
 print("Access Granted")
else:
 print("Access denied")

