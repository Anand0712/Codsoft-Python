import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        password_label.config(text="Invalid length")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    password_label.config(text=password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate a password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
password_label = tk.Label(root, text="", wraplength=3000)
password_label.pack()

# Start the GUI main loop
root.mainloop()
