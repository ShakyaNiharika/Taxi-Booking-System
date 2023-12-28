import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from myProfile import MyProfile
import time



class History:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('History')

        self.create_widgets()
    
    def create_widgets(self):
        self.frame1=tk.Frame(self.root,bg="#E8E4E4")
        self.frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        self.head = tk.Label(self.root, text="Welcome To Taxi Boking System", font=("Verdana", 18),bg="#E8E4E4")
        self.head.place(x=20,y=20)

        self.frame2=tk.Frame(self.root,bg="#E8E4E4")
        self.frame2.place(x=0,y=72,relwidth=0.26, relheight=1)

        self.frame3=tk.Frame(self.root,bg="#F9943B")
        self.frame3.place(x=0,y=590,relwidth=0.26, relheight=0.35)

        self.customer = Image.open('image/yello.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        self.user_label = tk.Label(self.root, image=self.customer,bg="#E8E4E4")
        self.user_label.place(x=58,y=80)

    #Time
        def update_time():
            current_time = time.strftime('%H:%M:%S')
            clock_label.config(text=current_time)
            root.after(1000, update_time) 

        clock_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        clock_label.place(x=75,y=230)
        # Start updating the time
        update_time()

#dashboard image
        self.dash = Image.open('image/dash.png')
        self.dash= self.dash.resize((20,20))
        self.dash = ImageTk.PhotoImage(self.dash)
        self.dash_label = tk.Label(self.root, image=self.dash,bg="#E8E4E4")
        self.dash_label.place(x=30,y=285)

        dashboard = tk.Button(self.root, text="Dashboard",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        dashboard.place(x=56, y=280)

#profile image
        self.profile = Image.open('image/profile.png')
        self.profile= self.profile.resize((20,20))
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_label = tk.Label(self.root, image=self.profile,bg="#E8E4E4")
        self.profile_label.place(x=30,y=330)

        def profile():
            self.root.destroy()
            pro=tk.Tk()
            MyProfile(pro)

        profile_section = tk.Button(self.root, text="My Profile",command=profile,font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        profile_section.place(x=56, y=325)



        history = tk.Button(self.root, text="History",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        history.place(x=56, y=360)

#history image
        self.his = Image.open('image/history.png')
        self.his= self.his.resize((20,20))
        self.his = ImageTk.PhotoImage(self.his)
        self.his_label = tk.Label(self.root, image=self.his,bg="#E8E4E4")
        self.his_label.place(x=30,y=370)

#password image
        self.sidelock = Image.open('image/sidelock.png')
        self.sidelock= self.sidelock.resize((20,20))
        self.sidelock = ImageTk.PhotoImage(self.sidelock)
        self.sidelock_label = tk.Label(self.root, image=self.sidelock,bg="#E8E4E4")
        self.sidelock_label.place(x=30,y=405)

        def password():
            self.root.destroy()
            from changepassword import ChangePassword
            passw=tk.Tk()
            ChangePassword(passw)

        change_password = tk.Button(self.root, text="Change Password",command=password,  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        change_password.place(x=56, y=400)

        self.Logout= tk.Button(self.root, text="Logout",  font=("Verdana", 14),borderwidth=0,bg="#F9943B")
        self.Logout.place(x=56, y=590)

    #frame
        # frame3=tk.Frame(root,bg="#E8E4E4")
        # frame3.place(x=270,y=100,relwidth=0.69, relheight=0.70)
    #heading
        head = tk.Label(self.root, text="Your History", font=("Verdana", 18))
        head.place(x=320,y=110)
    #treeview
        self.tree = ttk.Treeview(self.root, columns=("Driver Name", "Phone Number", "Email Address", "Pickup Address","Dropoff Address","Time","Date"), show="headings",height=15)
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
    app = History(root)
    root.mainloop()