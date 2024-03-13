import tkinter as tk
from tkinter import messagebox


def do_something():
    messagebox.showinfo("Action", "This button can make something!")


def main():
    window = tk.Tk()
    window.title("Application")
    window.geometry("300x200")

    action_btn = tk.Button(window, text="Make something", command=do_something)
    action_btn.pack()

    noop_btn = tk.Button(window, text="do nothing")
    noop_btn.pack()

    exit_btn = tk.Button(window, text="exit", command=window.quit)
    exit_btn.pack()

    window.mainloop()

main()