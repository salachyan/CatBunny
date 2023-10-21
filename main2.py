import tkinter as tk
from tkinter import PhotoImage
import subprocess

# Create the main application window
root = tk.Tk()
root.title("Button Options")

# Function to handle button clicks
def button_click(button_name):
    if button_name == "Play":
        subprocess.Popen(["python", "main.py"])
        root.destroy()
    # if button_name == "Settings":
        
    # if button_name == "Shop":

# Load and display the background image
bg_image = PhotoImage(file="background.png")  # Replace "background.png" with your image file
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Set the window size
root.geometry("300x500")  # Width x Height

# Create a label widget
label = tk.Label(root, text="Choose an Option!")
label.grid(row=0, column=0, columnspan=2, pady=20)

# Create Play button
play_button = tk.Button(root, text="Play", command=lambda: button_click("Play"), width=10, height=2, relief="ridge", borderwidth=4, bg="green", fg="white")
play_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

# Create Settings button
settings_button = tk.Button(root, text="Settings", command=lambda: button_click("Settings"), width=10, height=2, relief="ridge", borderwidth=4, bg="blue", fg="white")
settings_button.grid(row=2, column=0, columnspan=2, padx=20, pady=5)

# Create Shop button
shop_button = tk.Button(root, text="Shop", command=lambda: button_click("Shop"), width=10, height=2, relief="ridge", borderwidth=4, bg="orange", fg="white")
shop_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# Center the grid in the window
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.mainloop()
