import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import *
import sqlite3
import time


class AdminDashboard:
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

        assign_driver = tk.Button(self.root, text="Assign Drivers",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        assign_driver.place(x=60, y=260)

        def customer():
            from viewcustomer import ViewCustomer
            self.root.destroy()
            view = tk.Tk()
            ViewCustomer(view)

        view_customers = tk.Button(self.root, text="View Customers",command=customer,font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
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

        self.Logout= tk.Button(self.root, text="Logout",  font=("Verdana", 14),borderwidth=0,bg="#F9943B")
        self.Logout.place(x=56, y=590)

    # #Create Database
    #     self.conn = sqlite3.connect("crud3.db")
    #     self.cursor = self.conn.cursor()

    # # Create table if not exists
    #     self.cursor.execute('''CREATE TABLE IF NOT EXISTS adminDashboard
    #                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                         customer_name TEXT,pickup_address TEXT, dropoff_address TEXT, pickup_date TEXT, pickup_time TEXT, booing_status TEXT, assign_driver TEXT)''')
                            
    #     self.conn.commit()


#main page
        

        #treeview
        self.tree = ttk.Treeview(self.root, columns=("S.N","Customer Name","Pickup Address", "dropoff Address", "Pickup Date", "Pickup Time","Booking Status","Assign Driver"), show="headings",height=10)
        self.tree.heading("S.N", text="S.N")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Pickup Address", text="Pickup Address")
        self.tree.heading("dropoff Address", text="dropoff Address")
        self.tree.heading("Pickup Date", text="Pickup Date")
        self.tree.heading("Pickup Time", text="Pickup Time")
        self.tree.heading("Booking Status", text="Booking Status")
        self.tree.heading("Assign Driver", text="Assign Driver")
        
        
        
        self.tree.column("S.N", width=30)
        self.tree.column("Customer Name", width=92)
        self.tree.column("Pickup Address", width=90)  # Adjust the width as needed
        self.tree.column("dropoff Address", width=94)
        self.tree.column("Pickup Date", width=76)
        self.tree.column("Pickup Time", width=76)
        self.tree.column("Booking Status", width=88)
        self.tree.column("Assign Driver", width=80)
        self.tree.grid(row=8, columnspan=8, padx=285, pady=110)#here changed padx
        self.tree.tag_configure("Driver_Name", background="#E8E4E4")

        #Entry fields

        self.customer_name = tk.Label(self.root, text="Customer Name", font=("Verdana", 11),bg="#E8E4E4")
        self.customer_name.place(x=280,y=375)
        self.customer_name_entry = tk.Entry(self.root,width="35")
        self.customer_name_entry.place(x=410,y=375,height="30")
        
        self.pickup_date = tk.Label(self.root, text="Picup Date", font=("Verdana", 11),bg="#E8E4E4")
        self.pickup_date.place(x=640,y=375)
        self.pickup_date_entry = DateEntry(self.root, width=12, year=2019, month=6, day=22, background='gray', foreground='white', borderwidth=2)
        self.pickup_date_entry.place(x=740,y=375,height="30",width="150")

        self.pickup_address = tk.Label(self.root, text="Pickup Address", font=("Verdana", 11),bg="#E8E4E4")
        self.pickup_address.place(x=280,y=420)
        self.pickup_address_entry = tk.Entry(self.root,width="35")
        self.pickup_address_entry.place(x=410,y=420,height="30")

        self.pickup_time = tk.Label(self.root, text="Pickup Time", font=("Verdana", 11),bg="#E8E4E4")
        self.pickup_time.place(x=640,y=420)
        self.pickup_time_entry = tk.Entry(self.root,width="25")
        self.pickup_time_entry.place(x=740,y=420,height="30")

        self.dropoff_address = tk.Label(self.root, text="dropoff Address", font=("Verdana", 11),bg="#E8E4E4")
        self.dropoff_address.place(x=280,y=470)
        self.dropoff_address_entry = tk.Entry(self.root,width="35")
        self.dropoff_address_entry.place(x=410,y=470,height="30")

        self.booking_status = tk.Label(self.root, text="Booking Status", font=("Verdana", 11),bg="#E8E4E4")
        self.booking_status.place(x=640,y=470)
        self.booking_status_entry = tk.Entry(self.root,width="25")
        self.booking_status_entry.place(x=758,y=470,height="30")

        self.booking_status = tk.Label(self.root, text="Assign Driver", font=("Verdana", 11),bg="#E8E4E4")
        self.booking_status.place(x=280,y=520)
        self.booking_status_entry = tk.Entry(self.root,width="35")
        self.booking_status_entry.place(x=410,y=520,height="30")

    #BUTTONS
        self.cancel_booking= tk.Button(self.root,  text="Assign Driver",font=("Verdana", 10),width=13,bg="#F1B547",)
        self.cancel_booking.place(x=380, y=570)
        self.cancel_booking= tk.Button(self.root, text="Cancel Booking", font=("Verdana", 10),bg="#F1B547",)
        self.cancel_booking.place(x=510, y=570)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()