import tkinter as tk
from tkinter import PhotoImage, font
import subprocess
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Button Options")

# Function to handle button clicks
def button_click(button_name):
    if button_name == "English":
        subprocess.Popen(["python3", "englishmain.py"])
        root.destroy()

bg_image = PhotoImage(file="images/settings_page.png")
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Set the window size
root.geometry("1000x600")  

# Define a custom font
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

# Define pastel colors
pastel_green = "#A8D6B7"
pastel_blue = "#A6C1E7"
pastel_orange = "#F7C7A7"
pastel_red = "#F69585"

english_button = tk.Button(root, text="English", command=lambda: button_click("English"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
english_button.grid(row=0, column=0,  columnspan=2, padx = 325, pady=(300))

korean_button = tk.Button(root, text="한국어", command=lambda: button_click("Korean"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
korean_button.grid(row=0, column=1, padx = 525 , columnspan=2, pady=(300)) 

# Center the grid in the window and set column weights
for i in range(2):
    root.grid_columnconfigure(i, weight=0)



root.mainloop()
