import tkinter as tk
from tkinter import PhotoImage
import subprocess

# Create the main application window
root = tk.Tk()
root.title("Button Options")

# Function to handle button clicks
def button_click(button_name):
    if button_name == "Buy 1":
        # Load the new background image
        new_bg_image = PhotoImage(file="images/shop_bought.png")  
        background_label.configure(image=new_bg_image) 
        background_label.image = new_bg_image 
        buy_button1.destroy()
    if button_name == "Bottom Right":
        subprocess.Popen(["python", "englishmain.py"])
        root.destroy()


# Load and display the background image
bg_image = PhotoImage(file="images/shop_original.png")  
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Set the window size
root.geometry("1000x600")  # Width x Height

buy_button1 = tk.Button(root, text="Buy & Equip", command=lambda: button_click("Buy 1"), width=10, height=2, relief="ridge", borderwidth=4, bg="#57CC99", fg="white")
buy_button1.place(x=210,y=300)
buy_button2 = tk.Button(root, text="Buy & Equip", command=lambda: button_click("Buy 2"), width=10, height=2, relief="ridge", borderwidth=4, bg="#7EABAD", fg="white")
buy_button2.place(x=525,y=300)

# Configure column weights to distribute buttons evenly
for i in range(2):
    root.grid_columnconfigure(i, weight=0)
    root.grid_rowconfigure(i, weight=0)

root.geometry("1000x600")  # Width x Height

buy_button3 = tk.Button(root, text="Buy & Equip", command=lambda: button_click("Buy 3"), width=10, height=2, relief="ridge", borderwidth=4, bg="#D6A2E8", fg="white")
buy_button3.place(x=210, y=420)

buy_button4 = tk.Button(root, text="Buy & Equip", command=lambda: button_click("Buy 4"), width=10, height=2, relief="ridge", borderwidth=4, bg="#E9724C", fg="white")
buy_button4.place(x=525, y=420)

# Configure column weights to distribute buttons evenly
for i in range(2):
    root.grid_columnconfigure(i, weight=0)
    root.grid_rowconfigure(i, weight=0)

bottom_right_button = tk.Button(root, text="Exit to Main", command=lambda: button_click("Bottom Right"), width=10, height=2, relief="ridge", borderwidth=4, bg="#FFB9A3", fg="white")
bottom_right_button.place(relx=1.0, rely=1.0, anchor="se")


root.mainloop()
