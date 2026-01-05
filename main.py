from csvmng import addpassword, viewpasswords, searchservices, deletepasswords
def AddEntry():
    ServiceName = input("What service are you adding? ")
    UserName = input("Username: ")
    Password = input("Password: ")
    newdt = [[ServiceName, UserName, Password]]
    if not ServiceName or not UserName or not Password:
        print("All fields must be filled.")
        return

    addpassword(newdt)

def ViewPasswords():
    vpwd = viewpasswords()
    for serv, usernm, pwd in vpwd:
        print("------------------------")
        print(f"Service: {serv}")
        print(f"Username: {usernm}")
        print(f"Password: {pwd}")
        print("------------------------")
    

def SearchbyServ():
    ServiceKey = input("Service Name? ")
    results = searchservices(ServiceKey)
    if results:
        for usrnm, pwd in results:
            print("------------------------")
            print(f"Service: {ServiceKey}")
            print(f"Username: {usrnm}")
            print(f"Password: {pwd}")
            print("------------------------")
    else:
        print(f"No Service {ServiceKey} Found")

def DeletePassword():
    try:
        deletepasswords()
    except Exception as e:
        print("Invalid Input, Try Again")

def main():
    while True:
        print("----Password Manager----")
        print("1. Add Entry")
        print("2. View All")
        print("3. Search by Service")
        print("4. Delete Entry")
        print("5. Exit")
        
        try:
            UserChoice = int(input("What do you want to do? "))
        except ValueError:
            print("Enter a Valid Number")
            continue

        if UserChoice == 1:
            AddEntry()
        elif UserChoice == 2:
            ViewPasswords()
        elif UserChoice == 3:
            SearchbyServ()
        elif UserChoice == 4:
            DeletePassword()
        elif UserChoice == 5:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()






