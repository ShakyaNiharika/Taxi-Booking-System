import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from myProfile import MyProfile



class History:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('History')

        self.create_widgets()
    
    def create_widgets(self):
        frame1=tk.Frame(self.root,bg="#E8E4E4")
        frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        head = tk.Label(self.root, text="Welcome To Taxi Boking System", font=("Verdana", 18),bg="#E8E4E4")
        head.place(x=20,y=20)

        frame2=tk.Frame(self.root,bg="#E8E4E4")
        frame2.place(x=0,y=72,relwidth=0.26, relheight=1)

        self.customer = Image.open('image/yello.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        user_label = tk.Label(root, image=self.customer)
        user_label.place(x=58,y=80)

        home = tk.Button(self.root, text="Home",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        home.place(x=56, y=260)

        def profile():
            self.root.destroy()
            pro=tk.Tk()
            MyProfile(pro)

        profile_section = tk.Button(self.root, text="My Profile",command=profile,font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        profile_section.place(x=56, y=295)

        history = tk.Button(self.root, text="History",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        history.place(x=56, y=340)

        change_password = tk.Button(self.root, text="Change Password",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        change_password.place(x=56, y=385)

        Logout= tk.Button(self.root, text="Logout",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        Logout.place(x=56, y=425)

    #frame
        # frame3=tk.Frame(root,bg="#E8E4E4")
        # frame3.place(x=270,y=100,relwidth=0.69, relheight=0.70)
    #heading
        head = tk.Label(self.root, text="Your History", font=("Verdana", 18))
        head.place(x=320,y=110)
    #treeview
        self.tree = ttk.Treeview(root, columns=("Driver Name", "Phone Number", "Email Address", "Pickup Address","Dropoff Address","Time","Date"), show="headings",height=15)
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