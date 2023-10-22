import tkinter as tk
from tkinter import PhotoImage, font
import subprocess
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Button Options")


# Function to handle button clicks
def button_click(button_name):
    if button_name == "Play":
        subprocess.Popen(["python", "levelpage.py"])
        root.destroy()
    if button_name == "Settings":
        subprocess.Popen(["python", "settings.py"])
        root.destroy()
    if button_name == "Shop":
        subprocess.Popen(["python", "shop_interface.py"])
        root.destroy()
    if button_name == "Closet":
        subprocess.Popen(["python", "mycloset.py"])
        root.destroy()
    if button_name == "Close":
        root.destroy()
# Load and display the background image
bg_image = PhotoImage(file="images/main_page_korean.png")  # Replace "background.png" with your image file
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Set the window size
root.geometry("1000x600")  # Width x Height

# Define a custom font
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

# Define pastel colors
pastel_green = "#A8D6B7"
pastel_blue = "#A6C1E7"
pastel_orange = "#F7C7A7"
pastel_red = "#F69585"




# Create Play button
play_button = tk.Button(root, text="레벨", command=lambda: button_click("Levels"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
play_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(100, 10)) 

# Create Settings button
settings_button = tk.Button(root, text="세팅", command=lambda: button_click("Settings"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
settings_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10) 

# Create Shop button
shop_button = tk.Button(root, text="가게", command=lambda: button_click("Shop"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_orange, fg="white", font=custom_font)
shop_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create Closet button
closet_button = tk.Button(root, text="옷장", command=lambda: button_click("Closet"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_red, fg="white", font=custom_font)
closet_button.grid(row=4, column=0, columnspan=2, padx=10, pady=(10))

close_button = tk.Button(root, text="닫기", command=lambda: button_click("Close"), width=10, height=2, relief="ridge", borderwidth=4, bg='#D6A2E8', fg="white", font=custom_font)
close_button.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 50))
# Center the grid in the window
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()
