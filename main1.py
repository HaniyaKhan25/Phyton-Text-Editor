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

# Func -1 create a new_file:
def new_file():
    text.delete(1.0, tk.END)

# Func -2 create open_file:
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Files Types", "*.txt")]
    )

    if file_path:
        with open(file_path , "r")as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Func -3 create save_file:
def save_file():
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")]
    )

    if file_path:
        with open(file_path, "w")as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved sucessfully")



   
   
