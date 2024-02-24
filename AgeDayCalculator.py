from tkinter import *
import datetime
from datetime import date

root = Tk()
root.geometry("1000x700")
root.title("Age and Day Calculator")
root.config(bg="#F4ECF7")

name_var = StringVar()
year_var = StringVar()
month_var = StringVar()
date_var = StringVar()


def calculate_age_and_day():
    global name, year, month, day
    name = name_var.get()
    year = year_var.get()
    month = month_var.get()
    day = date_var.get()

    year = int(year)
    month = datetime.datetime.strptime(month, "%B").month
    day = int(day)

    # Age calculation
    user_date = date(year, month, day)
    my_date = date.today()
    age = (my_date - user_date).days // 365

    # Day of the week calculation
    dob = f"{year}-{month:02d}-{day:02d}"
    user_date = datetime.datetime.strptime(dob, "%Y-%m-%d")
    day_of_week = user_date.weekday()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_name = days[day_of_week]

    # Displaying results
    age_frame = Frame(root, bg="#F4ECF7", height=50, width=1000)
    age_frame.place(y=450)
    age_text = f"{name}, Your Age is {age} Years!"
    age_label = Label(root, text=age_text, font=("Helvetica", 25), bg="#F4ECF7", fg="#8E44AD")
    age_label.place(x=270, y=480)

    day_frame = Frame(root, bg="#F4ECF7", height=50, width=1000)
    day_frame.place(y=520)
    day_text = f"You were born on a {day_name}!"
    day_label = Label(root, text=day_text, font=("Helvetica", 25), bg="#F4ECF7", fg="#8E44AD")
    day_label.place(x=270, y=550)


header_frame = Frame(root, bg='#F4ECF7', height=60)
header_frame.pack(fill=X, padx=10, pady=10)
header_label = Label(header_frame, text="Age and Day Calculator", font=("Helvetica", 40), bg='#F4ECF7', fg="#8E44AD")
header_label.pack(pady=10)

name_label = Label(root, justify="center", text="Name: ", fg="#8E44AD", font=("Helvetica", 20), bg="#F4ECF7")
name_label.place(x=100, y=120)
name_text = Entry(root, justify="center", width=20, font=("Helvetica", 18), border=0, bg="#D7BDE2", fg="#8E44AD", bd=4,
                  textvariable=name_var)
name_text.place(x=600, y=120)

year_label = Label(root, justify="center", text="Birth Year: ", fg="#8E44AD", font=("Helvetica", 20), bg="#F4ECF7")
year_label.place(x=100, y=180)
year_text = Entry(root, justify="center", width=20, font=("Helvetica", 18), border=0, bg="#D7BDE2", fg="#8E44AD", bd=4,
                  textvariable=year_var)
year_text.place(x=600, y=180)

month_label = Label(root, justify="center", text="Birth Month: ", fg="#8E44AD", font=("Helvetica", 20), bg="#F4ECF7")
month_label.place(x=100, y=240)
month_text = Entry(root, justify="center", width=20, font=("Helvetica", 18), border=0, bg="#D7BDE2", fg="#8E44AD", bd=4,
                   textvariable=month_var)
month_text.place(x=600, y=240)

date_label = Label(root, justify="center", text="Birth Date: ", fg="#8E44AD", font=("Helvetica", 20), bg="#F4ECF7")
date_label.place(x=100, y=300)
date_text = Entry(root, justify="center", width=20, font=("Helvetica", 18), border=0, bg="#D7BDE2", fg="#8E44AD", bd=4,
                  textvariable=date_var)
date_text.place(x=600, y=300)

submit_button = Button(root, text="Submit", font=("Helvetica", 16), cursor="hand2", bg="#8E44AD", fg="#F4ECF7",
                       width=15, command=calculate_age_and_day)
submit_button.config(width=10, height=1)
submit_button.place(x=400, y=380)

root.mainloop()


