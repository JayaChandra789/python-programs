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

