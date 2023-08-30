from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("500x500")
root.title("Login")

name=Label(root, text="Name:")
name.place(relx=0.04, rely=0.15)
entry_name = Entry(root)
entry_name.place(relx=0.25, rely=0.15,anchor=CENTER)

password=Label(root, text="Password:")
password.place(relx=0.06, rely=0.45, anchor=CENTER)
entry_password = Entry(root)
entry_password.place(relx=0.25, rely=0.45,anchor=CENTER)

captcha=Label(root,text="Captcha: ")
captcha.place(relx=0.07, rely=0.75, anchor=CENTER)
entry_captcha = Entry(root)
entry_captcha.place(relx=0.25, rely=0.75,anchor=CENTER)

class userDB():
    def __init__(self):
        self.username = "James"
        self._password = 265638
        self._captcha = "37j"
        
    def showUser():
        label_show_name["text"] = "Name : "+self.username
        label_show_password["text"] = "Password : "+self.password
        label_show_captcha["text"] = "Captcha : "+self.captcha
   
    def addUser():
        global userDB 
        name.username = entry_name.get()
        password._password = entry_password.get()
        captcha._captcha = captcha_captcha.get()
        print("Detaails Updated")
        

ULD= Button(root, text="Update Login Details", command=addUser())
ULD.place(relx=0.10, rely=0.25, anchor=CENTER)
show=Button(root, text="Show Profile", command=showUser())
show.place(relx=0.12, rely=0.25, anchor=CENTER)    
root.mainloop()