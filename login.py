
import tkinter as tk
from tkinter import Image, messagebox
# from tkinter.tix import IMAGETEXT
from PIL import Image, ImageTk

class TaxiBookingLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking Login")
       
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        frame = tk.Frame(root, bg="white")
        frame.place(x=450, y=26, relwidth=0.46, relheight=0.90)

        self.image_path = "logoo.png"  # Replace with the path to your photo
        self.original_image = Image.open(self.image_path)

        target_width = 90
        target_height = 140
        self.image = self.original_image.resize((target_width, target_height))

        self.photo = ImageTk.PhotoImage(self.image)

        image_label = tk.Label(root, image=self.photo,bg="white")
        image_label.place(x=620,y=40)

        self.tittle = tk.Label(root,text="Login:",font=("Verdana", 15),bg="white")
        self.tittle.place(x=644,y=150)

        self.username_entry = tk.Label(root,text="Username:", font=90,bg="white")
        self.username_entry.place(x=500,y=210)

        c1=tk.Entry(root)
        c1.place(x=500,y=240,height=40, width=340,)

        # self.user_image = Image.open('user.png')
        # self.resized_userimage= self.user_image.resize((50,70))
        # self.user_photo = ImageTk.PhotoImage(self.resized_userimage)
       

        # user_label = tk.Label(root, image=self.user_photo,bg="white")
        # user_label.place(x=800, y=225)
      

        self.password_entry = tk.Label(root,text="Password:",font=90,bg="white") 
        self.password_entry.place(x=500,y=300)

        c2=tk.Entry(root)
        c2.place(x=500,y=328,height=40, width=340)

        button=tk.Button(root,text="Log in",bg="#FFA500",font=("Verdana", 10))
        button.place(x=500,y=400,width=340,height=40) 

        # button=tk.Button(root,text="Sign in",bg="green")
        # button.place(x=660,y=420,width=95,height=35)        

        self.forget_password_entry = tk.Label(root,text="Forgot Password ?",font=("Verdana", 13),bg="white") 
        self.forget_password_entry.place(x=596,y=470)

        # button=tk.Button(root,text="Create Account",bg="#FFA500",font=("Verdana", 10))
        # button.place(x=500,y=380,width=340,height=35) 

        frame2 = tk.Frame(root, bg="white", highlightthickness=0)
        frame2.place(x=620,y=520)

       
        button = tk.Label(frame2, text="Create Account",font=("Verdana", 10),fg="#FFA500",)
        button.pack(expand=True, fill="both")

        frame2.config(bg=root.cget("bg"))

        self.root.geometry("950x630")

        # self.result_label = tk.Entry(self.root, text="", font=("bold", 12))
        # self.result_label.place(x=180, y=420)
        

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()

    #   self.result_label.config(text=f"Username: {username}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxiBookingLogin(root)
    root.mainloop()