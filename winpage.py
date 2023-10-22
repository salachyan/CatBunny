import tkinter as tk
from tkinter import PhotoImage, font
import subprocess
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Button Options")


def button_click(button_name):
    if button_name == "Shop":
        subprocess.Popen(["python", "shop_interface.py"])
        root.destroy()
    if button_name == "Home":
        subprocess.Popen(["python", "englishmain.py"])
        root.destroy()


bg_image = PhotoImage(file="images/you_win_page.png") 
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Set the window size
root.geometry("1000x600")  # Width x Height


custom_font = font.Font(family="Helvetica", size=16, weight="bold")


pastel_green = "#A8D6B7"
pastel_blue = "#A6C1E7"
pastel_orange = "#F7C7A7"
pastel_red = "#F69585"




play_button = tk.Button(root, text="Next Level?", command=lambda: button_click("Continue"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
play_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(200,10)) 

settings_button = tk.Button(root, text="Shop", command=lambda: button_click("Shop"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
settings_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10) 

shop_button = tk.Button(root, text="Go to Home", command=lambda: button_click("Home"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_orange, fg="white", font=custom_font)
shop_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# Center the grid in the window
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(3, weight=0)

root.mainloop()
