import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        display_text(os.path.basename(filename))

def display_text(filename):
    window = tk.Toplevel(root)
    window.geometry('100x100')
    label = tk.Label(window, text=filename)
    label.pack(expand=True)

root = tk.Tk()
root.resizable(False, False)
root.geometry('200x200')

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(expand=True)

root.mainloop()
