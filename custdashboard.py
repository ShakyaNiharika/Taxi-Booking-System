import tkinter as tk
from tkinter import Image, messagebox,OptionMenu, Radiobutton,ttk
from PIL import Image, ImageTk
from tkcalendar import*
import sqlite3
import globalvar
import time


class CustomerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("950x630")
        self.root.title('Cus Dashboard')

        self.create_widgets()
    
    def create_widgets(self):
        self.frame1=tk.Frame(self.root,bg="#E8E4E4")
        self.frame1.place(x=0,y=0,relwidth=1, relheight=0.12)

        self.head = tk.Label(self.root, text="Welcome To Taxi Boking System", font=("Verdana", 18),bg="#E8E4E4")
        self.head.place(x=20,y=20)

        self.frame2=tk.Frame(self.root,bg="#E8E4E4")
        self.frame2.place(x=0,y=75,relwidth=0.26, relheight=1)

        self.frame3=tk.Frame(self.root,bg="#F1B547")
        self.frame3.place(x=0,y=590,relwidth=0.26, relheight=0.35)

        self.top = Image.open('image/man.png')
        self.top= self.top.resize((60,50))
        self.top = ImageTk.PhotoImage(self.top)
        self.top_label = tk.Label(self.root, image=self.top,bg="#E8E4E4")
        self.top_label.place(x=700,y=10)
        self.name = tk.Label(text="",font=("Verdana", 16),bg="#E8E4E4")
        self.name.place(x=780,y=25)
        self.name.config(text=globalvar.customer[1])

        
    #image
        self.customer = Image.open('image/yello.png')
        self.resized_customer= self.customer.resize((120,130))
        self.customer = ImageTk.PhotoImage(self.resized_customer)
        self.user_label = tk.Label(self.root, image=self.customer,bg="#E8E4E4")
        self.user_label.place(x=58,y=80)
        self.booking_id = tk.Entry()
        print(self.booking_id)

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

        #this is customer id where is came from login or global variable 
        self_id =globalvar.customer[0]

        self.dashboard = tk.Button(self.root, text="Dashboard",  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.dashboard.place(x=56, y=280)

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
            self.root.destroy()
            from history import History
            hist=tk.Tk()
            History(hist)

        self.history = tk.Button(self.root, text="History", command=history,  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.history.place(x=56, y=365)

#password image
        self.sidelock = Image.open('image/sidelock.png')
        self.sidelock= self.sidelock.resize((20,20))
        self.sidelock = ImageTk.PhotoImage(self.sidelock)
        self.sidelock_label = tk.Label(self.root, image=self.sidelock,bg="#E8E4E4")
        self.sidelock_label.place(x=30,y=410)

        def password():
            self.root.destroy()
            from changepassword import ChangePassword
            passw=tk.Tk()
            ChangePassword(passw)

        self.change_password = tk.Button(self.root, text="Change Password",command=password,  font=("Verdana", 14),bg="#E8E4E4",borderwidth="0")
        self.change_password.place(x=56, y=405)

        def logout():
            self.root.destroy()
            from log import TaxiBookingLogin
            log_out=tk.Tk()
            TaxiBookingLogin(log_out)

        self.Logout= tk.Button(self.root, text="Logout",command=logout , font=("Verdana", 14),borderwidth=0,bg="#F1B547")
        self.Logout.place(x=56, y=590)

#Create Database
        self.conn = sqlite3.connect("crud5.db")
        self.cursor = self.conn.cursor()

        # Create table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS booking
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            pickup_address TEXT , dropoff_address TEXT, pickup_date TEXT, pickup_time TEXT,customer_id INTERGER,FOREIGN KEY(customer_id) REFERENCES customer(id))''')
                            
        self.conn.commit()

#main page
        self.pickup_address = tk.Label(self.root, text="Pickup Address", font=("Verdana", 11),bg="#E8E4E4")
        self.pickup_address.place(x=280,y=140)
        self.pickup_address_entry = tk.Entry(self.root,width="50")
        self.pickup_address_entry.place(x=410,y=140,height="30")

        self.dropoff_address = tk.Label(self.root, text="dropoff Address", font=("Verdana", 11),bg="#E8E4E4")
        self.dropoff_address.place(x=280,y=195)
        self.dropoff_address_entry = tk.Entry(self.root,width="50")
        self.dropoff_address_entry.place(x=410,y=190,height="30")

        self.pickup_date = tk.Label(self.root, text="Picup Date", font=("Verdana", 11),bg="#E8E4E4")
        self.pickup_date.place(x=280,y=240)
        self.pickup_date_entry = DateEntry(self.root, width=12, year=2019, month=6, day=22, background='gray', foreground='white', borderwidth=2)
        self.pickup_date_entry.place(x=410, y=240, height=30, width=300)
        
        self.pickup_time = tk.Label(self.root, text="Pickup Time", font=("Verdana", 11),bg="#E8E4E4")
        self.pickup_time.place(x=280,y=300)
        self.pickup_time_entry = tk.Entry(self.root,width="50")
        self.pickup_time_entry.place(x=410,y=300,height="30")

#Insert into Customerdashboard table
        def request():
            pickup_address=self.pickup_address_entry.get()
            dropoff_address=self.dropoff_address_entry.get()
            pickup_date=self.pickup_date_entry.get()
            pickup_time=self.pickup_time_entry.get()
            status = 'pending'

            if pickup_address and dropoff_address and pickup_date and pickup_time:
                self.cursor.execute('''INSERT INTO booking (pickup_address, dropoff_address, pickup_date, pickup_time,customer_id,booking_status) VALUES (?, ?, ?, ?,?,?)''',
                                        (pickup_address, dropoff_address, pickup_date, pickup_time,self_id,status))
                self.conn.commit()
                messagebox.showinfo("Successfully! Booking has been requested")
                # display_in_treeview(self,pickup_address,dropoff_address,pickup_date,pickup_time) #hereeee
                read()
                # clear_entries()
            else:
                messagebox.showerror("There is smothing problem with your entries")

#To Update the booking
        def update():
            selected_item = self.tree.selection()

            if not selected_item:
                messagebox.showerror("Error", "Please select a record to update.")
                return
            selected_id=self.tree.item(selected_item, "values")[0]
            pickup_address=self.pickup_address_entry.get()
            dropoff_address=self.dropoff_address_entry.get()
            pickup_date=self.pickup_date_entry.get()
            pickup_time=self.pickup_time_entry.get()

            self.cursor.execute('''Update booking SET pickup_address=?, dropoff_address=?, pickup_date=?,pickup_time=? WHERE id=?''',
                                    (pickup_address, dropoff_address, pickup_date,pickup_time, selected_id))
            self.conn.commit()
            messagebox.showinfo("Success", "booking updated successfully!") 
            read()

        def read():
            self.tree.delete(*self.tree.get_children())

            self.cursor.execute('''SELECT id, pickup_address, dropoff_address, pickup_date, pickup_time FROM booking where customer_id = ?''',str(self_id))
            records = self.cursor.fetchall()

            if records:
                for record in records:
                    self.tree.insert("", "end", values=record)

            else:
                messagebox.showinfo("No Records", "No records found.")
        
#to Cancel the booking
        def delete():
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showerror("error","Plese select one")
            else:
                 selected_id = self.tree.item(selected_item, "values")[0]
                 self.cursor.execute('''DELETE FROM booking WHERE id=?''', (selected_id,))
                 self.conn.commit()
                 messagebox.showinfo("success","Your booking have been canceled successfully!")
                 read()


        def clear_entries(self):
            self.pickup_address_entry.delete(0, tk.END)
            self.dropoff_address_entry.delete(0, tk.END)
            self.pickup_date_entry.delete(0, tk.END)
            self.pickup_time_entry.delete(0, tk.END)

        def selectedRow(event):
            selected_item = self.tree.focus()
            values = self.tree.item(selected_item, "values")

            if values:
                
                self.booking_id.insert(0, values[0])

                self.pickup_address_entry .delete(0, "end")
                self.pickup_address_entry .insert(0, values[1])

                self.dropoff_address_entry.delete(0, "end")
                self.dropoff_address_entry.insert(0, values[2])

                self.pickup_date_entry.delete(0, "end")
                self.pickup_date_entry.insert(0, values[3])

                self.pickup_time_entry.delete(0, "end")
                self.pickup_time_entry.insert(0, values[4])

                
#button for Request,Update and Cancel
        self.cancel_booking= tk.Button(self.root, command=read, text="view Booking",font=("Verdana", 10),width=13,bg="#F1B547",)
        self.cancel_booking.place(x=280, y=360)
        self.request_booking= tk.Button(self.root, text="Request Booking",command=request , font=("Verdana", 10),bg="#F1B547",)
        self.request_booking.place(x=400, y=360)
        self.update_booking= tk.Button(self.root, text="Update Booking",command=update,font=("Verdana", 10),bg="#F1B547",)
        self.update_booking.place(x=280, y=405)
        self.cancel_booking= tk.Button(self.root, text="Cancel Booking",command=delete,font=("Verdana", 10),bg="#F1B547",)
        self.cancel_booking.place(x=400, y=405)
        

 #treeview
        self.tree = ttk.Treeview(self.root, columns=("S.N","Pickup Address", "dropoff Address", "Picup Date", "Pickup Time"), show="headings",height=10)
        self.tree.heading("S.N", text="S.N")
        self.tree.heading("Pickup Address", text="Pickup Address")
        self.tree.heading("dropoff Address", text="dropoff Address")
        self.tree.heading("Picup Date", text="Picup Date")
        self.tree.heading("Pickup Time", text="Pickup Time")
        
        
        self.tree.column("S.N", width=50)
        self.tree.column("Pickup Address", width=90)  
        self.tree.column("dropoff Address", width=94)
        self.tree.column("Picup Date", width=80)
        self.tree.column("Pickup Time", width=80)

        #For selected item
        self.tree.bind("<<TreeviewSelect>>",selectedRow)

        self.tree.grid(row=4, columnspan=4, padx=530, pady=350)#here changed padx
        self.tree.tag_configure("Driver_Name", background="#E8E4E4")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerDashboard(root)
    root.mainloop()