# User Registration SignIn SignUp
from database import *
from customer import *
from bank import Bank
import random

def SignUp():
    username = input("Create Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = random.randint(10000000 ,99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Yours Account Number",account_number)
                break
    cobj = Customer(username, password, name, age, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()

    
def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()}Enter Password: ")
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign In Succesfully")
                return username
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct username")
        SignIn()


