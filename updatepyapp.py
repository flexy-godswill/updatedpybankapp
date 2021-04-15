import datetime
import random
import string
import time

datetime_object = datetime.datetime.now()
print(datetime_object)

database = {}

def init():
    validOptionSelected = False
    print("Welcome To Parrot's Bank")
    
    haveAccount = int(input("Do You Have An Account With Us?? \n 1. Yes \n 2. No \n"))

    if(haveAccount == 1):
        validOptionSelected = True
        login()
        
    elif(haveAccount == 2):
        validOptionSelected = True
        register()
    else:
        print("You HAve Selected An Invalid Option")
        init()
            
def login():
    print("::: ::: Login ::: ::: \n")
    print("Enter Your Details To Continue Transaction \n")
    accountNumberUser = int(input("Please Enter Your Account Details To Continue \n"))
    passPin = input("Enter Your Parrot Account Pin, Ensure That No One Is Watching; Guide Your Pin Very Well \n")
    
    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberUser):
            if(userDetails[3] == passPin):
                bankOp(userDetails)
                isLoginSuccessful = True

            else:
                print("\n Invalid Account Number Or PassPin")
                print("Please Login Again To Continue")
                login()
        else:
            print("Invalid Account Number Or PassPin")
            login()

def register():
    print("\n ::::: :::Join Parrot's Bank To Have A Swift Bank Transactions::: :::: \n")
    firstName = input("Enter Your First Name: \n")
    lastName = input("Enter Your Last Name: \n")
    email = input("Enter Your E-mail Address: \n")
    length = int(input("Due To Security Reasons, We Would Be Generating A Banking Pin For You \n You are Only Expected To Enter The Length Of PassPin: "))
    all = string.digits
    password = "".join(random.sample(all,length))
    print("This is YOur Generated Banking Pin: %s" %password)   
    accountNumber = generatedaccountnumber()
    fullName = firstName + lastName
    print("::: ::::: Welcome, %s :::::::::::::::" %fullName)
    print(datetime_object)
    print("")
    print("::: ::::: Congrats!!!, You Have succesfuully Created An Account With Parrot's Bank::::: This Is Your Account Number: %d :::" %accountNumber)
    print("")
    print("::: ::::: Do Not Reveal Your Details To Anyone ::::: :::")
    print("")
    database[accountNumber] = [firstName, lastName, email, password]
    login()
            
def bankOp(user):
    print(":|:|:|:|:|:|:|:|:|: Voila!!!.......... You Are Logged In!!! :|:|:|:|:|:|:|:|:|:")
    print(datetime_object)
    selctedOption = int(input("What Would You Like To Do?? \n 1. Withdraw \n 2. Deposit \n 3. File A Complaint \n 4. Check Balance \n 5. Logout \n 6. Exit \n"))
    if(selctedOption == 1):
        withdraw()
    elif(selctedOption == 2):
        deposit()
    elif(selctedOption == 3):
        complaint()
    elif(selctedOption == 4):
        checkBalance()
    elif(selctedOption == 5):
        login()
    elif(selctedOption == 6):
        exit()
    else:
        print("You HAve Selected An Invalid Option")
        bankOp(user)

    
def generatedaccountnumber():
    return random.randrange(1111111111, 9999999999)
    
def withdraw():
    balance = 75000
    cash = int(input("How Much Would You Like To Withdraw?? \n Enter Amount... \n"))
    remBal = balance - cash
    if (cash < balance):
        time.sleep(3)
        print("Transaction Successful, Please Take Your Cash, Here's Your Remaining Balance: %s" % remBal)
    elif(cash > balance):
        print("Insufficient Funds")
    complete()
    
def deposit():
    balance = 75000
    deposit = int(input("How Much Would You Like To Deposit?? \n"))
    total = deposit + balance
    print("Waiting To Receive Alert....." )
    time.sleep(3)
    print("Your Current Balance is %s" %total)
    complete()
    
def complaint():
    palava = input("What Issues Would You Like To Report?? \n")
    time.sleep(2)
    print(palava)
    print("We Have Received Your Complaint, We Will Get Back To You As Soon As You Can...Have A Nice Day")
    complete()
    
def checkBalance():
    balance = 75000
    time.sleep(3)
    print("Your Account Balance Is %s" %balance)
    complete()
    
def complete():
    option = int (input("Dear Valued Customer, Would You Like To Make Another Transaction??? \n 1. Yes \n 2. No \n"))
    if(option == 1):
        time.sleep(3)
        print("Enter Your Details Again To Continue")
        login()
    elif(option == 2):
        print("Thanks For Banking With Us, Have A Nice Day")
    else:
        print("You Have Selected An Invalid Option, Try Again")
        complete()
        
        
def logout():
    print("::::::::::::::: Ciao ::::::::::::::: \nYou Are Logged Out Of Your Account, Will You Like To Login Again??? %d" % login)
        

def exit():
    print("::::::::::::::: Have A Nice Day :::::::::::::::")
    
init()