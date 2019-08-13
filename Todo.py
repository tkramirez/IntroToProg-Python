#Title: Assignment05; Lists and Dictionaries
#Dev: TKRamirez
#Date: August 12th, 2019
#ChangeLog: I don't believe I actually used any of his code, but I did look at RRoot, 11/02/2016, Created starting template and possibly used some ideas from it.

task_list = []
def add_task(task_name, priority):
    dicRow1 = {'Task': task_name, 'Priority': priority}
    #print(dicRow1)
    task_list.append(dicRow1)
def save_data():
    save_list = []
    for item in task_list:
        save_list.append(item['Task'] + ',' + item['Priority'])
    save_string = '\n'.join(save_list)
    fob = open("Todo.txt", "w")
    fob.write(save_string)
    fob.close()
    print("Data Saved Successfully!")

fob = open("Todo.txt", "r")
fob_lines = fob.read()
#print(fob_lines)
fob_list = fob_lines.split("\n")
#print(fob_list)

for task in fob_list:
    (task_name, priority) = task.split(",")
    #print(task_name)
    #print(priority)
    add_task(task_name, priority)

print(task_list)

#display menu:
menu_choice = '0'
while menu_choice != '5':
    print("____________________\n")
    print("\t\tMenu:\n")
    print("1. Show current data. ")
    print("2. Add a new item. ")
    print("3. Remove an existing item.")
    print("4. Save Data to a file.")
    print("5. Exit Program.")
    print("____________________\n")
    menu_choice = input("Pick an item from the Menu: \n")
    #menu_choice = menu_choice.strip()
    if menu_choice == '1':
        print("Your task list is: \n")
        print(task_list)
    elif menu_choice == '2':
        new_task = input("Please input a new Task: \n")
        new_priority = input(f"Please input {new_task} priority\n")
        add_task(new_task, new_priority)
    elif menu_choice == '3':
        remove_option = input('Which item would you like to remove: \n')
        #loop through all the items in task list, and number them in index
        for idx, task_dict in enumerate (task_list):
            if remove_option == task_dict['Task']:
                task_list.pop(idx)
                print(f"You have sucessfully removed {remove_option}. Your list is now {task_list}\n")
                #put in a you removed so and so successfully
                break
        else:
            print(f'{remove_option} is not on your list. Try again if you would like to remove something')
    elif menu_choice == '4':
        save_data()
save_data()








'''
exit()dicRow1 = {fob.readline(1)}
dicRow2 = {fob.readline(2)}

print(dicRow1)
print(dicRow2)

#dicRow1 = {'Task': 'Clean House', 'Priority': 'Low',}
#dicRow2 = {'Task': 'Pay Bills', 'Priority': 'High'}
lstTable = [dicRow1, dicRow2]
print(lstTable)



for line in fob:
    dicRow1.append("Clean House,low")
for line in fob:
    dicRow2.append("Pay Bills,high")
print(dicRow1, dicRow2)

for item in fob:
    dicRow1.append(fob(1))
for item in fob:
    dicRow2.append(fob(2))

mylist = []
for line in fob:
    mylist.append("Clean House,low \nPay Bills,high")
print(mylist)

fob = open("Todo.txt", "w")
fob.write()
print(lstTable)

'''