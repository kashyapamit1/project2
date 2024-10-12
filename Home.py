"""import sqlite3
import tkinter as tk
def rajni():
    CHECKIN=Entry_CHECKIN.get()
    CHECKOUT=Entry_CHECKOUT.get()
    DATEIN=Entry_DATEIN.get()
    DATEOUT=Entry_DATEOUT.get()
    purpose=Entry_purpose.get()
    connect=sqlite3.connect("Taj.db")
    cursor=connect.cursor()
    cursor.execute('''create table if not exists entry(CHECKIN text,CHECKOUT text,DATEIN integer,DATEOUT integer,PURPOSE text_notnull)''')
    cursor.execute('''insert into entry(CHECKIN ,CHECKOUT,DATEIN,DATEOUT,purpose)values(?,?,?,?,?)''',(CHECKIN,CHECKOUT,DATEIN,DATEOUT,purpose))
    connect.commit()
    connect.close()
    #TKINTER WINDOW
root=tk.Tk()
name=tk.Label(root,text="ENTERIES")
name.grid(row=0,column=1)
padx=500
pady=300
Label_checkin=tk.Label(root,text="CHECKIN")
Label_checkin.grid(row=1,column=0)
Entry_CHECKIN=tk.Entry(root)
Entry_CHECKIN.grid(row=1,column=2)
dot=tk.Label(root,text=":")
dot.grid(row=1,column=1)
Label_checkout=tk.Label(root,text="CHECKOUT")
Label_checkout.grid(row=2,column=0)
Entry_CHECKOUT=tk.Entry(root)
Entry_CHECKOUT.grid(row=2,column=2)
dot=tk.Label(root,text=":")
dot.grid(row=2,column=1)
Label_datein=tk.Label(root,text="DATEIN")
Label_datein.grid(row=3,column=0)
Entry_DATEIN=tk.Entry(root)
Entry_DATEIN.grid(row=3,column=2)
dot=tk.Label(root,text=":")
dot.grid(row=3,column=1)
dateout=tk.Label(root,text="DATEOUT")
dateout.grid(row=4,column=0)
Entry_DATEOUT=tk.Entry(root)
Entry_DATEOUT.grid(row=4,column=2)
dot=tk.Label(root,text=":")
dot.grid(row=4,column=1)
purpose=tk.Label(root,text="PURPOSE")
purpose.grid(row=5,column=0)
Entry_purpose=tk.Entry(root)
Entry_purpose.grid(row=5,column=2)
purpose=tk.Label(root,text=":")
purpose.grid(row=5,column=1)
name=tk.Button(root,text="SUBMIT BUTTON",command=rajni)
name.grid(row=6,column=2)
root.mainloop()"""



import os
import sqlite3
import tkinter as tk
def login():
    os.system('python3 Login.py')
def Signup():
    os.system('python3 Signup.py')

def amit():
    HOME=Entry_HOME.get()
    LOGIN=Entry_LOGIN.get()
    SIGNUP=Entry_SIGNUP.get()
    connect=sqlite3.connect("home.db")
    cursor=connect.cursor()
    cursor.execute('''create table if not exists signup(LOGIN text,SIGNUP text_notnull)''')
    connect.commit()
    connect.close()
#TKINTER WINDOW
root=tk.Tk()
root.geometry("300x200")
padx=10
pady=20
name=tk.Label(root,text="HOME")
name.grid(row=1,column=2,padx=50)
Entry_HOME=tk.Entry(root)
login=tk.Button(root,text="LOGIN",command=login)
login.grid(row=2,column=1,padx=6)
Entry_LOGIN=tk.Entry(root)
login=tk.Button(root,text="SIGNUP",command=Signup)
login.grid(row=2,column=3,padx=8)
Entry_SIGNUP=tk.Entry(root)
root.mainloop()



"""name=tk.Button(root,text="SUBMIT BUTTON",command=amit)
name.grid(row=3,column=2,pady=50)
root.mainloop()"""
