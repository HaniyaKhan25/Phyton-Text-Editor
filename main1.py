# Text Editor App

# import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog , messagebox

# create main window:
root= tk.Tk()
root.title("Text Editor")
root.geometry("600x500")

# create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12) 
)



   
   
