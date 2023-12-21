import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton
from PIL import Image, ImageTk


class CustomerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('Registration form')

        self.create_widgets()
    
    def create_widgets(self):
        frame1=tk.Frame(self.root,bg="#E8E4E4")
        frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        head = tk.Label(self.root, text="Admin Dashboard", font=("Verdana", 18),bg="#E8E4E4")
        head.place(x=40,y=20)

        frame2=tk.Frame(self.root,bg="#E8E4E4")
        frame2.place(x=0,y=72,relwidth=0.26, relheight=1)

        self.customer = Image.open('image/admin.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        user_label = tk.Label(root, image=self.customer)
        user_label.place(x=58,y=80)

        home = tk.Label(self.root, text="Assign Drivers",  font=("Verdana", 14),bg="#E8E4E4")
        home.place(x=60, y=260)

        add_customers = tk.Label(self.root, text="Add Customers",  font=("Verdana", 14),bg="#E8E4E4")
        add_customers.place(x=60, y=295)

        billing = tk.Label(self.root, text="Billing History",  font=("Verdana", 14),bg="#E8E4E4")
        billing.place(x=60, y=340)

        payment = tk.Label(self.root, text="Payment",  font=("Verdana", 14),bg="#E8E4E4")
        payment.place(x=60, y=385)

        Logout= tk.Button(self.root, text="Logout",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        Logout.place(x=60, y=425)


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerDashboard(root)
    root.mainloop()