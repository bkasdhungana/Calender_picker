from tkinter import *
import calendar
import time

# Function


def text():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)


def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)


root = Tk()
root.geometry("400x300")
root.title("Calendar")
root.resizable(height=False, width=False)

# Creating Labels
label1 = Label(root, text="Month:")
label1.grid(row=0, column=0)

label2 = Label(root, text="Year:")
label2.grid(row=0, column=1)

# Creating spinbox
month = Spinbox(root, from_=1, to=12, width=10)
month.grid(row=1, column=0, padx=5)

year = Spinbox(root, from_=2000, to=2100, width=10)
year.grid(row=1, column=1, padx=10)

# Creating Button
button = Button(root, text="Go", command=text)
button.grid(row=1, column=2, padx=10)

clock = Label(root, font=("times", 20, "bold"), bg="white")
clock.grid(row=1, column=3, pady=25, padx=10)
times()

# Creating Textfield
textfield = Text(root, width=30, height=50, fg="red")
textfield.grid(row=2, columnspan=2)


root.mainloop()