import csv

def add():
    f = open("Data.csv","a",newline="")
    catagory = input("Enter Expense Label: ")
    amt = float(input("Expense / Amount: "))
    w = csv.writer(f)
    w.writerow([catagory, amt])
    f.close()

def view():
    f = open("Data.csv","r")
    r = csv.reader(f)
    for i in r:
        print(i)
    f.close()

def total():
    f = open("Data.csv","r")
    r = csv.reader(f)
    next(r)
    total = 0.0
    for i in r:
        total+=float(i[1])
    print(f"Your total is {total}.")
    f.close()

def update():
    f = open("Data.csv","r+",newline='')
    f.seek(0)
    l=[]
    r = csv.reader(f)
    w = csv.writer(f)
    ctg = input("Enter the catagory you want to update: ")
    g = list(r)
    l+=[g[0]]
    for i in g[1:]:
        if i[0]==ctg:
            amt = float(input("Update your amount: "))
            i[1]=str(amt)
        l+=[i]
    f.seek(0)
    w.writerows(l)
    print("Updated.")
    f.close()

def delete():
    f = open("Data.csv","r")
    ctg = input("Enter catagory you want to delete: ")
    f.seek(0)
    r = csv.reader(f)
    g = list(r)
    for i in g[1:].copy():
        if i[0]==ctg:
            g.remove(i)
    f.close()
    f = open("Data.csv","w",newline='')
    w = csv.writer(f)
    w.writerows(g)
    print("Deleted.")
    f.close()
    
print("""Welcome to Expense Tracker!
This program will help you track your expenses and generate a summary report.

Here are some available commands:
    1. Add Expense: Add a new expense to the tracker with a label, amount, and date.
    2. View Expenses: View all recorded expenses in a tabular format.
    3. Total Expenses: Calculate and display the total amount of expenses recorded.
    4. Update Expense: Update an existing expense by specifying its label and new details.
    5. Delete Expense: Remove an expense from the tracker by specifying its label.
    6. Exit: Exit the program.
""")

while True:
    choice = int(input("Enter your choice (1-6): "))
    if choice==1:
        add()
    elif choice==2:
        view()
    elif choice==3:
        total()
    elif choice==4:
        update()
    elif choice==5:
        delete()
    elif choice==6:
        print("Thank You!")
        print("------------------------------------------------------------------")
        break
    print("------------------------------------------------------------------")

