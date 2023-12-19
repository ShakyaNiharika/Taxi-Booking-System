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

    # # Database
    #     self.conn = sqlite3.connect("crud.db")
    #     self.cursor = self.conn.cursor()

    #     # Create table if not exists
    #     self.cursor.execute('''CREATE TABLE IF NOT EXISTS records
    #                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                          First_Name TEXT, Last_Name TEXT, Address TEXT, Phone_Number TEXT, Email_Address TEXT,Method_Of_Payment TEXT,Gender TEXT,)''')
    #     self.conn.commit()
    # def create_record(self):
    #     name = self.first_name_entry.get()
    #     age = self.first_name_entry.get()
    #     address = self.address_entry.get()

    def create_widgets(self):
         # background image
        self.bg_image = Image.open('bgimage.jpg')
        self.resized_bg_image= self.bg_image.resize((950,630))
        self.bg_image = ImageTk.PhotoImage(self.resized_bg_image)
        user_label = tk.Label(self.root, image=self.bg_image)
        user_label.place(relwidth=1, relheight=1)
        
        gray_frame=tk.Frame(self.root,bg="#E8E4E4")
        gray_frame.place(x=40,y=26,relwidth=0.46, relheight=0.90)
        
        frame = tk.Frame(self.root, bg="white")
        frame.place(x=475, y=26, relwidth=0.46, relheight=0.90)

        head = tk.Label(self.root, text="User Registration for Taxi Services", font=("Verdana", 16),bg="white")
        head.place(x=484, y=60)

        first_name = tk.Label(self.root, text="First Name",  font=("bold", 11),bg="white")
        first_name.place(x=492, y=130)
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.place(x=605, y=130, height=30, width=260)

        last_name = tk.Label(self.root, text="Last Name",font=("bold", 11),bg="white")
        last_name.place(x=488, y=180)
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.place(x=605, y=175, height=30, width=260)

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

        # def pick_date(e):
            
        #     data_window = Toplevel()

       
        date_of_birth = tk.Label(self.root, text="Date of Birth", font=("bold", 10),bg="white")
        date_of_birth.place(x=482, y=475)
        self.date_of_birth_entry = tk.Entry(self.root)
        self.date_of_birth_entry.place(x=605, y=475, height=30, width=260)
        # self.date_of_birth_entry.insert(0, "dd/mm/yy")
        # cal = Calendar(root, selectmode = 'day',
        #        year = 2020, month = 5,
        #        day = 22)
 


        def sign_in():
            from log import TaxiBookingLogin
            # self.root.destroy()
            sign = tk.Tk()
            TaxiBookingLogin(sign)

        

        button=tk.Button(self.root,text="Sign In",bg="#FFA500",font=("Verdana", 10))
        button.place(x=605,y=525,width=260,height=30) 

       

        # if first_name and last_name and address and phone_number and email_address and method_of_payment and gender and date_of_birth:
        #     messagebox.showinfo("Success","Record created successfully")
        #     sign_in()
        # else:
        #     messagebox.showinfo("Error","Please fill in all fields.")

        # lbl_4 = Label(self.root, text="Gender", width=20, font=("bold", 10))
        # lbl_4.place(x=70, y=230)
        # self.vars = IntVar()
        # Radiobutton(self.root, text="Male", padx=5, variable=self.vars, value=1).place(x=235, y=230)
        # Radiobutton(self.root, text="Female", padx=20, variable=self.vars, value=2).place(x=290, y=230)

        # lbl_5 = Label(self.root, text="Country", width=20, font=("bold", 11))
        # lbl_5.place(x=70, y=280)
        # list_of_cntry = ['Nepal', 'Canada', 'US', 'Germany', 'UK']
        # self.cv = StringVar()
        # drplist = OptionMenu(self.root, self.cv, *list_of_cntry)
        # drplist.config(width=15)
        # self.cv.set('Select your Country')
        # drplist.place(x=240, y=280)

        # lbl_6 = Label(self.root, text="Language", width=20, font=('bold', 10))
        # lbl_6.place(x=75, y=330)
        # self.vars1 = IntVar()
        # self.vars2 = IntVar()
        # Checkbutton(self.root, text="English", variable=self.vars1).place(x=230, y=330)
        # Checkbutton(self.root, text="Neepali", variable=self.vars2).place(x=300, y=330)

        # submit_button = Button(self.root, text='Sign In', width=30, bg="black", fg='white', command=self.submit)
        # submit_button.place(x=240, y=440)

        # self.result_label = Label(self.root, text="", font=("bold", 12))
        # self.result_label.place(x=180, y=420)

    # def submit(self):
    #     full_name = self.enter_1.get()
    #     email = self.enter_3.get()
    #     gender = "Male" if self.vars.get() == 1 else "Female"
    #     country = self.cv.get()
    #     language_english = "English" if self.vars1.get() == 1 else ""
    #     language_nepali = "Nepali" if self.vars2.get() == 1 else ""

    #     self.result_label.config(text=f"Full Name: {full_name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\nLanguages: {language_english} {language_nepali}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()