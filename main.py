import time as t
import os
from tkinter import messagebox

def check():
    yesno = messagebox.askyesno("checking if you drink water", "do you drink water ?")
    return yesno

def count(ti):
    while ti:

        mins,secs = divmod(ti,60)
        ti_for = "{:02d}:{:02d}".format(mins,secs)
        print(ti_for,end="\r")
        t.sleep(1)
        ti -= 1

    os.system("zenity --info --title \"drink water\" --text \"drink water\"")
    c = check()

    while c == False:
        if c == False:
            os.system("zenity --info --title \"drink water\" --text \"go drink water\"")
        c = check()

while True:
    count(5)