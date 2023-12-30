import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import *
import sqlite3
import time


class ViewCustomer:
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
        self.user_label = tk.Label(self.root, image=self.customer,bg="#E8E4E4")
        self.user_label.place(x=58,y=80)

        def assigndriver():
            from admindash import AdminDashboard
            self.root.destroy()
            assign_driver = tk.Tk()
            AdminDashboard(assign_driver)

        assign_driver = tk.Button(self.root, text="Assign Drivers",command=assigndriver,  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        assign_driver.place(x=60, y=260)

        view_customers = tk.Button(self.root, text="View Customers",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        view_customers.place(x=60, y=300)

        def driver():
            from viewdriver import ViewDriver
            self.root.destroy()
            view_driver = tk.Tk()
            ViewDriver(view_driver)

        billing = tk.Button(self.root, text="View Drivers",command=driver,  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        billing.place(x=60, y=340)

        payment = tk.Label(self.root, text="Payment",  font=("Verdana", 14),bg="#E8E4E4")
        payment.place(x=60, y=385)

        def logout():
            self.root.destroy()
            from adminlogin import AdminLogin
            logout=tk.Tk()
            AdminLogin(logout)

        self.Logout= tk.Button(self.root, text="Logout", command=logout, font=("Verdana", 14),borderwidth=0,bg="#F9943B")
        self.Logout.place(x=56, y=590)

    #main View profile
        #Search Bar
        customer_name = tk.Label(self.root, text="Customer Name",  font=("Verdana", 10),bg="#E8E4E4")
        customer_name.place(x=280, y=120)
        self.customer_name_entry = tk.Entry(self.root,width="35")
        self.customer_name_entry.place(x=400,y=110,height="30")
        self.search_button= tk.Button(self.root, text="Search",  font=("Verdana", 8),borderwidth=0,bg="#E8E4E4")
        self.search_button.place(x=630, y=110,height="30")

        background_frame=tk.Frame(self.root,bg="#E8E4E4")
        background_frame.place(x=275,y=162,relwidth=0.68, relheight=0.62)

    #treeview
        self.tree = ttk.Treeview(self.root, columns=("S.N","Customer Name","Address", "Phone Number", "Email Address", "Password","Method Of Payment"), show="headings",height=15)
        self.tree.heading("S.N", text="S.N")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Phone Number", text="Phone Number")
        self.tree.heading("Email Address", text="Email Address")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Method Of Payment", text="Method Of Payment")
        
        self.tree.column("S.N", width=30)
        self.tree.column("Customer Name", width=98)
        self.tree.column("Address", width=80)  # Adjust the width as needed
        self.tree.column("Phone Number", width=94)
        self.tree.column("Email Address", width=76)
        self.tree.column("Password", width=76)
        self.tree.column("Method Of Payment", width=125)
        self.tree.grid(row=7, columnspan=7, padx=305, pady=186)#here changed padx
        self.tree.tag_configure("Driver_Name", background="#E8E4E4")
        

        # customer_data = []
        # query = ''
        # conn = sqlite3.connect('crud5.db')



if __name__ == "__main__":
    root = tk.Tk()
    app = ViewCustomer(root)
    root.mainloop()