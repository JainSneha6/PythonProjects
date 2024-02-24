from tkinter import *
import pyttsx3

month=""
date=""
sign=""
root=Tk()

root.geometry("1000x700")
root.title("Zodiac Sign")
root.config(bg="#091329")

month_var=StringVar()
date_var=StringVar()

capricorn=PhotoImage(file=r"zodiac\capricorn.png")
aquarius=PhotoImage(file=r"zodiac\aquarius.png")
pisces=PhotoImage(file=r"zodiac\pisces.png")
aries=PhotoImage(file=r"zodiac\aries.png")
taurus=PhotoImage(file=r"zodiac\taurus.png")
gemini=PhotoImage(file=r"zodiac\gemini.png")
cancer=PhotoImage(file=r"zodiac\cancer.png")
leo=PhotoImage(file=r"zodiac\leo.png")
virgo=PhotoImage(file=r"zodiac\virgo.png")
libra=PhotoImage(file=r"zodiac\libra.png")
scorpio=PhotoImage(file=r"zodiac\scorpio.png")
sagittarius=PhotoImage(file=r"zodiac\sagitarus.png")


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def zodiac():
    global month,date,sign
    month=month_var.get()
    date=date_var.get()
    month=month.lower()
    date=int(date)
    if 0 < date <= 31:
        if month == "january":
            if date <= 19:
                sign = "Capricorn"
            else:
                sign = "Aquarius"
        elif month == "february":
            if date <= 18:
                sign = "Aquarius"
            else:
                sign = "Pisces"
        elif month == "march":
            if date <= 20:
                sign = "Pisces"
            else:
                sign = "Aries"
        elif month == "april":
            if date <= 19:
                sign = "Aries"
            else:
                sign = "Taurus"
        elif month == "may":
            if date <= 20:
                sign = "Taurus"
            else:
                sign = "Gemini"
        elif month == "june":
            if date <= 18:
                sign = "Gemini"
            else:
                sign = "Cancer"
        elif month == "july":
            if date <= 22:
                sign = "Cancer"
            else:
                sign = "Leo"
        elif month == "august":
            if date <= 22:
                sign = "Leo"
            else:
                sign = "Virgo"
        elif month == "september":
            if date <= 22:
                sign = "Virgo"
            else:
                sign = "Libra"
        elif month == "october":
            if date <= 22:
                sign = "Libra"
            else:
                sign = "Scorpio"
        elif month == "november":
            if date <= 21:
                sign = "Scorpio"
            else:
                sign = "Sagittarius"
        elif month == "december":
            if date <= 21:
                sign = "Sagittarius"
            else:
                sign = "Capricorn"

    frame = Frame(root, bg="#091329", height=350, width=1000)
    frame.place(y=350)

    if sign == "Capricorn":
        image=Label(frame,image=capricorn)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is CAPRICORN!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Aquarius":
        image=Label(frame,image=aquarius)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is AQUARIUS!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Pisces":
        image=Label(frame,image=pisces)
        image.place(x=650,y=60)
        text1=Label(frame,text="Your Zodiac Sign is PISCES!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Aries":
        image=Label(frame,image=aries)
        image.place(x=650,y=60)
        text1=Label(frame,text="Your Zodiac Sign is ARIES!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Taurus":
        image=Label(frame,image=taurus)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is TAURUS!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Gemini":
        image=Label(frame,image=gemini)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is GEMINI!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Cancer":
        image=Label(frame,image=cancer)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is CANCER!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Leo":
        image=Label(frame,image=leo)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is LEO!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Virgo":
        image=Label(frame,image=virgo)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is VIRGO!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Libra":
        image=Label(frame,image=libra)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is LIBRA!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Scorpio":
        image=Label(frame,image=scorpio)
        image.place(x=700,y=60)
        text1=Label(frame,text="Your Zodiac Sign is SCORPIO!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    elif sign == "Sagittarius":
        image=Label(frame,image=sagittarius)
        image.place(x=650,y=60)
        text1=Label(frame,text="Your Zodiac Sign is SAGITTARIUS!", font="comicsans 25 bold", bg="#091329", fg="white")
        text1.place(x=30,y=20)
    speak(f'Your Zodiac Sign is {sign}')


header_frame = Frame(root, bg='#091329', height=60)
header_frame.pack(fill=X, padx=10, pady=10)

header_label=Label(header_frame, text="ZODIAC SIGN", font="comicsans 40 bold", bg='#091329', fg="white")
header_label.pack(pady=10)

month_label=Label(root, justify="center", text="Enter your Birth Month", fg="white", font="comicsans 20 bold", bg="#091329")
month_label.place(x=100, y=120)

month_text=Entry(root,justify="center",width=20,font="Arial 18",border=0,bg="#000C7B",fg="white",bd=4,textvariable=month_var)
month_text.place(x=600, y=120)

date_label=Label(root, justify="center", text="Enter your Birth Date", fg="white", font="comicsans 20 bold", bg="#091329")
date_label.place(x=100, y=180)

date_text=Entry(root,justify="center",width=20,font="Arial 18",border=0,bg="#000C7B",fg="white",bd=4,textvariable=date_var)
date_text.place(x=600, y=180)

submit_button=Button(root, text="Submit", font="Arial 16", cursor="hand2", bg="#000C7B", fg="white", width=15, command=zodiac)
submit_button.config(width=10, height=1)
submit_button.place(x=430,y=280)

root.mainloop()