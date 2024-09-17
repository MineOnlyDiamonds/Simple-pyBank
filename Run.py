import os
import shutil

pathToFile = os.path.dirname(os.path.abspath(__file__))
pathToBank = "Data/InfoBank/"
path_Loan = os.path.join(pathToFile, pathToBank + "loanPercentage.txt")
path_BankName = os.path.join(pathToFile, pathToBank + "name.txt")
fileL = open(path_Loan, "r")
LoanPercentage = fileL.read()
fileBN = open(path_BankName, "r")
BankName = fileBN.read()

def IDtoCustomer(ID):
    pathToCustomerTXT = "Data/customers/" + ID + ".txt"
    path = os.path.join(pathToFile, pathToCustomerTXT)

    lines = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            lines.append(line)

    name = lines[1]
    surname = lines[4]
    IDFind = lines[7]
    balance = lines[10]

    print()
    print("--------------------")
    print("Name:    ", name)
    print("Surname: ", surname)
    print("ID: ", IDFind)
    print("Balance: ", balance, "€")
    print("--------------------")
    print()

    return name, surname, ID, float(balance), path

def Options(name, surname, ID, balance, path):
    print("Select from options: \n 1 : Check Balance \n 2 : Withdraw \n 3 : Deposit \n 4 : Loan")
    option = int(input("Option: "))

    if option == 1:
        print(ID, "balance: ", balance)
    if option == 2:
        count = float(input("How much do you want to withdraw? : "))
        
        if count < 0:
            count = count * -1

        if count > balance:
            print("Sorry! You do not have enough money.")
        else:
            balance = round(balance - count, 3)

            with open(path, "w") as file:
                text = "Name: \n" + name + "\n\nSurname: \n" + surname + \
                    "\n\nID: \n" + ID + "\n\nBalance: \n" + str(balance)
                file.write(text)
                print("Succes!")
    if option == 3:
        count = float(input("How much do you want to deposit? : "))
        balance = round(balance + count, 3)

        with open(path, "w") as file:
            text = "Name: \n" + name + "\n\nSurname: \n" + surname + \
                "\n\nID: \n" + ID + "\n\nBalance: \n" + str(balance)
            file.write(text)
            print("Succes!")
    if option == 4:
        print("You will need to pay another", LoanPercentage, "% of loan.")
        count = float(input("How much do you want to loan? : "))

        if count < balance or count == balance:
            print("Sorry! You do have enough money on your account.")
        else:
            balance = round(balance - count / ((100 - int(LoanPercentage)) / 100), 3)

            with open(path, "w") as file:
                text = "Name: \n" + name + "\n\nSurname: \n" + surname + \
                    "\n\nID: \n" + ID + "\n\nBalance: \n" + str(balance)
                file.write(text)
                print("Succes! You must to pay back", balance * -1)
                
                print

    Start()

def Start():
    print("Choose from options: \n 1 : Login by ID \n 2 : Find an ID by Name and Surname \n 3 : Delete a account \n 4 : Register a new account")
    option = int(input("Option: "))

    if option == 1:
        print("Please insert customer's ID.")

        ID = str(input("ID: "))
        name, surname, ID, balance, path = IDtoCustomer(ID)
        Options(name, surname, ID, balance, path)
    if option == 2:
        name = input("Name: ")
        surname = input("Surname: ")

        pathToFile = os.path.dirname(os.path.abspath(__file__))
        pathToCustomers = "Data/customers"
        path = os.path.join(pathToFile, pathToCustomers)
        list = os.listdir(path)

        for file2 in list:
            pathToFile2 = os.path.join(path, file2)

            lines = []
            with open(pathToFile2, 'r') as file:
                for line in file:
                    line = line.strip()
                    lines.append(line)

            nameF = lines[1]
            surnameF = lines[4]

            if nameF == name and surnameF == surname:
                ID = lines[7]
                print("Found! ID: ", ID)

                Start()

        print("Nothing was found!")
        Start()
    if option == 3:
        ID = input("Input an ID of the account you want to delete: ")
        
        name, surname, _, balance, _ = IDtoCustomer(ID)
        
        pathToFile = os.path.dirname(os.path.abspath(__file__))
        pathToCustomerTXT = "Data/customers/" + ID + ".txt"
        path = os.path.join(pathToFile, pathToCustomerTXT)
        
        os.remove(path)
        
        print("Account was deleted!", ID)
        print("Name: ", name)
        print("Surname: ", surname)
        print("Balance: ", balance)
        
        Start()
    if option == 4:
        pathToFile = os.path.dirname(os.path.abspath(__file__))
        pathToTemplate = "Data/template.txt"
        path = os.path.join(pathToFile, pathToTemplate)
        
        pathToCustomer = "Data/customers/"
        path2 = os.path.join(pathToFile, pathToCustomer)
        
        shutil.copy2(path, path2)
        
        pathToCustomerTXT = "Data/customers/template.txt"
        pathToCoppiedTemplate = os.path.join(pathToFile, pathToCustomerTXT)
        
        NameList = os.listdir(path2)
        aNewName = ""
        ID = ""
        
        for missingFile in range(1, len(NameList) + 1):
            nameFile = str(missingFile).zfill(3) + ".txt"
            
            if not nameFile in NameList:
                aNewName = nameFile
                ID = str(missingFile).zfill(3)
        
        newCustomersPath = os.path.join(pathToFile, pathToCustomer + aNewName)
        
        os.rename(pathToCoppiedTemplate, newCustomersPath)
        
        print("New account was made!", aNewName)
        print("Please write these informations about new owner!")
        name = input("Name: ")
        surname = input("Surname: ")
        
        with open(newCustomersPath, "w") as file:
            text = "Name: \n" + name + "\n\nSurname: \n" + surname + "\n\nID: \n" + ID + "\n\nBalance: \n" + str(0)
            file.write(text)
        print("Succes!")
        
        Start()
        
def Verify():
    Username = input("Username: ")
    Password = input("Password: ")

    RUsername = False
    RPassword = False

    pathToFile = os.path.dirname(os.path.abspath(__file__))
    pathToStaffU = "Data/staff/name.txt"
    pathToStaffP = "Data/staff/password.txt"
    UsernamesPath = os.path.join(pathToFile, pathToStaffU)
    PasswordPath = os.path.join(pathToFile, pathToStaffP)

    linesUsername = []
    linesPassword = []

    with open(UsernamesPath, 'r') as file:
        for line in file:
            line = line.strip()
            linesUsername.append(line)

    with open(PasswordPath, 'r') as file:
        for line in file:
            line = line.strip()
            linesPassword.append(line)

    i = 0
    while i < len(linesPassword):
        if linesUsername[i] == Username:
            RUsername = True

        if linesPassword[i] == Password:
            RPassword = True

        i = i + 1

    if RUsername and RPassword:
        print("Login succesfull!")
        Start()
    else:
        print("Login unsuccesfull!")
        input("Press enter button to restart verification process.")
        Verify()

print("Welcome in", BankName, "! Please input your Username and Password.")
Verify()