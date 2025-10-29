import json
import random



while True:
    while True:
        userchoice = input("\n Press 1 to add the Task \n Press 2 to list  the All Task \n Press 3 to Update the Task \n press 4 to Delete the task\n Press 5 to exit the program smothly\n")
        if userchoice not in ["1","2","3","4" ,"5"]:
            print("please Enter the input that is mention above")
            continue
        else:
            break


    choice = int(userchoice)



    if choice == 1:
        try:
            with open('person.json' ,'r') as f:
                Task = json.load(f)
        except:
            Task = []
        print("please filled that field to Add a task\n")
        while True:
            title = input("please enter a title of Task\n").strip()
            if len(title) < 2:
                print("please enter complete title")
                continue
            else:
                break
        while True:
            descript= input("please give discription about it\n").strip()
            if len(title) < 2:
                print("please enter complete title")
                continue
            else:
                break
        while True:
            status = input("please Enter the status of Task\n").strip()
            if len(status) < 2:
                print("please enter complete value")
                continue
            else:
                break
        
        uniqueid = random.randint(500,10000)
       
        data = {
            "title" : title,
            "descript" : descript,
            "id" : uniqueid }
        data["status"] = "pending"
        Task.append(data)
        with open('person.json' , 'w') as f:
            json.dump(Task,f,indent=4)
            print("Task are added suceesfully")
   

    if choice == 2:
        try:
            with open('person.json' , 'r') as f:
                show = json.load(f)
            print(" your All Task are Listed below")
            for item in show:
                print(f'{item} \n')
        except FileNotFoundError:
            print("error are raised that file are empty or not found")
    if choice == 3:
        with open('person.json' , 'r') as f:
                Task = json.load(f)
        tar_id = input("\nplease enter a unique id of task that yu want to update\n")
        target = int(tar_id)
        found = False
        for user in Task:
            if user["id"] == target:
                print(f"current data {user}")
                user["title"] = input("\nplease enter the updated title\n") or user["title"]
                user["status"] = input("\nplease enter an updated Status\n") or user["status"]
                user["descript"] = input("\nplease enter an updated discription\n") or user["descript"]

                found = True
                break
        if found:
            with open("person.json" ,"w") as f:
                json.dump(Task, f, indent=4)
            print("The Task was updated sucessfully")
        else:
            print("user with that id not found")
    if choice == 4:
        with open('person.json' , 'r') as f:
                Task = json.load(f)
        tar = input("\nplease enter a unique id of task that yu want to Delete\n")
        target1 = int(tar)
        found = False
        for user in Task:
            if user["id"] == target1:
                Task.remove(user)
                found = True
                break
        if found:
             with open('person.json' ,'w') as f:
                json.dump(Task,f,indent=4)
                print("The Task was Deleted sucessfully")
        else:
            print("wrong id of task ... try again with correct one?")
    if choice == 5:
        print("bye")
        break
        
        
            


