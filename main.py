from tkinter import *


window = Tk()
window.title('Miles2Kilometre Calculator')
window.minsize(width=200, height=100)

# user input miles

user_input = Entry(width=20)
user_input.grid(column=1, row=0)

# mile label
mile_label = Label(text='Mile', font=('Arial', 10))
mile_label.grid(column=2, row=0)

# is equal to
equal = Label(text='is equal to', font=('Arial', 10))
equal.grid(column=0, row=1)

# output
converted = Label(text='0', font=('Arial', 10))
converted.grid(column=1, row=1)


# Kilometre
kilometre = Label(text='Kilometre', font=('Arial', 10))
kilometre.grid(column=2, row=1)


# conversion function


def convert():
    conversion = float(user_input.get()) * 1.609
    converted.config(text=f'{conversion}')


# calculate button
calculate = Button(text='Calculate', command=convert)
calculate.grid(column=1, row=3)


















window.mainloop()