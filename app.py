import datetime
def buy_airtime():
    cash = 1000
    x =datetime.datetime.now()
    amount = int(input("Enter amount: "))
    balance = cash - amount
    print("Airtime", amount, "Bought on",x,"at","New balance is",balance )


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
      print("cash", amount, "Withdrawn successfully from agent number",agent,"on",x,"at","balance is: " )
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
  

