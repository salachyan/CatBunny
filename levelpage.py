import tkinter as tk
from tkinter import PhotoImage, font
import subprocess
from PIL import Image, ImageTk

current_window = "main_page"
# Create the main application window
root = tk.Tk()
root.title("Button Options")

def button_click(button_name):
    if button_name == "LVL1":
        open_level_window()

    if button_name == "Start":
        subprocess.Popen(["python3", "main.py"])
        root.destroy()
      
def open_level_window():
    play_button.grid_forget()
    settings_button.grid_forget()
    shop_button.grid_forget()
    closet_button.grid_forget()

    new_bg_image = PhotoImage(file="images/level1_selection_page.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 


    start_button = tk.Button(root, text="Play", command=lambda: button_click("Start"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
    start_button.grid(row=0, column=0, padx=(200), pady=(450))


    goback_button = tk.Button(root, text="Exit", command=lambda: button_click("GoBack"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
    goback_button.grid(row=0, column=1, padx=10) 
    for i in range(2):
        root.grid_columnconfigure(i, weight=1)

# Load and display the background image
bg_image = PhotoImage(file="images/select_level_page.png")
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Set the window size
root.geometry("1000x600")
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

pastel_green = "#A8D6B7"
pastel_blue = "#A6C1E7"
pastel_orange = "#F7C7A7"
pastel_red = "#F69585"

play_button = tk.Button(root, text="Level 1", command=lambda: button_click("LVL1"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
play_button.grid(row=0, column=0, padx=10, pady=(300))

settings_button = tk.Button(root, text="Level 2", command=lambda: button_click("LVL2"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
settings_button.grid(row=0, column=1, padx=10, pady=10)

shop_button = tk.Button(root, text="Level 3", command=lambda: button_click("LVL3"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_orange, fg="white", font=custom_font)
shop_button.grid(row=0, column=2, padx=10, pady=10)

closet_button = tk.Button(root, text="Level 4", command=lambda: button_click("LVL4"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_red, fg="white", font=custom_font)
closet_button.grid(row=0, column=3, padx=10, pady=10)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
