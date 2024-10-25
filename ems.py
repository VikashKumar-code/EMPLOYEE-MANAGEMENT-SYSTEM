from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database

#functions

def deleteall_employee():
    result=messagebox.askokcancel('Question','Are you sure to delete all the records ?')
    if result:
        database.deleteall()
        treeview_data()

def showall_employee():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Please Enter Value to Search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option to search')
    else:
        search_result=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        if len(search_result)==0:
            messagebox.showerror('Error','No Data Found')
        else:
            for emp in search_result:
                tree.insert('',END,values=emp)
            

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Please select any data to delete')
    else:
        database.delete(identry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is deleted successfully.')

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Please select any data to Update')
    else:
        database.update(identry.get(),nameentry.get(),phoneentry.get(),roleBox.get(),genderBox.get(),salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is updated successfully.')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        identry.insert(0,row[0])
        nameentry.insert(0,row[1])
        phoneentry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryentry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)
    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryentry.delete(0,END)


def treeview_data():
    employees=database.fetchemployees()
    tree.delete(*tree.get_children())
    if len(employees)==0:
        tree.insert('',END,values='No records found')
    else:
        for emp in employees:
            tree.insert('',END,values=emp)

def add_employee():
    if identry.get()=='' or nameentry.get()=='' or phoneentry.get()=='' or salaryentry.get()=='':
        messagebox.showerror('Error','All Fields are required')

    elif database.id_exists(identry.get()):
        messagebox.showerror('Error','ID already Exists')
    elif identry.get().startswith('EMP')==False:
        messagebox.showerror('Error',"Invalid ID Format. Use 'EMP' followed by a number (e.g. 'EMP1')")
    elif phoneentry.get().isdigit()==False:
        messagebox.showerror('Error',"Invalid Phone Number")
    elif len(phoneentry.get())>10 or len(phoneentry.get())<10:
        messagebox.showerror('Error',"Invalid Phone Number")
    elif salaryentry.get().isdigit()==False:
        messagebox.showerror('Error',"Invalid Salary")
    else:
        database.insert(identry.get(),nameentry.get(),phoneentry.get(),roleBox.get(),genderBox.get(),salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is inserted Successfully')

window=CTk()
window.title("Employees Management System")
window.geometry('1020x590+400+150')
window.resizable(0,0)
window.configure(fg_color='#161C30')
logo=CTkImage(Image.open("D:\\Chandigarh university\\1st sem\\python\\project\\logo.jpg"),size=(930,151))
logo_label=CTkLabel(window,image=logo,text="")
logo_label.grid(row=0,column=0,columnspan=2)

leftframe=CTkFrame(window,fg_color='#161C30')
leftframe.grid(row=1,column=0)

idlabel=CTkLabel(leftframe,text='ID', font=('arial',18,'bold'),)
idlabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

identry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
identry.grid(row=0,column=1)

namelabel=CTkLabel(leftframe,text='Name', font=('arial',18,'bold'))
namelabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameentry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
nameentry.grid(row=1,column=1)

phonelabel=CTkLabel(leftframe,text='Phone', font=('arial',18,'bold'))
phonelabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneentry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
phoneentry.grid(row=2,column=1)

rolelabel=CTkLabel(leftframe,text='Role', font=('arial',18,'bold'))
rolelabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Web developer','Data Scientist','UI/UX Designer','Java Developer','Python Developer']
roleBox=CTkComboBox(leftframe,values=role_options,font=('arial',15,'bold'),width=180,state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderlabel=CTkLabel(leftframe,text='Gender', font=('arial',18,'bold'))
genderlabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female']
genderBox=CTkComboBox(leftframe,values=gender_options,font=('arial',15,'bold'),width=180,state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

salarylabel=CTkLabel(leftframe,text='Salary', font=('arial',18,'bold'))
salarylabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryentry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
salaryentry.grid(row=5,column=1)

rightframe=CTkFrame(window)
rightframe.grid(row=1,column=1,padx='20')

search_options=['ID','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightframe,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightframe,font=('arial',13,'bold'))
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text='Search',width=100,cursor="hand2",command=search_employee,font=('arial',14,'bold'))
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightframe,text='Show All',width=100,cursor="hand2",command=showall_employee,font=('arial',14,'bold'))
showallButton.grid(row=0,column=3,pady=5)


tree=ttk.Treeview(rightframe,height=16)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=['ID','Name','Phone','Role','Gender','Salary']
tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')
tree.config(show='headings')
tree.column('ID',width='100',anchor=CENTER)
tree.column('Name',width='160',anchor=CENTER)
tree.column('Phone',width='160',anchor=CENTER)
tree.column('Gender',width='100',anchor=CENTER)
tree.column('Role',width='200',anchor=CENTER)
tree.column('Salary',width='140',anchor=CENTER)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowheight=25,background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightframe,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',width=180,font=('arial',15,'bold'),cursor='hand2',corner_radius=10,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',width=180,font=('arial',15,'bold'),cursor='hand2',corner_radius=10,command=add_employee)
addButton.grid(row=0,column=1,padx=5,pady=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',width=180,font=('arial',15,'bold'),cursor='hand2',corner_radius=10,command=update_employee)
updateButton.grid(row=0,column=2,padx=5,pady=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',width=180,font=('arial',15,'bold'),cursor='hand2',corner_radius=10,command=delete_employee)
deleteButton.grid(row=0,column=3,padx=5,pady=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',width=180,font=('arial',15,'bold'),cursor='hand2',corner_radius=10,command=deleteall_employee)
deleteallButton.grid(row=0,column=4,padx=5,pady=5)

treeview_data()

window.bind('<ButtonRelease>',selection)
window.mainloop()