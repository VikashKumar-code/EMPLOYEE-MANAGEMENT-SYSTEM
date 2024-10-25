from customtkinter import *
from PIL import Image
from tkinter import messagebox

#login function
def login():
    if userentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("Error","All fields are required")
    elif userentry.get()=='admin' and passwordentry.get()=='Admin@12345':
        messagebox.showinfo("Success","Login is successful")
        root.destroy()
        import ems
    else:
        messagebox.showerror("Error","Login Failed")
    


root=CTk()
root.geometry("950x450+400+150")
root.resizable(0,0)
root.title("Employee Management System - Login Page")
Image=CTkImage(Image.open("D:\\Chandigarh university\\1st sem\\python\\project\\cover_login.jpg"),size=(950,450))
ImageLabel=CTkLabel(root,image=Image,text='')
ImageLabel.place(x=0,y=0)

#username input Box
userentry=CTkEntry(root,placeholder_text="Enter Username", width=220,corner_radius=10,font=('arial',14,'bold'))
userentry.place(x=570,y=150)

#password input Box
passwordentry=CTkEntry(root,placeholder_text="Enter Password", width=220,show="*",corner_radius=10,font=('arial',14,'bold'))
passwordentry.place(x=570,y=200)

#login Button
loginbtn=CTkButton(root,text="Submit",width=220,cursor="hand2",command=login,corner_radius=20,font=('arial',14,'bold'))
loginbtn.place(x=570,y=250)
root.mainloop()
