import tkinter as tk




import os

main_screen = tk.Tk()
main_screen.geometry('400x600')
main_screen.title('TO-DO LIST')
main_screen.resizable(False,False)

task_list=[]

    
def addTask():
    task=task_entry.get()
    task_entry.delete(0,tk.END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(tk.END, task)

def deleteTask():
    global task_list
    task=str(listbox.get(tk.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(f"\n{task}") 
        listbox.delete(tk.ANCHOR)
    
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks= taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
            listbox.insert(tk.END , task)
    except:
        file=open("tasklist.txt",'w')
        file.close()


#application icon
application_icon = tk.PhotoImage(file="icons/to-do-list.png")
main_screen.iconphoto(False,application_icon )

# tool bar
Top_image= tk.PhotoImage(file="icons/topbar.png")
tk.Label(main_screen, image=Top_image).pack()

menu_image= tk.PhotoImage(file="icons/menu.png")
# menu_image = menu_image.subsample(15)
tk.Label(main_screen, image=menu_image,bg="#32405b").place(x=25,y=20)

notes_image= tk.PhotoImage(file="icons/to-do-list.png")
# notes_image = notes_image.subsample(15)
tk.Label(main_screen, image=notes_image,bg="#32405b").place(x=325,y=20)

handing=tk.Label(main_screen,text="ALL TASKS",font="arial 24 bold",fg="white",bg="#32405b")
handing.place(x=130,y=20)

# main body

task_fream = tk.Frame(main_screen,width=400,height=50,bg="white")
task_fream.place(x=0,y=180)
task=tk.StringVar()
task_entry= tk.Entry(task_fream,width=18,font="arial 28",bd=0)
task_entry.place(x=0,y=4)
task_button= tk.Button(task_fream,text="ADD",font="arial 20 bold",width=6,height=2,bg="#82CC6C",fg="black",highlightbackground="#82CC6C",highlightthickness=1,borderwidth=0.8, relief="groove",bd=0,padx=0,pady=0,command=addTask)

task_button.place(x=300,y=0)

# Listbox

list_fream = tk.Frame(main_screen,width=700,height=280,bg="#32405b")
list_fream.pack(pady=(160,0))
listbox= tk.Listbox(list_fream,font="arial 12 bold",fg="white",width=50,height=18,bg="#32405b")
listbox.pack(side="left",fill="both",padx=2)
scrolbar=tk.Scrollbar(list_fream)
scrolbar.pack(side="right",fill="both")
listbox.config(yscrollcommand=scrolbar.set)
scrolbar.config(command=listbox.yview)

openTaskFile()

# delete

delete_icon=tk.PhotoImage(file="icons/delete.png")
# delete_icon = delete_icon.subsample(12)
tk.Button(main_screen,image=delete_icon,bd=0,command=deleteTask).pack(side="bottom",pady=12)






main_screen.mainloop()