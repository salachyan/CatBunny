import tkinter as tk
from tkinter import PhotoImage, font
import subprocess
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Button Options")

# Define a custom font
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

pastel_green = "#A8D6B7"
pastel_blue = "#A6C1E7"
pastel_orange = "#F7C7A7"
pastel_red = "#F69585"
# Function to handle button clicks
def button_click(button_name):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()


    #main page
    if button_name == "Levels":
        open_level_window()
    if button_name == "Settings":
        open_settings()
    if button_name == "Shop":
        open_shop()
    if button_name == "Closet":
        open_closet()
    if button_name == "Close":
        root.destroy()


    #settings page
    if button_name == "English":
        open_main_page()
    
    if button_name == "Korean":
        open_korean_page()
    #shop page
    if button_name == "Shop":
        open_shop()
    if button_name == "Buy 1":
        open_bought_shop()

    #level page
    if button_name == "LVL1":
        open_intstruction_window()
    if button_name == "Play":
        open_intstruction_window()

    #BEGIN GAME.
    if button_name == "StartGame":
        subprocess.Popen(["python", "main.py"])
        root.destroy()

    if button_name == "Bottom Right":
        open_main_page()
    

def open_main_page():
        
    # Load and display the background image

    new_bg_image = PhotoImage(file="images/main_page_english.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 

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
    play_button = tk.Button(root, text="Levels", command=lambda: button_click("Levels"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
    play_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(100, 10)) 

    # Create Settings button
    settings_button = tk.Button(root, text="Setting", command=lambda: button_click("Settings"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
    settings_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10) 

    # Create Shop button
    shop_button = tk.Button(root, text="Shop", command=lambda: button_click("Shop"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_orange, fg="white", font=custom_font)
    shop_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Create Closet button
    closet_button = tk.Button(root, text="Closet", command=lambda: button_click("Closet"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_red, fg="white", font=custom_font)
    closet_button.grid(row=4, column=0, columnspan=2, padx=10, pady=(10))

    close_button = tk.Button(root, text="Exit", command=lambda: button_click("Close"), width=10, height=2, relief="ridge", borderwidth=4, bg='#D6A2E8', fg="white", font=custom_font)
    close_button.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 50))

    # Center the grid in the window
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(5, weight=1)

def open_settings():
    new_bg_image = PhotoImage(file="images/settings_page.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 

    # Set the window size
    root.geometry("1000x600")  

    # Define a custom font
    custom_font = font.Font(family="Helvetica", size=16, weight="bold")

    # Define pastel colors
    pastel_green = "#A8D6B7"
    pastel_blue = "#A6C1E7"

    english_button = tk.Button(root, text="English", command=lambda: button_click("English"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
    english_button.place(x=325,y=300)
    korean_button = tk.Button(root, text="한국어", command=lambda: button_click("Korean"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
    korean_button.place(x=525,y=300)

    # Center the grid in the window and set column weights
    for i in range(2):
        root.grid_columnconfigure(i, weight=0)

def open_shop():
    # Load and display the background image
    new_bg_image = PhotoImage(file="images/shop_original.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 

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

def open_bought_shop():
    new_bg_image = PhotoImage(file="images/shop_bought.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 
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
    buy_button1.destroy()

def open_level_window():
    # Load and display the background image
    new_bg_image = PhotoImage(file="images/select_level_page.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 

    # Set the window size
    root.geometry("1000x600")
    custom_font = font.Font(family="Helvetica", size=16, weight="bold")

    pastel_green = "#A8D6B7"
    pastel_blue = "#A6C1E7"
    pastel_orange = "#F7C7A7"
    pastel_red = "#F69585"

    play_button = tk.Button(root, text="Level 1", command=lambda: button_click("LVL1"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
    play_button.grid(row=0, column=0, padx=10, pady=(200))

    settings_button = tk.Button(root, text="Level 2", command=lambda: button_click("LVL2"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
    settings_button.grid(row=0, column=1, padx=10, pady=10)

    shop_button = tk.Button(root, text="Level 3", command=lambda: button_click("LVL3"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_orange, fg="white", font=custom_font)
    shop_button.grid(row=0, column=2, padx=10, pady=10)

    closet_button = tk.Button(root, text="Level 4", command=lambda: button_click("LVL4"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_red, fg="white", font=custom_font)
    closet_button.grid(row=0, column=3, padx=10, pady=10)

    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

def open_intstruction_window():
    new_bg_image = PhotoImage(file="images/level1_selection_page.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 


    start_button = tk.Button(root, text="Play", command=lambda: button_click("StartGame"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_green, fg="white", font=custom_font)
    start_button.place(x=200,y=400)


    goback_button = tk.Button(root, text="Exit", command=lambda: button_click("GoBack"), width=10, height=2, relief="ridge", borderwidth=4, bg=pastel_blue, fg="white", font=custom_font)
    goback_button.place(x=700,y=400)
    for i in range(2):
        root.grid_columnconfigure(i, weight=1)

def open_closet():
    # Load and display the background image
    new_bg_image = PhotoImage(file="images/my_closet.png")  
    background_label.configure(image=new_bg_image) 
    background_label.image = new_bg_image 

    root.geometry("1000x600") 

    bottom_right_button = tk.Button(root, text="Exit to Main", command=lambda: button_click("Bottom Right"), width=10, height=2, relief="ridge", borderwidth=4, bg="#FFB9A3", fg="white")
    bottom_right_button.place(relx=1.0, rely=1.0, anchor="se")

def open_korean_page():
    # Load and display the background image
    new_bg_image = PhotoImage(file="images/main_page_korean.png")  
    background_label.configure(image=new_bg_image)
    background_label.image = new_bg_image  

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



#INITIAL MAIN PAGE BACKGROUND.
bg_image = PhotoImage(file="images/main_page_korean.png")  # Replace "background.png" with your image file
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

# Load and display the background image
def open_initial():
    root.geometry("1000x600")  # Width x Height
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

open_initial()







root.mainloop()
