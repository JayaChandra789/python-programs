'''#palindrome checker
name=input("Enter name: ")
def ispalindrome(name):
 name==malayalam and palindrome==malayalam
 if name==palindrome:
  return "Name is palindrome"
 else:
   return "entered is not palindrome"

result = ispalindrome(name)
print(result)'''


name = input("Enter name: ")

def is_palindrome(name):
    # Clean the name by removing spaces and converting to lowercase
    cleaned_name = name.replace(" ", "").lower()
    # Check if the cleaned name is equal to its reverse
    if cleaned_name == cleaned_name[::-1]:
        return "Name is a palindrome"
    else:
        return "Entered name is not a palindrome"

result = is_palindrome(name)
print(result)



    
    

