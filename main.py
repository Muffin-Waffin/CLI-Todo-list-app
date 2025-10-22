import json
import os
    
def login(username,password):
    with open('user.json','r') as infile:
        read = json.load(infile)
    if read[f'{username}'] == password:
        print("Login successful")
    else:
        print("User does not exist")  
def sign(username,password):
    data = {
        username:password
    }
    file = os.path.exists("user.json")
    if file == True:
        with open('user.json','r') as outfile:
            users = json.load(outfile)
        if username in users:
            print(f"{username} is already a user. Choose diffrent name")
            return
        
        users[username] = password
        with open('user.json','w') as outfile:
            json.dump(users, outfile, indent=4)
    
    else:
        with open('user.json','w') as outfile:
            json.dump(data, outfile, indent=4)

    with open(f'{username}.json','w') as u:
        json.dump([], u)
        print('User Created')
 
    # print(f"You have successfully made an account")
def Auth():
    print(f"1. Sign Up")
    print(f"2. Login")

    auth = int(input("What Would you like to do:"))
    if auth == 1:
        username = input("Username : ")
        password = input("Password : ")
        sign(username, password)
        Auth()

    else:
        username = input("Username : ")
        password = input("Password : ") 
        login(username, password)
    return username    
def addTasks(username):
    with open(f'{username}.json','r+') as f:
        tasks = json.load(f)
        title = " "
    # print("Current tasks!")
        while(title != ""):
            title = input("What Would you like to add :")
            if title != "":
                id = len(tasks) +1
                tasks.append({"Id":f"{id}","Title":f"{title}","status":False})
        # print(tasks)
        f.seek(0)
        json.dump(tasks, f,indent=4)
def displayTask():
    with open(f'{username}.json','r') as f:
        tasks = json.load(f)
        for task in tasks:
            print(f"{task["Id"]}.{task["Title"]}|| Status :{task["status"]}")
def deleteTask():
    displayTask()
    delete = int(input("Which task would you like to get deleted :"))

    # Step 1: Read file in read mode
    with open(f'{username}.json', 'r') as f:
        tasks = json.load(f)

    # Step 2: Modify list
    if 0 < delete <= len(tasks):
        tasks.pop(delete - 1)
    else:
        print("Invalid task number.")
        return
    
    for i, task in enumerate(tasks, start=1):
        task["Id"] = i

    # Step 3: Write updated list back to file
    with open(f'{username}.json', 'w') as f:
        json.dump(tasks, f, indent=4)
    print("\n\n\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("***********New Todo List -*****************")
    displayTask()
def completeTask():
    displayTask()
    with open(f"{username}.json", "r") as f:
        tasks = json.load(f)
        complete =input("Which task would you like to mark completed : ")
        for task in tasks:
            if task["Id"] == complete:
                task["status"] = "True"
    with open(f"{username}.json", "w") as ff:
        json.dump(tasks, ff, indent=4)
    print("\n\n\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("****** New list ****")
    displayTask()      
    
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Welcome to the cmd task manager") 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
username = Auth()
req = 0
while req != 5:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("What Would you like to do:\n 1) Add a Task \n 2) View Tasks \n 3) Delete Tasks \n 4) Mark Task Completed \n 5) exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    req = int(input(":"))
    if req == 1:
        print("*************************************************************")
        addTasks(username)
        print("*************************************************************")
    elif req == 2:
        print("___________________________________________________________")
        displayTask()
        print("___________________________________________________________")
    elif req == 3:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        deleteTask()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif req == 4:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        completeTask()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

