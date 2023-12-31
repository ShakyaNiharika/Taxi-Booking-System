import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton
from PIL import Image, ImageTk
import time
# from custdashboard import CustomerDashboard
import globalvar
import sqlite3


class MyProfile():
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('My Profile')
        # try:
        #     self.frame2=tk.Frame(self.root).place()
        #     print('Yes')
        # except:
        #     print('asd error')

    #middle frame which needs to be change
        #
            
        self.create_widgets()
    
    def create_widgets(self):
        #to set we need to do this
        self.string = tk.StringVar()
        self.string2 = tk.StringVar()
        self.string3 = tk.StringVar()
        self.string4 = tk.StringVar()
        self.string5 = tk.StringVar()
        self.string6 = tk.StringVar()




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

        def dashboard():
            self.root.destroy()
            from custdashboard import CustomerDashboard
            hom=tk.Tk()
            CustomerDashboard(hom)

        self.dashboard = tk.Button(self.root, text="Dashboard", command=dashboard,font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.dashboard.place(x=56, y=280)

        self.top = Image.open('image/man.png')
        self.top= self.top.resize((60,50))
        self.top = ImageTk.PhotoImage(self.top)
        self.top_label = tk.Label(self.root, image=self.top,bg="#E8E4E4")
        self.top_label.place(x=700,y=10)
        self.name = tk.Label(text="",font=("Verdana", 16),bg="#E8E4E4")
        self.name.place(x=780,y=25)
        self.name.config(text=globalvar.customer[1])

#profile image
        self.profile = Image.open('image/profile.png')
        self.profile= self.profile.resize((20,20))
        self.profile = ImageTk.PhotoImage(self.profile)
        self.profile_label = tk.Label(self.root, image=self.profile,bg="#E8E4E4")
        self.profile_label.place(x=30,y=330)

        def profile():
            self.root.destroy()
            from myProfile import MyProfile
            pro=tk.Tk()
            MyProfile(pro)

        self.profile_section = tk.Button(self.root, text="My Profile",command=profile,font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.profile_section.place(x=56, y=325)

#history image
        self.his = Image.open('image/history.png')
        self.his= self.his.resize((20,20))
        self.his = ImageTk.PhotoImage(self.his)
        self.his_label = tk.Label(self.root, image=self.his,bg="#E8E4E4")
        self.his_label.place(x=30,y=370)

        #send to page history
        def history():
            from history import History
            self.root.destroy()
            self.hist=tk.Tk()
            History(self.hist)

        self.history = tk.Button(self.root, text="History", command=history,  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.history.place(x=56, y=360)

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

        self.change_password = tk.Button(self.root, text="Change Password",command=password,  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.change_password.place(x=56, y=400)
        
        def logout():
            self.root.destroy()
            from log import TaxiBookingLogin
            log_out=tk.Tk()
            TaxiBookingLogin(log_out)

        self.Logout= tk.Button(self.root, text="Logout",command=logout,font=("Verdana", 14),borderwidth=0,bg="#F9943B")
        self.Logout.place(x=56, y=590)

    #My Profile
        background_frame=tk.Frame(self.root,bg="#E8E4E4")
        background_frame.place(x=300,y=162,relwidth=0.58, relheight=0.62)

        my_profile = tk.Label(self.root, text="My Profile", font=("Verdana", 18),bg="#E8E4E4")
        my_profile.place(x=310,y=100)

        username = tk.Label(self.root, text="Username",  font=("bold", 11),bg="#E8E4E4")
        username.place(x=320, y=180)
        self.user_name_entry = tk.Entry(self.root,textvariable=self.string)
        self.user_name_entry.place(x=460, y=180, height=30, width=260)
        self.string.set(globalvar.customer[1])

        address = tk.Label(self.root, text="Address",  font=("bold", 11),bg="#E8E4E4")
        address.place(x=320, y=233)
        self.address_entry = tk.Entry(self.root,textvariable=self.string2)
        self.address_entry.place(x=460, y=233, height=30, width=260)
        self.string2.set(globalvar.customer[3])

        phone_number = tk.Label(self.root, text="Phone Number", font=("bold", 11),bg="#E8E4E4")
        phone_number.place(x=320, y=285)
        self.phone_number_entry = tk.Entry(self.root,textvariable=self.string3)
                                           
        self.phone_number_entry.place(x=460, y=285, height=30, width=260)
        self.string3.set(globalvar.customer[4])

        email_address = tk.Label(self.root, text="Email Address", font=("bold", 11),bg="#E8E4E4")
        email_address.place(x=320, y=335)
        self.email_address_entry = tk.Entry(self.root,textvariable=self.string4)
        self.email_address_entry.place(x=460, y=335, height=30, width=260)
        self.string4.set(globalvar.customer[5])

        method_of_payment = tk.Label(self.root, text="Method Of Payment", font=("bold",11),bg="#E8E4E4")
        method_of_payment.place(x=320, y=390)
        method = ['Cash' , 'eSewa' ,'Mobile Banking']
        self.var = tk.StringVar()
        drop_down = OptionMenu(self.root, self.var, *method)
        drop_down.config(width=36 , indicatoron=True,bg="white")

        drop_down["menu"].config(bg="#FFA500")
        self.var.set(globalvar.customer[6])
        drop_down.place(x=460, y=390,height=35 )

        gender = tk.Label(self.root, text="Gender", font=("bold", 11),)
        gender.place(x=320, y=445)
        self.vars = tk.StringVar()
        self.vars.set(globalvar.customer[7])
        Radiobutton(self.root, text="Male", padx=5, variable=self.vars, value="Male",bg="#E8E4E4",).place(x=460, y=445)
        Radiobutton(self.root, text="Female", padx=20, variable=self.vars, value="Female",bg="#E8E4E4",).place(x=530, y=445)
        Radiobutton(self.root, text="Others", padx=20, variable=self.vars, value="Others",bg="#E8E4E4",).place(x=620, y=445)
        # self.string5.set(globalvar.customer[6])

        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()

        def update():
            username=self.user_name_entry.get()
            address=self.address_entry.get()
            phone_number=self.phone_number_entry.get()
            email_address=self.email_address_entry.get()
            method_of_payment=self.var.get()
            gender=self.vars.get()
            update_value=globalvar.customer[0]

            self.cursor.execute('''Update customer SET username=?, address=?, phone_number=?,email_address=?,method_of_payment=?,gender=? WHERE id=?''',
                                    (username, address, phone_number,email_address,method_of_payment,gender, update_value))
            self.conn.commit()
            messagebox.showinfo("Success", "updated successfully!")

        self.update= tk.Button(self.root, text="Update",font=("Verdana", 10),command=update,bg="#F1B547",width="30",)
        self.update.place(x=460, y=495)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyProfile(root)
    root.mainloop()