import tkinter as tk
from PIL import Image, ImageTk

def open_register_page():
    # Destroy the login page
    root.destroy()
    print("To call Registratrion Page:")
    print("We will cover this in futher class :")


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your authentication logic here
    # For simplicity, I'm just printing the entered username and password
    print(f"Username: {username}\nPassword: {password}")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Load the image
image_path = "img.png"  # Replace with the path to your photo
original_image = Image.open(image_path)

# Resize the image to a fixed height and width while maintaining the aspect ratio
target_width = 500
target_height = 500
image = original_image.resize((target_width, target_height))

photo = ImageTk.PhotoImage(image)

# Set window size based on the fixed dimensions
root.geometry(f"900x900")

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.pack()

# Create username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Create password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Create register button
register_button = tk.Button(root, text="Register", command=open_register_page)
register_button.pack()

# Run the Tkinter event loop
root.mainloop()