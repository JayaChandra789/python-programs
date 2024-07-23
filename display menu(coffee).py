#Program using List,def,condition statements
menu_items=["normal coffee","cappuccino","latte","cold coffee,hot coffee"]#list
def display_menu1(user_input):#def
    if user_input=="menu":#condition statements
     return menu_items
    else:
     return "Invalid"#
    
user_input=input("Ask menu to display menu: ")
view=display_menu1(user_input)
print(view)

def select_coffee(user_input2):
    if user_input2=="normal coffee":
      return "normal coffee"
    elif user_input2=="cappuccino":
      return "Cappuccino"
    elif user_input2=="latte":
      return "Latte"
    elif user_input2=="cold coffee":
      return "Cold coffee"
    elif user_input2=="hot coffee":
      return "cold coffee"
    else:
     return "Not Available bro"
user_input2=input("Enter your coffee name from the menu: ")
user_input2=user_input2
if user_input2=="normal coffee":
    print(f"Your {user_input2 } will be prepared in 5 mins Bro ")
elif user_input2=="cappuccino":
    print(f"Your {user_input2 } will be prepared in 5 mins Bro ")
elif user_input2=="cold coffee":
    print(f"Your {user_input2 } will be prepared in 5 mins Bro ")
elif user_input2=="latte":
    print(f"Your {user_input2 } will be prepared in 5 mins Bro ")
elif user_input2=="hot coffee":
    print(f"Your {user_input2 } will be prepared in 5 mins Bro ")
else:
    print("Please choose the coffee from the menu/Not available")


     
