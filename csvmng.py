import os, csv
import pandas as pd

data = [
    ["service", "username", "password"]
]

if os.path.exists("Password Manager\\passwords.csv"):
    pass
else:
    with open("Password Manager\\passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def addpassword(newdt):
    with open("Password Manager\\passwords.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(newdt)

def viewpasswords():
    with open("Password Manager\\passwords.csv", "r")  as file:
        reader = csv.reader(file)
        next(reader)
        entries = []
        for rows in reader:
            entries.append(rows)
        return entries
    
def searchservices(ServiceKey):
    pwddata = pd.read_csv("Password Manager\\passwords.csv")
    ServiceKey = ServiceKey.lower()
    
    matches = pwddata[pwddata["service"].str.lower() == ServiceKey]
    
    if not matches.empty:
        return matches[["username", "password"]].values.tolist()
    else:
        return []



def deletepasswords():
    with open("Password Manager\\passwords.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        entries = [row for row in reader]

    for i, (serv, usernm, pwd) in enumerate(entries, start=1):
        print(f"{i}. Service: {serv}, Username: {usernm}, Password: {pwd}")

    try:
        DelChoice = int(input("Enter the number of the entry to delete: "))
        if 1 <= DelChoice <= len(entries):
            deleted = entries.pop(DelChoice - 1)
            print(f"Deleted entry: {deleted[0]} | {deleted[1]}")
        else:
            print("Invalid entry number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    with open("Password Manager\\passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["service", "username", "password"])
        writer.writerows(entries)

    print("Entry deleted successfully.")



