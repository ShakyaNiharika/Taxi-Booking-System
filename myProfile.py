import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton
from PIL import Image, ImageTk
import time
# from custdashboard import CustomerDashboard


class MyProfile():
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('My Profile')

        frame1=tk.Frame(self.root,bg="#E8E4E4")
        frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        head = tk.Label(self.root, text="Welcome To Taxi Boking System", font=("Verdana", 18),bg="#E8E4E4")
        head.place(x=20,y=20)

        frame2=tk.Frame(self.root,bg="#E8E4E4")
        frame2.place(x=0,y=72,relwidth=0.26, relheight=1)

        self.customer = Image.open('image/yello.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        self.user_label = tk.Label(self.root, image=self.customer)
        self.user_label.place(x=58,y=80)
    #Time
        def update_time():
            current_time = time.strftime('%H:%M:%S')
            clock_label.config(text=current_time)
            root.after(1000, update_time) 

        clock_label = tk.Label(root, text="", font=("Helvetica", 14))
        clock_label.place(x=75,y=230)
        # Start updating the time
        update_time()

        # def home():
        #     self.root.destroy()
        #     hom=tk.Tk()
        #     CustomerDashboard(hom)

        home = tk.Label(self.root, text="Home",font=("Verdana", 14),bg="#E8E4E4")
        home.place(x=56, y=280)

        my_profile = tk.Button(self.root, text="My Profile",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        my_profile.place(x=56, y=325)

        history = tk.Label(self.root, text="History",  font=("Verdana", 14),bg="#E8E4E4")
        history.place(x=56, y=360)

        change_password = tk.Label(self.root, text="Change Password",  font=("Verdana", 14),bg="#E8E4E4")
        change_password.place(x=56, y=400)

        Logout= tk.Button(self.root, text="Logout",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        Logout.place(x=56, y=435)

    #My Profile
        my_profile = tk.Label(self.root, text="My Profile", font=("Verdana", 12),bg="#E8E4E4")
        my_profile.place(x=280,y=100)
       

        first_name = tk.Label(self.root, text="First Name",  font=("bold", 11))
        first_name.place(x=280, y=150)
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.place(x=420, y=155, height=30, width=260)

        last_name = tk.Label(self.root, text="Last Name",font=("bold", 11),)
        last_name.place(x=280, y=190)
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.place(x=420, y=195, height=30, width=260)

        address = tk.Label(self.root, text="Address",  font=("bold", 11))
        address.place(x=280, y=233)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.place(x=420, y=235, height=30, width=260)

        phone_number = tk.Label(self.root, text="Phone Number", font=("bold", 11),)
        phone_number.place(x=280, y=275)
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.place(x=420, y=275, height=30, width=260)

        email_address = tk.Label(self.root, text="Email Address", font=("bold", 11))
        email_address.place(x=280, y=325)
        self.email_address_entry = tk.Entry(self.root)
        self.email_address_entry.place(x=420, y=325, height=30, width=260)

        method_of_payment = tk.Label(self.root, text="Method Of Payment", font=("bold",11))
        method_of_payment.place(x=280, y=385)
        method = ['Cash' , 'eSewa' ,'Mobile Banking']
        self.var = tk.StringVar()
        drop_down = OptionMenu(self.root, self.var, *method)
        drop_down.config(width=36 , indicatoron=True,bg="white")
        drop_down["menu"].config(bg="#FFA500")
        self.var.set('Select the methods for payment')
        drop_down.place(x=420, y=375,height=35 )

        gender = tk.Label(self.root, text="Gender", font=("bold", 11),)
        gender.place(x=280, y=425)
        self.vars = tk.IntVar()
        Radiobutton(self.root, text="Male", padx=5, variable=self.vars, value=1,bg="white").place(x=420, y=430)
        Radiobutton(self.root, text="Female", padx=20, variable=self.vars, value=2,bg="white").place(x=480, y=430)
        Radiobutton(self.root, text="Others", padx=20, variable=self.vars, value=3,bg="white").place(x=560, y=430)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyProfile(root)
    root.mainloop()