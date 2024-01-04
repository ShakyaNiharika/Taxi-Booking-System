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

        self.top = Image.open('image/carr.png')
        self.top= self.top.resize((60,50))
        self.top = ImageTk.PhotoImage(self.top)
        self.top_label = tk.Label(self.root, image=self.top,bg="#E8E4E4")
        self.top_label.place(x=700,y=10)
        self.name = tk.Label(text="",font=("Verdana", 16),bg="#E8E4E4")
        self.name.place(x=780,y=25)
        self.name.config(text=globalvar.driver[1])

        #image
        self.customer = Image.open('image/driverlogo.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        self.user_label = tk.Label(self.root, image=self.customer,bg="#E8E4E4")
        self.user_label.place(x=58,y=80)
        self.booking_id = tk.Entry()
        print(self.booking_id)

        #Time
        def update_time():
            self.current_time = time.strftime('%H:%M:%S')
            self.clock_label.config(text=self.current_time)
            self.root.after(1000, update_time) 

        self.clock_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.clock_label.place(x=75,y=230)
        # Start updating the time
        update_time()

        #dashboard image
        self.dash = Image.open('image/dash.png')
        self.dash= self.dash.resize((20,20))
        self.dash = ImageTk.PhotoImage(self.dash)
        self.dash_label = tk.Label(self.root, image=self.dash,bg="#E8E4E4")
        self.dash_label.place(x=30,y=285)

        self.dashboard = tk.Button(self.root, text="Dashboard",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.dashboard.place(x=56, y=280)

        self.his = Image.open('image/history.png')
        self.his= self.his.resize((20,20))
        self.his = ImageTk.PhotoImage(self.his)
        self.his_label = tk.Label(self.root, image=self.his,bg="#E8E4E4")
        self.his_label.place(x=30,y=335)

        def history():
            self.root.destroy()
            from driverhistory import DriverHistory
            his=tk.Tk()
            DriverHistory(his)

        self.history = tk.Button(self.root, text="History",command=history, font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.history.place(x=56, y=325)

        #profile image
        self.profile = Image.open('image/profile.png')
        self.profile= self.profile.resize((20,20))
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_label = tk.Label(self.root, image=self.profile,bg="#E8E4E4")
        self.profile_label.place(x=30,y=330)

        def myprofile():
            self.root.destroy()
            from drivermyprofile import DriverMyProfile
            profile=tk.Tk()
            DriverMyProfile(profile)

        self.my_profile = tk.Button(self.root, text="My Profile",command=myprofile, font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.my_profile.place(x=56, y=365)

        #password image
        self.sidelock = Image.open('image/sidelock.png')
        self.sidelock= self.sidelock.resize((20,20))
        self.sidelock = ImageTk.PhotoImage(self.sidelock)
        self.sidelock_label = tk.Label(self.root, image=self.sidelock,bg="#E8E4E4")
        self.sidelock_label.place(x=30,y=415)

        def change_password():
            self.root.destroy()
            from driverchangepassword import DriverChangePassword
            change_pass=tk.Tk()
            DriverChangePassword(change_pass)

        self.change_password = tk.Button(self.root, text="Change Password", command=change_password,font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.change_password.place(x=56, y=410)

        def logout():
            self.root.destroy()
            from driverlogin import Driverlogin
            log_out=tk.Tk()
            Driverlogin(log_out)

        self.Logout= tk.Button(self.root, text="Logout",command=logout , font=("Verdana", 14),borderwidth=0,bg="#F1B547")
        self.Logout.place(x=56, y=590)

#Main page
        self.frame4=tk.Frame(self.root,bg="#E8E4E4")
        self.frame4.place(x=295,y=120,relwidth=0.65, relheight=0.35)

        self.head = tk.Label(self.root,text="Assigned Customer" ,bg="#F1B547",borderwidth=4)
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
        
        self.second_head = tk.Label(self.root,text="Current Ride" ,bg="#F1B547",borderwidth=4)
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
        self.pickup_date_entry = DateEntry(self.root, width=12, year=2019, month=6, day=22, background='gray', foreground='white', borderwidth=2)
        self.pickup_date_entry.place(x=730, y=420, height=30, width=150)

        self.pickup_time = tk.Label(self.root, text="Pickup Time", font=("Verdana", 10))
        self.pickup_time.place(x=620,y=480)
        self.pickup_time_entry = tk.Entry(self.root,width="45")
        self.pickup_time_entry.place(x=730,y=480,height="30",width="150")

        ##Button
        button=tk.Button(self.root,text="Ride Complete", bg="#F1B547",font=("Verdana", 10))
        button.place(x=550,y=530,width=120,height=30) 

       

        # self.cursor.execute('''SELECT id, pickup_address, dropoff_address, pickup_date, pickup_time FROM customerdashboard where customer_id = ?''')
        # records = self.cursor.fetchall()

        # if records:
        #     for record in records:
        #         self.tree.insert("", "end", values=record)

        # else:
        #         messagebox.showinfo("No Records", "No records found.")




if __name__ == "__main__":
    root = tk.Tk()
    app = DriverDashboard(root)
    root.mainloop()