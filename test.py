password = 4466

if password == 4466:
    input("Please enter your password")
    print("welcome to options")
   
else:
    print("password was wrong")
        

import re

def validate_password(password):
    # Check length
    if len(password) < 5:
        return False, "Password is invalid"
    
    # Check for digits
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    
    # Check for special characters
    if not re.search(r"[#*]", password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is Success."

# Example usage
password = input("Enter a password to validate: ")
is_valid, message = validate_password(password)
print(message)



import re
import sys

def validate_password(password):
    # Check length
    if len(password) < 5:
        print("Password must be at least 5 characters long.")
        sys.exit()
    # Check for digits
    if not re.search(r"[0-9]", password):
        print("Password must contain at least one digit.")
        sys.exit()
    
    # Check for special characters
    if not re.search(r"[#*]", password):
        print("Password must contain at least one special character.")
        sys.exit()
    
    print("Password is valid.")

# Example usage
password = input("Enter a password to validate: ")
validate_password(password)  



for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 4 == 0:
        string = string + "Buzz"
    if num % 4 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string) 





# list items
# create a list of items
items = ["item1","item2","item3","item4"]
# read the list of the items
print(items)
# update a list of items
items[0] = "banana"

# delete list of the items
del items[0]


# extending items
items.extend(["item4","item5","item6"])
print(items)

# filter list of the items
item = items[0]
print(item)

# dictionary

items = {
    "item_name": "Apple",
    "Description": "fruit",
    "price": 15.99,
    "stock": "20"
}
print(items)

# function

def message():
    return  "hello mr jerry"
result = message()
print(result)

def add(a,b,c,d):
    return a+b*c*d
result2 = add(2,2,5,5)
print(result2)

# lambda
multi = lambda x,y: x*y
print(multi(5,5))


