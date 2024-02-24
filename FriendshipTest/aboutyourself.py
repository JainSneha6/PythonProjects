from tkinter import *

root = Tk()

root.geometry("800x600")
root.title("Friendship Test")
root.config(bg='black')

color_var=StringVar()
birthdate_var=StringVar()
movie_var=StringVar()
hobby_var=StringVar()
destination_var=StringVar()


def database1():
    data={
        "color": color_var.get(),
        "birthdate": birthdate_var.get(),
        "movie": movie_var.get(),
        "hobby": hobby_var.get(),
        "destination": destination_var.get()
    }
    return data;


def form():

    header_frame = Frame(root, bg='goldenrod1', height=60)
    header_frame.pack(fill=X, padx=10, pady=10)

    header_label = Label(header_frame, text="Friendship Test", font="Arial 30 bold", bg='goldenrod1', fg="black")
    header_label.pack(pady=10)

    form_frame = Frame(root, bg='goldenrod1')
    form_frame.pack(padx=50, pady=30)

    color_label = Label(form_frame, text="1. Your favorite color", font="Arial 16", bg='goldenrod1', fg="black",
                        anchor="w")
    color_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    color_entry = Entry(form_frame, font="Arial 16", width=30, bd=3,textvariable=color_var)
    color_entry.grid(row=0, column=1, padx=10, pady=10)

    birthdate_label = Label(form_frame, text="2. Your birthdate", font="Arial 16", bg='goldenrod1', fg="black",
                            anchor="w")
    birthdate_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    birthdate_entry = Entry(form_frame, font="Arial 16", width=30, bd=3,textvariable=birthdate_var)
    birthdate_entry.grid(row=1, column=1, padx=10, pady=10)

    movie_label = Label(form_frame, text="3. Your favorite movie", font="Arial 16", bg='goldenrod1', fg="black",
                        anchor="w")
    movie_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    movie_entry = Entry(form_frame, font="Arial 16", width=30, bd=3,textvariable=movie_var)
    movie_entry.grid(row=2, column=1, padx=10, pady=10)

    hobby_label = Label(form_frame, text="4. Your hobby", font="Arial 16", bg="goldenrod1", fg="black", anchor="w")
    hobby_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    hobby_entry = Entry(form_frame, font="Arial 16", width=30, bd=3,textvariable=hobby_var)
    hobby_entry.grid(row=3, column=1, padx=10, pady=10)

    destination_label = Label(form_frame, text="5. Your favorite destination", font="Arial 16", bg='goldenrod1',
                              fg="black", anchor="w")
    destination_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    destination_entry = Entry(form_frame, font="Arial 16", width=30, bd=3,textvariable=destination_var)
    destination_entry.grid(row=4, column=1, padx=10, pady=10)

    submit_button = Button(root, text="Submit", font="Arial 16", cursor="hand2", bg="goldenrod1", fg="black", width=15, command=database1)
    submit_button.pack(pady=30)
    submit_button.config(width=10, height=1)

form()
root.mainloop()


