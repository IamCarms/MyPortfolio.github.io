from tkinter import *


root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list_box.insert(END, task)

def delete_Task():
    global task_list
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        list_box.delete(ANCHOR)
def open_task():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                list_box.insert(END, task)
    except:
        file = open("tasklist.txt", "w")
        file.close             
#icon
Image_icon=PhotoImage(file="task.png")
root.iconphoto(False, Image_icon)

#top bar 
TopImage=PhotoImage(file="topbar.png")
Label(root, image = TopImage).pack()

dock_image = PhotoImage(file = "dock.png")
Label(root, image = dock_image, bg = "#32405b").place(x = 30, y = 25)

note_image = PhotoImage(file = "task1.png")
Label(root, image = note_image, bg = "#32405b").place(x = 340, y = 20)
heading = Label(root, text = "Today Task", font = "Arial 20 bold", fg = "white", bg = "#32405b")
heading.place(x = 130, y = 20)

#main
frame = Frame(root, width = 400, height =  50, bg = "white")
frame.place(x = 0, y = 180)

task = StringVar()
task_entry = Entry(frame, width = 18, font = "Arial 20", bd = 0)
task_entry.place(x = 10, y = 7)
task_entry.focus()

button = Button(frame, text = "ADD", font = "Arial 20 bold", width = 6,fg = "white", bg = "#5a95ff", bd = 0, command=addTask)
button.place(x = 300, y = 0)

frame1 = Frame(root, bd = 3, width=700, height=280, bg = "#32405b")
frame1.pack(pady=(160, 0))

list_box = Listbox(frame1, font= ('Arial', 12), width = 40, height = 16, bg = "#32405b", fg = "white", cursor = "hand2", selectbackground="#5a95ff")
list_box.pack(side = LEFT, fill = BOTH, padx = 2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side = RIGHT, fill= BOTH) 

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

open_task()

#delete button 
del_icon = PhotoImage(file = "delete.png")
Button(root, image=del_icon, bd=0, command= delete_Task).pack(side=BOTTOM, pady = 13)
root.mainloop()