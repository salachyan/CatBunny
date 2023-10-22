import tkinter as tk
from tkinter import PhotoImage
import subprocess

# Create the main application window
root = tk.Tk()
root.title("Button Options")

def button_click(button_name):
    if button_name == "Buy 1":
        new_bg_image = PhotoImage(file="images/shop_bought.png")  
        background_label.configure(image=new_bg_image)
        background_label.image = new_bg_image  
    if button_name == "Bottom Right":
        subprocess.Popen(["python", "englishmain.py"])
        root.destroy()


# Load and display the background image
bg_image = PhotoImage(file="images/my_closet.png")  
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

root.geometry("1000x600") 

bottom_right_button = tk.Button(root, text="Exit to Main", command=lambda: button_click("Bottom Right"), width=10, height=2, relief="ridge", borderwidth=4, bg="#FFB9A3", fg="white")
bottom_right_button.place(relx=1.0, rely=1.0, anchor="se")


root.mainloop()
