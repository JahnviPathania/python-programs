tasks=[]
def load_tasks():
    try:
        with open("tasks.txt","r") as file:
            for l in file:
                name,status=l.strip().split("||")
                tasks.append({"name":name,"completed":status=="True"})
    except FileNotFoundError:
        pass
def save_tasks():
    with open("tasks.txt","w") as file:
        for t in tasks:
            file.write(f"{t['name']}||{t['completed']}\n")
def view_task():
    if not tasks:
        print("no tasks")
    else:
        for i, t in enumerate(tasks,start=1):
             status = "✅" if t["completed"] else "❌"
             print(f"{i}. {t['name']} [{status}]")


def add_task():
    while True:
        x=input("enter a task(if done with adding task just write done):  ")
        if x.lower()=="done":
            break
        tasks.append({"name": x, "completed": False})
        save_tasks()
        print(f"Task added: {x}")
        view_task()

def mark_complete():
    view_task()
    try:
        if not tasks:
            break
        else:
            index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks()
            print(f"Marked '{tasks[index]['name']}' as completed ✅")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

    
def delete_task():
    view_task()
    x = input("Enter the exact task name to delete: ")
    for task in tasks:
        if task["name"] == x:
            tasks.remove(task)
            save_tasks()
            print(f"Task '{x}' removed.")
            return
    print("Task does not exist.")
while True:    
    print("menu")
    print("view")
    print("add")
    print("delete")
    print("complete")
    print("exit")
    choose=input("enter what you want to do from above : ")
    if(choose=="view"):
        view_task()
    elif(choose=="add"):
        add_task()
    elif(choose=="complete"):
        mark_complete()
    elif (choose=="delete"):
        delete_task()
    elif choose=="exit":
        print("exiting")
        break
    else:
        print("not valid function please choose from the menu")


    