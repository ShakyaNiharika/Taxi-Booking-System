import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import*
import sqlite3
import globalvar
import time


class DriverHistory:
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

        self.his = Image.open('image/history.png')
        self.his= self.his.resize((20,20))
        self.his = ImageTk.PhotoImage(self.his)
        self.his_label = tk.Label(self.root, image=self.his,bg="#E8E4E4")
        self.his_label.place(x=30,y=335)

        self.history = tk.Button(self.root, text="History", font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.history.place(x=56, y=325)

        #profile image
        self.profile = Image.open('image/profile.png')
        self.profile= self.profile.resize((20,20))
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_label = tk.Label(self.root, image=self.profile,bg="#E8E4E4")
        self.profile_label.place(x=30,y=365)

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
            from log import TaxiBookingLogin
            log_out=tk.Tk()
            TaxiBookingLogin(log_out)

        self.Logout= tk.Button(self.root, text="Logout",command=logout , font=("Verdana", 14),borderwidth=0,bg="#F1B547")
        self.Logout.place(x=56, y=590)


    #Main Page
        #treeview
        self.tree = ttk.Treeview(self.root, columns=("ID","Pickup Address", "dropoff Address", "Date", "Time","Customer_id","Driver_id","Booking Status"), show="headings",height=10)
        self.tree.heading("Booking Status", text="Booking Status")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Pickup Address", text="Pickup Address")
        self.tree.heading("dropoff Address", text="dropoff Address")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Customer_id", text="Customer_id")
        self.tree.heading("Driver_id", text="Driver_id")
        
        self.tree.column("Booking Status", width=95)
        self.tree.column("ID", width=40)
        self.tree.column("Pickup Address", width=90)  # Adjust the width as needed
        self.tree.column("dropoff Address", width=94)
        self.tree.column("Date", width=50)
        self.tree.column("Time", width=50)
        self.tree.column("Customer_id", width=80)
        self.tree.column("Driver_id", width=80)

        

        # self.tree.grid(row=7, columnspan=4, padx=260, pady=150)
        self.tree.place(x=300,y=100,height=300,width = 600)
        self.tree.tag_configure("Driver_Name", background="#E8E4E4")

        #Joining the two tables
        #Database connection
        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT * FROM customerDashboard WHERE driverid=?''', (globalvar.driver[0],))
        # self.cursor.execute('''SELECT 
        #             customer.username,
        #             customer.Phone_Number,
        #             customer.Email_Address,
        #             customerDashboard.pickup_address,
        #             customerDashboard.dropoff_address,
        #             customerDashboard.pickup_date,
        #             customerDashboard.pickup_time
        #         FROM 
        #             customerDashboard
        #         JOIN 
        #             customer
        #         ON 
        #             customer.id = customerDashboard.customer_id''')
        records = self.cursor.fetchall()

        if records:
            for record in records:
                self.tree.insert("", "end", values=record)

        else:
                messagebox.showinfo("No Records", "No records found.")

        self.button=tk.Button(self.root,text="Ride Complete", bg="#F1B547",font=("Verdana", 10),command=self.complete)
        self.button.place(x=550,y=530,width=120,height=30) 

    def complete(self):
        selected_item = self.tree.selection()
        selected_id = self.tree.item(selected_item, "values")[0]

        if not selected_item:
            messagebox.showerror("Error", "Please select a record to complete the ride.")
            return
        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''UPDATE customerDashboard SET booking_status="completed" WHERE id=?''',( selected_id,))
        self.conn.commit()
        messagebox.showinfo("Success", "Ride Completed successfully!")
        self.root.destroy()
        new_root = tk.Tk()
        DriverHistory(new_root)
        new_root.mainloop()
    

        

         ##Button
        
    
    


if __name__ == "__main__":
    root = tk.Tk()
    app = DriverHistory(root)
    root.mainloop()