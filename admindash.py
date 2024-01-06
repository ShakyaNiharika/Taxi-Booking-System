import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import *
import sqlite3
import time
import globalvar


class AdminDashboard:
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

        frame3=tk.Frame(self.root,bg="#F9943B")
        frame3.place(x=0,y=590,relwidth=0.26, relheight=0.35)

        self.customer = Image.open('image/admin.png')
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
        

        assign_driver = tk.Button(self.root, text="Assign Drivers",  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        assign_driver.place(x=60, y=260)

        def customer():
            from viewcustomer import ViewCustomer
            self.root.destroy()
            view = tk.Tk()
            ViewCustomer(view)

        view_customers = tk.Button(self.root, text="View Customers",command=customer,font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        view_customers.place(x=60, y=300)

        def driver():
            from viewdriver import ViewDriver
            self.root.destroy()
            view_driver = tk.Tk()
            ViewDriver(view_driver)

        billing = tk.Button(self.root, text="View Drivers",command=driver,  font=("Verdana", 14),bg="#E8E4E4",borderwidth=0)
        billing.place(x=60, y=340)

        def logout():
            self.root.destroy()
            from log import TaxiBookingLogin
            out=tk.Tk()
            TaxiBookingLogin(out)

        self.Logout= tk.Button(self.root, text="Logout",command=logout,  font=("Verdana", 14),borderwidth=0,bg="#F9943B")
        self.Logout.place(x=56, y=590)

    #Create Database
        

    # # Create table if not exists
    #     self.cursor.execute('''CREATE TABLE IF NOT EXISTS adminDashboard
    #                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                         customer_name TEXT,pickup_address TEXT, dropoff_address TEXT, pickup_date TEXT, pickup_time TEXT, booing_status TEXT, assign_driver TEXT)''')
                            
    #     self.conn.commit()


#main page
        def selectedRow(event):
            selected_item = self.tree.focus()
            values = self.tree.item(selected_item, "values")

            if values:
                
                self.Booking_id_entry.insert(0, values[0])

                self.customer_name_entry.delete(0, "end")
                self.customer_name_entry.insert(0, values[1])

                self.Booking_status_entry.delete(0, "end")
                self.Booking_status_entry.insert(0, values[7])

                # self.Assign_driver_entry.delete(0, "end")
                # self.Assign_driver_entry.insert(0, values[3])


        #treeview
        self.tree = ttk.Treeview(self.root, columns=("S.N","Customer Name","Payment Method","Pickup Address", "dropoff Address", "Pickup Date", "Pickup Time","Booking Status"), show="headings",height=10)
        self.tree.heading("S.N", text="S.N")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Payment Method", text="Payment Method")

        self.tree.heading("Pickup Address", text="Pickup Address")
        self.tree.heading("dropoff Address", text="dropoff Address")
        self.tree.heading("Pickup Date", text="Pickup Date")
        self.tree.heading("Pickup Time", text="Pickup Time")
        self.tree.heading("Booking Status", text="Booking Status")
        
        
        self.tree.column("S.N", width=30)
        self.tree.column("Customer Name", width=92)
        self.tree.column("Payment Method", width=92)
        self.tree.column("Pickup Address", width=90)  # Adjust the width as needed
        self.tree.column("dropoff Address", width=94)
        self.tree.column("Pickup Date", width=76)
        self.tree.column("Pickup Time", width=76)
        self.tree.column("Booking Status", width=88)
        self.tree.grid(row=8, columnspan=8, padx=285, pady=110)#here changed padx
        self.tree.tag_configure("Driver_Name", background="#E8E4E4")

        #For selected item
        self.tree.bind("<<TreeviewSelect>>",selectedRow)

        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()

        self.tree.delete(*self.tree.get_children())

        self.cursor.execute('''SELECT 
                    booking.id,
                    customer.username,
                    customer.Method_Of_Payment,
                    booking.pickup_address,
                    booking.dropoff_address,
                    booking.pickup_date,
                    booking.pickup_time,
                    booking.booking_status
                FROM 
                    customer
                JOIN 
                    booking
                ON 
                    customer.id = booking.customer_id''')
        records = self.cursor.fetchall()

        if records:
            for record in records:
                self.tree.insert("", "end", values=record)

        else:
                messagebox.showinfo("No Records", "No records found.")

        #Entry fields

        self.customer_name = tk.Label(self.root, text="Customer Name", font=("Verdana", 11),bg="#E8E4E4")
        self.customer_name.place(x=280,y=375)
        self.customer_name_entry = tk.Entry(self.root,width="35")
        self.customer_name_entry.place(x=410,y=375,height="30")
        
        self.Booking_id = tk.Label(self.root, text="Booking ID", font=("Verdana", 11),bg="#E8E4E4")
        self.Booking_id.place(x=640,y=375)
        self.Booking_id_entry = tk.Entry(self.root,width="35")
        self.Booking_id_entry.place(x=740,y=375,height="30",width="150")

        self.Booking_status = tk.Label(self.root, text="Booking Status", font=("Verdana", 11),bg="#E8E4E4")
        self.Booking_status.place(x=280,y=440)
        self.Booking_status_entry = tk.Entry(self.root,width="35")
        self.Booking_status_entry.place(x=410,y=440,height="30")

        self.Assign_driver = tk.Label(self.root, text="Assign Driver", font=("Verdana", 11),bg="#E8E4E4")
        self.Assign_driver.place(x=640,y=440)
        method = self.selectingdDriver()
        # print(method)
        value = []
        for i in method:
            value1 = i[0]
            value.append(value1)

            print(value)
        self.var = tk.StringVar()

        self.drop_down = OptionMenu(self.root, self.var,*value)

        self.drop_down.config(width=18, indicatoron=True, bg="white")
        self.drop_down["menu"].config(bg="#FFA500")
        self.var.set('Assign the driver')
        self.drop_down.place(x=740,y=440,height="30")
        self.selectingdDriver()

        def assign():
            booking_id=self.Booking_id_entry.get()
            selected_driver = self.var.get()
            self.cursor.execute(f"Update booking SET booking_status='Booked',driverid ='{selected_driver}' where id='{booking_id}' ")
            self.conn.commit()
            messagebox.showinfo("Success", "Assigned successfully!")
            self.root.destroy()
            new_root = tk.Tk()
            AdminDashboard(new_root)
            new_root.mainloop()
            


    #BUTTONS
        self.cancel_booking= tk.Button(self.root,  text="Assign Driver",command=assign,font=("Verdana", 10),width=13,bg="#F1B547",)
        self.cancel_booking.place(x=450, y=530)

        def cancel():
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showerror("error","Plese select one")
            else:
                selected_id = self.tree.item(selected_item, "values")[0]
                self.cursor.execute('''DELETE FROM booking WHERE id=?''', (selected_id,))
                self.conn.commit()
                messagebox.showinfo("success","Your booking have been canceled successfully!")
            self.root.destroy()
            new_root = tk.Tk()
            AdminDashboard(new_root)
            new_root.mainloop()
           
            
        self.cancel_booking= tk.Button(self.root, text="Cancel Booking",command=cancel, font=("Verdana", 10),bg="#F1B547",)
        self.cancel_booking.place(x=580, y=530)
        

        

    def selectingID(self):
        self.cursor.execute('''SELECT driver_id FROM driver WHERE status="Inactive"''')
        result = self.cursor.fetchall()
        id=result
        # print(id[0][0])
        self.conn.commit()
        return id
        
    def selectingdDriver(self):
        self.cursor.execute('''SELECT driver_id , username FROM driver WHERE status="Inactive"''')
        result = self.cursor.fetchall()
        usernames = [row for row in result]
        # print(usernames)
        self.conn.commit()
        return usernames
if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()