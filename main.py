
# AMA-RILDO

import random
from tkinter import *

# ----------------------------
lower = 'abcdefghjkilmnopqrstuvwxyz'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '0123456789'
symbols = '[]*{}()/;,_-"'
all_char = lower + upper + numbers + symbols

# ----------------------------
root = Tk()
root.geometry('500x350')
root.configure(bg='Gray21')
root.title('PASSWORD GENERATOR')
textTitle = Label(root, text='🔒 PASSWORD GENERATOR 🔒', bg='Gray21', fg='white', font=('Dubai Medium', 14))
textTitle.pack(side=TOP)

def new_rand():
    #clear the entry box
    pw_entry.delete(0,END)
    pw_lenght = int(my_entry.get())
    password = "".join(random.sample(all_char, pw_lenght))
    pw_entry.insert(0, password)

def pop_ok():
    pop.destroy()

def copy():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    # here the popup window 'pop'
    def button_hover_pop(event):
        button_pop['bg'] = 'chartreuse2'
    def leave_hover_pop(event):
        button_pop['bg'] = 'Gray21'
    global pop
    pop = Toplevel(root)
    pop.title('Info')
    pop.geometry('250x150')
    pop.configure(bg='Gray21')
    text_pop = Label(pop, text='📝 Password Copied!',font=('Dubai Medium', 12), bg='Gray21', fg='white')
    text_pop.pack(pady=4)
    button_pop = Button(pop, text='🔐 Done', font=('Dubai Medium', 12), bd=0.5, bg='Gray21', fg='white', command=lambda: pop_ok())
    button_pop.config(height=1, width=10)
    button_pop.pack(pady=10)
    button_pop.bind('<Enter>', button_hover_pop)
    button_pop.bind('<Leave>', leave_hover_pop)

def button_hover(event):
    my_button['bg'] = 'chartreuse2'
def leave_hover(event):
    my_button['bg'] = 'Gray21'
def button_hover_copy(event):
    copy_button['bg'] = 'chartreuse2'
def leave_hover_copy(event):
    copy_button['bg'] = 'Gray21'


#label frame
lf = LabelFrame(root, text='   Digit a number to define the lenght of your password', bg='Gray21', fg='white', font=('Dubai Medium', 12))
lf.pack(pady=18)
#blox of length of password
my_entry = Entry(lf, font=('Helvetica',24), bg='ghost white')
my_entry.pack(pady=8, padx=8)
#returned password
pw_entry = Entry(root, text='', font=('Helvetica',20), bd=0, bg='Gray21', fg='white')
pw_entry.pack(pady=18, padx=10)
# create a frame from the buttons
my_frame = Frame(root)
my_frame.configure(bg='Gray21')
my_frame.pack(pady=20)
# create buttons

my_button = Button(my_frame, text='GENERATE NEW PASSWORD', bd=0.5, command=new_rand, bg='Gray21', fg='white')
my_button.config(height=2, width=26)
my_button.bind('<Enter>', button_hover)
my_button.bind('<Leave>', leave_hover)
my_button.grid(row=0, column=0, padx=5)
# copy password to note
copy_button = Button(my_frame, text='COPY', bd=0.5, command=copy, bg='Gray21', fg='white')
copy_button.config(height=2, width=16)
copy_button.bind('<Enter>', button_hover_copy)
copy_button.bind('<Leave>', leave_hover_copy)
copy_button.grid(row=0, column=1, padx=5)

creator = Label(root, text='Powered by AMA-RILDO  ',font=('Dubai Medium', 7),bd=0, bg='snow', relief=SUNKEN, anchor=E)
creator.pack(fill=X, side=BOTTOM, ipady=2)


root.mainloop()

