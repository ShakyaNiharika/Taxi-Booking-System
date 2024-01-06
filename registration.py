import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton
# from tkinter.tix import IMAGETEXT
from PIL import Image, ImageTk
from tkcalendar import*
# from tkinter import ttk 
# from ttkcalender import Calendar



import sqlite3

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('Registration form')

        self.create_widgets()

    def create_widgets(self):
         # background image
        self.bg_image = Image.open('image/bgimage.jpg')
        self.resized_bg_image= self.bg_image.resize((950,630))
        self.bg_image = ImageTk.PhotoImage(self.resized_bg_image)
        user_label = tk.Label(self.root, image=self.bg_image)
        user_label.place(relwidth=1, relheight=1)
        
         # gray frame
        gray_frame=tk.Frame(self.root,bg="#E8E4E4")
        gray_frame.place(x=40,y=26,relwidth=0.46, relheight=0.90)

        self.tittle = tk.Label(self.root,text="Taxi Booking System",font=("Verdana", 18),bg="#E8E4E4")
        self.tittle.place(x=120,y=160)

        self.top = Image.open('image/front.png')
        self.top= self.top.resize((400,390))
        self.top = ImageTk.PhotoImage(self.top)
        self.top_label = tk.Label(self.root, image=self.top,bg="#E8E4E4")
        self.top_label.place(x=60,y=200)

        
        frame = tk.Frame(self.root, bg="white")
        frame.place(x=475, y=26, relwidth=0.46, relheight=0.90)

        head = tk.Label(self.root, text="User Registration for Taxi Services", font=("Verdana", 16),bg="white")
        head.place(x=484, y=60)

        username = tk.Label(self.root, text="Username",  font=("bold", 11),bg="white")
        username.place(x=492, y=130)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(x=605, y=130, height=30, width=260)

        password = tk.Label(self.root, text="Password",font=("bold", 11),bg="white")
        password.place(x=488, y=180)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.place(x=605, y=175, height=30, width=260)

        address = tk.Label(self.root, text="Address",  font=("bold", 10),bg="white")
        address.place(x=495, y=225)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.place(x=605, y=220, height=30, width=260)

        phone_number = tk.Label(self.root, text="Phone Number", font=("bold", 10),bg="white")
        phone_number.place(x=485, y=275)
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.place(x=605, y=275, height=30, width=260)

        email_address = tk.Label(self.root, text="Email Address", font=("bold", 10),bg="white")
        email_address.place(x=486, y=330)
        self.email_address_entry = tk.Entry(self.root)
        self.email_address_entry.place(x=605, y=330, height=30, width=260)

        method_of_payment = tk.Label(self.root, text="Method Of Payment", font=("bold", 8),bg="white")
        method_of_payment.place(x=482, y=385)
        method = ['Cash' , 'eSewa' ,'Mobile Banking']
        self.var = tk.StringVar()
        drop_down = OptionMenu(self.root, self.var, *method)
        drop_down.config(width=36 , indicatoron=True,bg="white")
        drop_down["menu"].config(bg="#FFA500")
        self.var.set('Select the methods for payment')
        drop_down.place(x=605, y=385,height=35 )

        gender = tk.Label(self.root, text="Gender", font=("bold", 11),bg="white")
        gender.place(x=485, y=435)
        self.vars = tk.IntVar()
        Radiobutton(self.root, text="Male", padx=5, variable=self.vars, value=1,bg="white").place(x=600, y=435)
        Radiobutton(self.root, text="Female", padx=20, variable=self.vars, value=2,bg="white").place(x=660, y=435)
        Radiobutton(self.root, text="Others", padx=20, variable=self.vars, value=3,bg="white").place(x=740, y=435)


       
        date_of_birth = tk.Label(self.root, text="Date of Birth", font=("bold", 10),bg="white")
        date_of_birth.place(x=482, y=475)
        self.date_of_birth = DateEntry(self.root, width=12, year=2019, month=6, day=22, background='gray', foreground='white', borderwidth=2)
        self.date_of_birth.place(x=605, y=475, height=30, width=260)
       
        def sign_in():
            from log import TaxiBookingLogin
            self.root.destroy()
            sign = tk.Tk()
            TaxiBookingLogin(sign)

        # Database
        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customer
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT, password TEXT, Address TEXT, Phone_Number TEXT, Email_Address TEXT,Method_Of_Payment TEXT,Gender TEXT)''')
                            
        self.conn.commit()
        
        def clear_entries():
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.address_entry.delete(0, ImageTk.END)
            self.phone_number_entry.delete(0,tk.END)
            self.email_address_entry.delete(0,tk.END)
            self.self.var.delete(0,tk.END)
            self.self.vars.delete(0,tk.END)



        def create_record():
            username = self.username_entry.get()
            password = self.password_entry.get()
            Address = self.address_entry.get()
            Phone_Number = self.phone_number_entry.get()
            Email_Address =  self.email_address_entry.get()
            Method_Of_Payment =  self.var.get()
            Gender =  str
            if self.vars.get() ==1:
                Gender = "Male"
            
            elif self.vars.get() ==2:
                Gender = "Female"

            else:
                Gender = 'Others'

            if username and password and Address and Phone_Number and Email_Address and Method_Of_Payment and Gender:
                if len(password) >= 6:
                    if len(password) >= 6:
                        if "@" in Email_Address:
                            self.cursor.execute('''INSERT INTO customer (username, password, Address, Phone_Number, Email_Address, Method_Of_Payment, Gender ) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                                (username, password, Address, Phone_Number, Email_Address, Method_Of_Payment, Gender ))
                            self.conn.commit()
                            messagebox.showinfo("Success", "Record created successfully!")
                            # self.clear_entries()
                            sign_in()
                        else:
                            messagebox.showerror("Error", "Please enter the valid email address")
                    else:
                        messagebox.showerror("Error", "Paaword needs to be atleast 10 digits")
                else:
                    messagebox.showerror("Error", "Paasword needs to be 6 digits atleast")
    
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        

        button=tk.Button(self.root,text="Sign In", command=create_record,bg="#FFA500",font=("Verdana", 10))
        button.place(x=605,y=525,width=260,height=30) 

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()