import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import*
import sqlite3
import globalvar
import time

class DriverChangePassword:
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
        # self.name.config(text=globalvar.driver[1])

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

        self.history = tk.Button(self.root, text="History", font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.history.place(x=56, y=325)

        #profile image
        self.profile = Image.open('image/profile.png')
        self.profile= self.profile.resize((20,20))
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_label = tk.Label(self.root, image=self.profile,bg="#E8E4E4")
        self.profile_label.place(x=30,y=330)

        self.my_profile = tk.Button(self.root, text="My Profile", font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
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

    #Connect Database
        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()

    ##main page (CHANGE PASSWORD)***
        background_frame=tk.Frame(self.root,bg="#E8E4E4")
        background_frame.place(x=300,y=172,relwidth=0.62, relheight=0.52)

        self.tittle = tk.Label(self.root,text="Change Password:",font=("Verdana", 15),bg="white")
        self.tittle.place(x=360,y=120)

        self.old_password = tk.Label(self.root,text="Old Password:", font=90,bg="#E8E4E4")
        self.old_password.place(x=350,y=220)
        self.old_password_entry=tk.Entry(self.root)
        self.old_password_entry.place(x=350,y=250,height=30, width=280,)

        self.new_password = tk.Label(self.root,text="New Password:", font=90,bg="#E8E4E4")
        self.new_password.place(x=350,y=310)
        self.new_password_entry=tk.Entry(self.root)
        self.new_password_entry.place(x=350,y=340,height=30, width=280,)

        #QUERY for updating the password
        def change():
            check=globalvar.driver[2]
            driver_id = globalvar.driver[0]
           
            password=self.old_password_entry.get()

            self.cursor.execute('''SELECT password FROM driverRegistration WHERE password=?''',(password,))
            result = self.cursor.fetchone() 
            
            new_password=self.new_password_entry.get()
            if result[0] == check:
                self.cursor.execute('''Update driverRegistration SET password=? WHERE driver_id=?''',
                                    (new_password,driver_id ))
                self.conn.commit()
                messagebox.showinfo("Success", "password updated successfully!")
            else:
                messagebox.showerror("Error", "your old password does not match!")
                 
            
        


        self.change= tk.Button(self.root, text="Change Password",command=change,font=("Verdana", 10),borderwidth=0,bg="white")
        self.change.place(x=380, y=400)

        self.lock = Image.open('image/lock.png')
        self.lock= self.lock.resize((120,130))
        self.lock = ImageTk.PhotoImage(self.lock)
        self.user_label = tk.Label(self.root, image=self.lock,bg="#E8E4E4")
        self.user_label.place(x=690,y=250)



if __name__ == "__main__":
    root = tk.Tk()
    app = DriverChangePassword(root)
    root.mainloop()