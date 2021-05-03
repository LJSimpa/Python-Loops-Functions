
                                                                        #INITIALIZE
def init():
    print('''Welcome to Integrity Bank'
    "Boundless possibilities"
    ''')
    haveAccount = int(input("Login (0) or Signup (1) \n"))
    if haveAccount == 0:
        validOptionSelected = True
        login()
        operations()
    elif haveAccount == 1:
        validOptionSelected = True
        signup()
    else:
        print("Invalid Option Selected. Please Try Again")
        init()


                                                                        #SIGNUP
def signup():
    mail = input("Email Address \n")
    global name
    name = input("Lastname Firstname \n")
    password = input("Password \n")
    accountNumber = acct()
    print("Welcome " + name+". Your account has been created.")
    print("This is your account number:",accountNumber)

    print("Please log in to your account")
    global database
    database = {accountNumber:password}
    login()    

                                                                     #GENERATE ACCOUNT
def acct(): 
    import random
    return random.randrange(1111111111,9999999999)


def currentAccountNumberValidation():
    # Check
    # If accountNumber is not empty
    # If account number is 10 digits
    # If account number is an integer
    if currentAccountNumber:
        if len(str(currentAccountNumber)) == 10:
            # if type(currentAccountNumber) == int:
            #     return True
            try:
                int(currentAccountNumber)
            except ValueError:
                print("Error. Account number must have no character other than numbers")
                login()
        else:
            print("Error. 10 digits are required for account number")
            login()
    else:
        print("Error. Account Number is a required field")
        login()



                                                                            #LOGIN
def login():
    global currentAccountNumber
    currentAccountNumber = input("Account Number \n")
    currentAccountNumberValidation()
    currentPassword = input("Input Password \n")
    database1 ={int(currentAccountNumber):currentPassword}
    print(database1)
    if database == database1:
        print("Welcome")
    else: 
        print("Wrong Account Number or Password, Try Again")
        login()
    import datetime
    now = datetime.datetime.now()
    print("You logged in at:"), print(now.strftime("%y-%m-%d %H:%M:%S"))
    print("These are your available options:")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint")
    print("4. Logout")
    operations()



                                                            #BANK OPERATIONS
def operations():
    selectedOption = int(input("Please select an option \n"))
    if selectedOption == 1:
        withdrawalAmount = (input("How much would you like to withdraw? \n"))
        print("Amount withdrawn = #"+withdrawalAmount)
        print("Please take your cash")

    elif selectedOption == 2:
        previousBalance = 2400
        deposit = int(input("How much would you like to deposit? \n"))
        currentBalance = previousBalance + deposit
        print("Previous balance = #{}".format(previousBalance))
        print("Amount deposited = #{}".format(deposit))
        print("Current Balance = #{}".format(currentBalance))
    elif selectedOption == 3:
        complaint = input("What issue will you like to report? \n")
        print("Thank you for contacting us")
    elif selectedOption == 4:
        print('''Thank you for banking with us.
        You are now logged out.
    ================================================
        ''')
        init()
    else:
        print("Invalid Option Selected. Please Try Again.")
        operations()

init()