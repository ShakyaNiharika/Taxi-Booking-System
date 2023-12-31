import tkinter as tk
from tkinter import Image, messagebox,OptionMenu
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from custdashboard import CustomerDashboard

class Driverlogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking Login")
       
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # background image
        self.bg_image = Image.open('image/bgimage.jpg')
        self.resized_bg_image= self.bg_image.resize((950,630))
        self.bg_image = ImageTk.PhotoImage(self.resized_bg_image)
        user_label = tk.Label(self.root, image=self.bg_image)
        user_label.place(relwidth=1, relheight=1)
        
        # gray frame
        gray_frame=tk.Frame(self.root,bg="#E8E4E4")
        gray_frame.place(x=40,y=26,relwidth=0.46, relheight=0.90)
       
        # white frame
        frame = tk.Frame(self.root, bg="white")
        frame.place(x=475, y=26, relwidth=0.46, relheight=0.90)

        frame3=tk.Frame(self.root)

        self.image_path = "image/logoo.png"  # Replace with the path to your photo
        self.original_image = Image.open(self.image_path)

        target_width = 90
        target_height = 140
        self.image = self.original_image.resize((target_width, target_height))

        self.photo = ImageTk.PhotoImage(self.image)

        image_label = tk.Label(self.root, image=self.photo,bg="white")
        image_label.place(x=640,y=40)

        # #choice
        # method = ['Customer' , 'Admin' ,'Driver']
        # self.var = tk.StringVar()
        # drop_down = OptionMenu(self.root, self.var, *method)
        # drop_down.config(width=16 , indicatoron=True,bg="white",borderwidth=0)
        # drop_down["menu"].config(bg="#FFA500")
        # self.var.set('Select the user')
        # drop_down.place(x=726,y=209,height=35 )

        self.tittle = tk.Label(self.root,text="Login:",font=("Verdana", 15),bg="white")
        self.tittle.place(x=664,y=150)

        self.email = tk.Label(self.root,text="Email:", font=90,bg="white")
        self.email.place(x=520,y=210)

        self.email_entry=tk.Entry(self.root)
        self.email_entry.place(x=520,y=240,height=40, width=340,)

        # self.user_image = Image.open('user.png')
        # self.resized_userimage= self.user_image.resize((50,70))
        # self.user_photo = ImageTk.PhotoImage(self.resized_userimage)
       

        # user_label = tk.Label(self.root, image=self.user_photo,bg="white")
        # user_label.place(x=800, y=225)
      

        self.password = tk.Label(self.root,text="Password:",font=90,bg="white") 
        self.password.place(x=520,y=300)

        self.password_entry=tk.Entry(self.root,show="*")
        self.password_entry.place(x=520,y=328,height=40, width=340)

        def show_password():
            if self.password_entry.cget("show") == "*":
                self.password_entry.config(show="")
            else:
                self.password_entry.config(show="*")
                


        check_button = tk.Checkbutton(self.root,text="show password", command=show_password,bg="white")
        check_button.place(x=745,y=370)


 #Database
        def login():
            
       
        
            self.conn = sqlite3.connect("crud5.db")
            self.cursor = self.conn.cursor()
            email = self.email_entry.get()
            password = self.password_entry.get()

        
            self.cursor.execute('''SELECT * FROM driverRegistration WHERE email_address=? AND password=? ''',(email,password))
            result = self.cursor.fetchone()
            if result:
                messagebox.showinfo("Success", "Record created successfully!")
                # self.root.destroy()
                # self.customer_dash = tk.Tk()
                # CustomerDashboard(self.customer_dash)
            else:
                messagebox.showerror("Invalid password or email")
            
            
        button=tk.Button(self.root,text="Log in driver",command=login, bg="#FFA500",font=("Verdana", 10))
        button.place(x=520,y=400,width=340,height=40) 

        self.forget_password_entry = tk.Label(self.root,text="Forgot Password ?",font=("Verdana", 13),bg="white") 
        self.forget_password_entry.place(x=616,y=460)

        # button=tk.Button(self.root,text="Create Account",bg="#FFA500",font=("Verdana", 10))
        # button.place(x=500,y=380,width=340,height=35) 

        frame2 = tk.Frame(self.root, bg="white", highlightthickness=0)
        frame2.place(x=640,y=510)


        def createAccount():
            from driverregistration import DriverRegistration
            self.root.destroy()
            here = tk.Tk()
            DriverRegistration(here)
       
        button = tk.Button(frame2, text="Create Account",command=createAccount, font=("Verdana", 10),fg="#FFA500",bg="white",borderwidth=0)
        button.pack(expand=True, fill="both")


        frame2.config(bg=root.cget("bg"))

        self.root.geometry("950x630")

#         # self.result_label = tk.Entry(self.root, text="", font=("bold", 12))
#         # self.result_label.place(x=180, y=420)
        
        #Database connection
        self.conn = sqlite3.connect("crud1.db")
        self.cursor = self.conn.cursor()
    

        
        

#     #   self.result_label.config(text=f"Username: {username}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Driverlogin(root)
    root.mainloop()