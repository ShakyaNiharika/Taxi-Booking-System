from tkinter import *
from PIL import ImageTk, Image

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("550x550")
        self.root.title('Registration form')

        self.create_widgets()

    def create_widgets(self):
        lbl_0 = Label(self.root, text="Registration form", width=20, font=("bold", 20))
        lbl_0.place(x=90, y=60)

        lbl_1 = Label(self.root, text="FullName", width=20, font=("bold", 10))
        lbl_1.place(x=80, y=130)
        self.enter_1 = Entry(self.root)
        self.enter_1.place(x=240, y=130)

        lbl_3 = Label(self.root, text="Email", width=20, font=("bold", 10))
        lbl_3.place(x=68, y=180)
        self.enter_3 = Entry(self.root)
        self.enter_3.place(x=240, y=180)

        lbl_4 = Label(self.root, text="Gender", width=20, font=("bold", 10))
        lbl_4.place(x=70, y=230)
        self.vars = IntVar()
        Radiobutton(self.root, text="Male", padx=5, variable=self.vars, value=1).place(x=235, y=230)
        Radiobutton(self.root, text="Female", padx=20, variable=self.vars, value=2).place(x=290, y=230)

        lbl_5 = Label(self.root, text="Country", width=20, font=("bold", 11))
        lbl_5.place(x=70, y=280)
        list_of_cntry = ['Nepal', 'Canada', 'US', 'Germany', 'UK']
        self.cv = StringVar()
        drplist = OptionMenu(self.root, self.cv, *list_of_cntry)
        drplist.config(width=15)
        self.cv.set('Select your Country')
        drplist.place(x=240, y=280)

        lbl_6 = Label(self.root, text="Language", width=20, font=('bold', 10))
        lbl_6.place(x=75, y=330)
        self.vars1 = IntVar()
        self.vars2 = IntVar()
        Checkbutton(self.root, text="English", variable=self.vars1).place(x=230, y=330)
        Checkbutton(self.root, text="Neepali", variable=self.vars2).place(x=300, y=330)

        submit_button = Button(self.root, text='Submit', width=20, bg="black", fg='white', command=self.submit)
        submit_button.place(x=180, y=380)

        self.result_label = Label(self.root, text="", font=("bold", 12))
        self.result_label.place(x=180, y=420)

    def submit(self):
        full_name = self.enter_1.get()
        email = self.enter_3.get()
        gender = "Male" if self.vars.get() == 1 else "Female"
        country = self.cv.get()
        language_english = "English" if self.vars1.get() == 1 else ""
        language_nepali = "Nepali" if self.vars2.get() == 1 else ""

        self.result_label.config(text=f"Full Name: {full_name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\nLanguages: {language_english} {language_nepali}")

if __name__ == "__main__":
    root = Tk()
    app = RegistrationForm(root)
    root.mainloop()