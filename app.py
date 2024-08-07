import datetime
# import re
def buy_airtime():
    cash = 1000
    x =datetime.datetime.now()
    amount = int(input("Enter amount: "))
    balance = cash - amount
    print("Airtime", amount, "Bought on",x,"at","New balance is",balance )
# def validate_password(password):
#     # Check length
#     if len(password) < 5:
#         return False, "Password is invalid"
#     sys.exit()
    
#     # Check for digits
#     if not re.search(r"[0-9]", password):
#         return False, "Password must contain at least one digit."
    
#     # Check for special characters
#     if not re.search(r"[#*]", password):
#         return False, "Password must contain at least one special character."
    
#     return True, "Password is Success."

# # Example usage
# password = input("Enter a password to validate: ")
# is_valid, message = validate_password(password)
# print(message)

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


def deposit():
    cash = 1000
    amount = int(input("Enter amount: "))
    new_balance = cash + amount
    print("Amount", amount, "Deposited successfully new balance is :", new_balance )

def send_money():
   cash = 1000
   x =datetime.datetime.now()
   reciever = int(input("Enter the  number: "))
   amount = int(input("Enter amount: "))
   if amount > 0 and amount <= cash:
     new_bal = cash - amount
     print("cash", amount, "sent to ",reciever,"on",x,"at","new balance is",new_bal )
   else:
     print("Insufficient Balance")

  
def withdraw():
    cash = 1000
    x =datetime.datetime.now()
    agent = int(input("Enter agent number: "))
    amount = int(input("Enter amount: "))
    if amount > 0 and amount <= cash:
      remaining_cash = cash - amount
      print("cash", amount, "Withdrawn successfully from agent number",agent,"on",x,"at","balance is: ",remaining_cash )
    else:
      print("Insufficient Balance")

def pay_bill():
   cash = 1000
   x =datetime.datetime.now()
   paybill = int(input("Enter paybill number: "))
   amount = int(input("Enter amount: "))
   if amount > 0 and amount <= cash:
     bal = cash - amount
     print("cash", amount, "paid to ",paybill,"Agencies on",x,"at","new balance is",bal )
   else:
     print("Insufficient Balance")
   
while True:
  print("Welcome to Ebirr")
  print("1.Send money")
  print("2.Deposit Cash")
  print("3.Withdraw Money")
  print("4.Buy airtime")
  print("5.Pay bill")

  user =int(input("Choose Option: "))
  if user ==1:
    send_money()
  elif user ==2:
    deposit()
  elif user ==3:
    withdraw()
  elif user ==4:
    buy_airtime()
  elif user ==5:
    pay_bill()
  else:
   print("Invalid Option: ")
  

