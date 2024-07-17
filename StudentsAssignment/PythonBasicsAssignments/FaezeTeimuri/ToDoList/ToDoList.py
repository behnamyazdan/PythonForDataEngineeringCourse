
import csv
import pandas as pd

to_do_list = []
Done_List = []

file = open("to_do_list.csv", "r")
to_do_list = [row[1] for row in list(csv.reader(file, delimiter=","))]

print(to_do_list)

to_do_list.remove("0")
file.close()

file = open("Done_list.csv", "r")
Done_List = [row[1] for row in list(csv.reader(file, delimiter=","))]

print(Done_List)

Done_List.remove("0")
file.close()

print("1. Add Tasks")
print("2. View Tasks")
print("3. Mark Tasks as Done")
print("4. Delete Tasks")
print("5. Save and Load Tasks")

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        to_do_list.append(input("Please enter a new task:"))

        print("All of My Tasks:", to_do_list)
        print("My Done Tasks:", Done_List)
    elif choice == "2":
        print("All of My Tasks:", to_do_list)
        print("My Done Tasks:", Done_List)
    elif choice == "3":
        print(to_do_list)
        Done_task = input("Which Task is Done? Please Enter a index:")
        Done_List.append(to_do_list[int(Done_task)])
        print("All of My Tasks:",to_do_list)
        print("My Done Tasks:",Done_List)
    elif choice == "4":
        Remove_Task = input("Which Task Do you want to remove? Please Enter a index:")
        print("You Remove:", to_do_list[int(Remove_Task)])
        del to_do_list[int(Remove_Task)]
        print("All of My Tasks:", to_do_list)
        print("My Done Tasks:", Done_List)
    elif choice == "5":
        df = pd.DataFrame(to_do_list)
        df1 = pd.DataFrame(Done_List)
        df.to_csv("to_do_list.csv")
        df1.to_csv("Done_list.csv")
        print("All of My Tasks:", to_do_list)
        print("My Done Tasks:", Done_List)
        print("Files Successfully saved!")


