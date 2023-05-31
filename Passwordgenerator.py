from tkinter import *
from random import randint

root = Tk()
root.title("Non-semester project - Password generator")


# root.iconbitmap("C:\Users\Saksham Jindal\Downloads")
# root.geometry("500x300")


def new_rand():
    # Clear our entry box
    pw_box.delete(0, END)
    # get the password length
    pw_length = int(my_entry.get())
    # create a variable to hold the password
    my_password = ''
    # loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    # output password
    pw_box.insert(0, my_password)


# copy to clipboard
def clipper():
    # clear the clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(pw_box.get())
    # pop up message
    global pop
    pop = Toplevel(root)
    pop.title("Copied")
    pop.geometry("250*100")

    pop_lable = Label(pop, text="Password copied successfully")
    pop_lable.pack(pady=10)


# lable frame
lf = LabelFrame(root, text="How many Characters?")
lf.pack(pady=20)

# create entry box to designate number of characters
my_entry = Entry(lf, font=("Chronica", 24))
my_entry.pack(pady=20, padx=20)

# create a entry box for our generated password
pw_box = Entry(root, text='', font=("Chronica", 24), bd=0, bg="systembuttonface")
pw_box.pack(pady=20)

# create a frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# create the buttons
my_pass_button = Button(my_frame, text="Generate Password", command=new_rand)
my_pass_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy to clipbord", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()