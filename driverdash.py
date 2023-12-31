import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import*
import sqlite3
import globalvar

import time

class DriverDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('Cus Dashboard')

        self.create_widgets()
    
    def create_widgets(self):
        self.frame1=tk.Frame(self.root,bg="#E8E4E4")
        self.frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        self.head = tk.Label(self.root, text="Welcome To Taxi Boking System", font=("Verdana", 18),bg="#E8E4E4")
        self.head.place(x=20,y=20)

        self.frame2=tk.Frame(self.root,bg="#E8E4E4")
        self.frame2.place(x=0,y=75,relwidth=0.26, relheight=1)

        self.frame3=tk.Frame(self.root,bg="#F1B547")
        self.frame3.place(x=0,y=590,relwidth=0.26, relheight=0.35)


#Main page
        self.frame4=tk.Frame(self.root,bg="#E8E4E4")
        self.frame4.place(x=295,y=120,relwidth=0.65, relheight=0.35)

        self.head = tk.Label(self.root,text="Assigned Customer" ,bg="#F1B547")
        self.head.place(x=320,y=140)
        
        self.name = tk.Label(self.root,text="Customer Name",font=("Verdana", 10))
        self.name.place(x=320,y=190)
        self.name_entry = tk.Entry(self.root,width="35")
        self.name_entry.place(x=430,y=180,height="30")

        self.email = tk.Label(self.root,text="Email Address",font=("Verdana", 10))
        self.email.place(x=320,y=240)
        self.email_entry = tk.Entry(self.root,width="35")
        self.email_entry.place(x=430,y=230,height="30")

        self.phone = tk.Label(self.root,text="Phone Number",font=("Verdana", 10))
        self.phone.place(x=320,y=280)
        self.phone_entry = tk.Entry(self.root,width="35")
        self.phone_entry.place(x=430,y=280,height="30")

        self.frame5=tk.Frame(self.root,bg="#E8E4E4")
        self.frame5.place(x=295,y=360,relwidth=0.65, relheight=0.35)
        
        self.second_head = tk.Label(self.root,text="Current Ride" ,bg="#F1B547")
        self.second_head.place(x=320,y=380)

        self.pickup_address = tk.Label(self.root, text="Pickup Address", font=("Verdana", 10))
        self.pickup_address.place(x=320,y=430)
        self.pickup_address_entry = tk.Entry(self.root,width="45")
        self.pickup_address_entry.place(x=440,y=420,height="30",width="150")

        self.dropoff_address = tk.Label(self.root, text="Drop off Address", font=("Verdana", 10))
        self.dropoff_address.place(x=320,y=480)
        self.dropoff_address_entry = tk.Entry(self.root,width="45")
        self.dropoff_address_entry.place(x=440,y=480,height="30",width="150")

        self.pickup_date = tk.Label(self.root, text="Pickup Date", font=("Verdana", 10))
        self.pickup_date.place(x=620,y=430)
        self.pickup_date_entry = tk.Entry(self.root,width="45")
        self.pickup_date_entry.place(x=730,y=420,height="30",width="150")

        self.pickup_time = tk.Label(self.root, text="Pickup Time", font=("Verdana", 10))
        self.pickup_time.place(x=620,y=480)
        self.pickup_time_entry = tk.Entry(self.root,width="45")
        self.pickup_time_entry.place(x=730,y=480,height="30",width="150")

        ##Button
        button=tk.Button(self.root,text="Ride Complete", bg="#E8E4E4",font=("Verdana", 10))
        button.place(x=550,y=530,width=120,height=30) 

        # self.Booking_status = tk.Label(self.root, text="Booking Status", font=("Verdana", 11),bg="#E8E4E4")
        # self.Booking_status.place(x=280,y=440)
        # self.Booking_status_entry = tk.Entry(self.root,width="35")
        # self.Booking_status_entry.place(x=410,y=440,height="30")




if __name__ == "__main__":
    root = tk.Tk()
    app = DriverDashboard(root)
    root.mainloop()