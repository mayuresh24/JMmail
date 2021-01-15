#pip install secure-smtplib
import smtplib
import tkinter as tk
import mysql.connector
import os
from tkinter import messagebox

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="zzz"
)

mycursor=mydb.cursor()
root=tk.Tk()

def login():
    global email
    global password
    email=name_entry.get()
    password=pass_entry.get()
    if(email=="mayureshdeshmukh101@gmail.com" and password=="iamaddict123"):
        global rcp
        global mesg
        top = tk.Toplevel(root)
        rcp=tk.Entry(top)
        mesg=tk.Entry(top)
        send=tk.Button(top,text="SEND",command=gd)
        rcp.pack()
        mesg.pack()
        send.pack()

def gd():
    r=rcp.get()
    m=mesg.get()
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(email,password) 
    # message to be sent 
    #message = "Full App"
    # sending the mail 
    s.sendmail(email,r,m) 
    # terminating the session 
    s.quit()

   
name_label=tk.Label(root,text="Enter Email")
name_entry=tk.Entry(root)

pass_label=tk.Label(root,text="Enter Password")
pass_entry=tk.Entry(root,show="*")

sub_btn=tk.Button(root,text="LOGIN",command=login)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

pass_label.grid(row=2,column=0)
pass_entry.grid(row=2,column=1)

sub_btn.grid(row=4,column=1)

root.mainloop()
