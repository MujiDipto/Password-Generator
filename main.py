"""
@author: Mujibul Islam Dipto
This program generates a strong password for the user.
"""

import random
import numpy as np
import tkinter as tk
import re


def is_strong_password(pw):
    count = 0 # keep track of strength
    problems = [] # store issues with password
    # check length
    if (len(pw)) < 8:
        pass
    else:
        count += 1

    # check for upper and lower case
    if not (any(c.isupper() for c in pw) and any(c.islower() for c in pw)):
        pass
    else:
        count += 1

    # check for special character
    special_c = re.findall("[^a-zA-Z, 0-9]", pw)
    if len(special_c) == 0:
        pass
    else:
        count += 1

    # check for numbers
    digits = re.findall("[0-9]", pw)
    if len(digits) == 0:
        pass
    else:
        count += 1
    # password is not strong enough
    if count < 4:
        return False
    return True

def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    num = "01234567890"
    sym = "[](){}/;.,-_"
    length = np.random.randint(12, 20)
    combined = lower + upper + num + sym
    # for the rare occurrences where a symbol or a number is missing
    while True: 
        password = "".join(random.sample(combined, length))
        if is_strong_password(password):
            break
    return password

# setup root
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")

# displays the result on the GUI
def show_result(event=None):
    # create canvas to display suggestions
    canvas = tk.Canvas(root, width=460, height=300)
    canvas.place(relx=.5, rely=.7, anchor="c")
    pw = generate_password()
    # display password
    label_pw = tk.Label(root, text = pw)
    label_pw.config(fg = 'yellow')
    label_pw.config(font=("Terminal", 24))
    label_pw.place(relx=.5, rely=.5, anchor="c")
    # copy password to clipboard
    root.clipboard_append(pw)
    canvas.delete("all")

# ensure app works with keyboard (return key)
root.bind('<Return>', show_result)

button = tk.Button(text='Generate Password!', command = show_result)
button.place(relx=.5, rely=.37, anchor="c")

root.mainloop()
