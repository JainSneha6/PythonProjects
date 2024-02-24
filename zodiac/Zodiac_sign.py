from tkinter import *
import pyttsx3

SIGN_IMAGES = {
    "Capricorn": "zodiac/capricorn.png",
    "Aquarius": "zodiac/aquarius.png",
    "Pisces": "zodiac/pisces.png",
    "Aries": "zodiac/aries.png",
    "Taurus": "zodiac/taurus.png",
    "Gemini": "zodiac/gemini.png",
    "Cancer": "zodiac/cancer.png",
    "Leo": "zodiac/leo.png",
    "Virgo": "zodiac/virgo.png",
    "Libra": "zodiac/libra.png",
    "Scorpio": "zodiac/scorpio.png",
    "Sagittarius": "zodiac/sagittarius.png",
}

root = Tk()
root.geometry("1000x700")
root.title("Zodiac Sign")
root.config(bg="#091329")

month_var = StringVar()
date_var = StringVar()

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def determine_zodiac(month, date):
    zodiac_map = {
        "january": ("Capricorn", 19),
        "february": ("Aquarius", 18),
        "march": ("Pisces", 20),
        "april": ("Aries", 19),
        "may": ("Taurus", 20),
        "june": ("Gemini", 18),
        "july": ("Cancer", 22),
        "august": ("Leo", 22),
        "september": ("Virgo", 22),
        "october": ("Libra", 22),
        "november": ("Scorpio", 21),
        "december": ("Sagittarius", 21),
    }
    month = month.lower()
    if month in zodiac_map:
        sign, boundary = zodiac_map[month]
        if date <= boundary:
            return sign
        else:
            months = list(zodiac_map.keys())
            next_month = months[(months.index(month) + 1) % len(months)]
            return zodiac_map[next_month][0]

def display_zodiac():
    month = month_var.get()
    date = int(date_var.get())
    sign = determine_zodiac(month, date)
    if sign:
        speak(f'Your Zodiac Sign is {sign}')
        display_sign_image(sign)
    else:
        print("Invalid date or month")

def display_sign_image(sign):
    frame = Frame(root, bg="#091329", height=350, width=1000)
    frame.place(y=350)
    image = PhotoImage(file=SIGN_IMAGES[sign])
    image_label = Label(frame, image=image)
    image_label.image = image
    image_label.place(x=600, y=60)
    text = f"Your Zodiac Sign is {sign.upper()}!"
    text_label = Label(frame, text=text, font="comicsans 25 bold", bg="#091329", fg="white")
    text_label.place(x=30, y=20)

# Header Frame
header_frame = Frame(root, bg='#091329', height=60)
header_frame.pack(fill=X, padx=10, pady=10)
header_label = Label(header_frame, text="ZODIAC SIGN", font="comicsans 40 bold", bg='#091329', fg="white")
header_label.pack(pady=10)

# Month Entry
month_label = Label(root, justify="center", text="Enter your Birth Month", fg="white", font="comicsans 20 bold", bg="#091329")
month_label.place(x=100, y=120)
month_text = Entry(root, justify="center", width=20, font="Arial 18", border=0, bg="#000C7B", fg="white", bd=4, textvariable=month_var)
month_text.place(x=600, y=120)

# Date Entry
date_label = Label(root, justify="center", text="Enter your Birth Date", fg="white", font="comicsans 20 bold", bg="#091329")
date_label.place(x=100, y=180)
date_text = Entry(root, justify="center", width=20, font="Arial 18", border=0, bg="#000C7B", fg="white", bd=4, textvariable=date_var)
date_text.place(x=600, y=180)

# Submit Button
submit_button = Button(root, text="Submit", font="Arial 16", cursor="hand2", bg="#000C7B", fg="white", width=15, command=display_zodiac)
submit_button.config(width=10, height=1)
submit_button.place(x=430, y=280)

root.mainloop()

