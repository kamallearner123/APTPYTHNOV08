import tkinter as tk
from tkinter import messagebox

# Function to handle the button click event
def greet():
    name = entry.get()
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example Program")
root.geometry("300x200")  # Set window size (width x height)

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)  # Add padding around the label

# Create an entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Create a button
button = tk.Button(root, text="Greet", font=("Arial", 12), command=greet)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

