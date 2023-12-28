import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import *
import sqlite3
import time

class AdminHistory:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('Registration form')

        self.create_widgets()
    
    def create_widgets(self):
        frame1=tk.Frame(self.root,bg="#E8E4E4")
        frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        head = tk.Label(self.root, text="Admin Dashboard", font=("Verdana", 18),bg="#E8E4E4")
        head.place(x=40,y=20)

        frame2=tk.Frame(self.root,bg="#E8E4E4")
        frame2.place(x=0,y=72,relwidth=0.26, relheight=1)

        frame3=tk.Frame(self.root,bg="#F9943B")
        frame3.place(x=0,y=590,relwidth=0.26, relheight=0.35)

        self.customer = Image.open('image/admin.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        user_label = tk.Label(self.root, image=self.customer,bg="#E8E4E4")
        user_label.place(x=58,y=80)

        home = tk.Label(self.root, text="Assign Drivers",  font=("Verdana", 14),bg="#E8E4E4")
        home.place(x=60, y=260)

        add_customers = tk.Label(self.root, text="Add Customers",  font=("Verdana", 14),bg="#E8E4E4")
        add_customers.place(x=60, y=295)

        billing = tk.Label(self.root, text="Billing History",  font=("Verdana", 14),bg="#E8E4E4")
        billing.place(x=60, y=340)

        payment = tk.Label(self.root, text="Payment",  font=("Verdana", 14),bg="#E8E4E4")
        payment.place(x=60, y=385)

        self.Logout= tk.Button(self.root, text="Logout",  font=("Verdana", 14),borderwidth=0,bg="#F9943B")
        self.Logout.place(x=56, y=590)


#main history part
        #treeview
        self.tree = ttk.Treeview(root, columns=("Driver Name", "Phone Number", "Email Address", "Pickup Address","Dropoff Address","Time","Date","Customer Nmae","Phone Number"), show="headings",height=15)
        self.tree.heading("Driver Name", text="Driver_Name")
        self.tree.heading("Phone Number", text="Phone Number")
        self.tree.heading("Email Address", text="Email Address")
        self.tree.heading("Pickup Address", text="Pickup Address")
        self.tree.heading("Dropoff Address", text="Dropoff Address")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Date", text="Date")
        self.tree.column("Driver Name", width=80)  
        self.tree.column("Phone Number", width=90)
        self.tree.column("Email Address", width=90)
        self.tree.column("Pickup Address", width=90)
        self.tree.column("Dropoff Address", width=90)
        self.tree.column("Time", width=60)
        self.tree.column("Date", width=60)
        self.tree.grid(row=7, columnspan=4, padx=320, pady=150)
        self.tree.tag_configure("Driver_Name", background="#E8E4E4")


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminHistory(root)
    root.mainloop()