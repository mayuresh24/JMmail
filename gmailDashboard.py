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
master=tk.Tk()


def send():
    
    msg=message_entry.get()
    rec=name_entry.get()
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login("mayureshdeshmukh101@gmail.com", "iamaddict123") 
    # message to be sent 
    #message = "Full App"
    # sending the mail 
    s.sendmail("mayureshdeshmukh101@gmail.com", rec, msg) 
    # terminating the session 
    s.quit()
    

    
name_label=tk.Label(master,text="Enter Recipeint EMail")
name_entry=tk.Entry(master)

message_label=tk.Label(master,text="Enter Message")
message_entry=tk.Entry(master)

sub_btn=tk.Button(master,text="SEND",command=send)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

message_label.grid(row=2,column=0)
message_entry.grid(row=2,column=1)

sub_btn.grid(row=4,column=1)
  
