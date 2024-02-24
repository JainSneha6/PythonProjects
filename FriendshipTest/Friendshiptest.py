from tkinter import *
from aboutyourself import database1
from aboutfrnd import database2
import pyttsx3


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


root = Tk()

root.geometry("800x600")
root.title("Friendship Test")
root.config(bg='black')

database1_dict = database1()
database2_dict = database2()

color1 = database1_dict.get("color")
color2 = database2_dict.get("color")

birthdate1 = database1_dict.get("birthdate")
birthdate2 = database2_dict.get("birthdate")

movie1 = database1_dict.get("movie")
movie2 = database2_dict.get("movie")

hobby1 = database1_dict.get("hobby")
hobby2 = database2_dict.get("hobby")

destination1 = database1_dict.get("destination")
destination2 = database2_dict.get("destination")

flag=0

header_frame = Frame(root, bg='goldenrod1', height=60)
header_frame.pack(fill=X, padx=10, pady=10)

header_label = Label(header_frame, text="Friendship Test", font="Arial 30 bold", bg='goldenrod1', fg="black")
header_label.pack(pady=10)

form_frame = Frame(root, bg='goldenrod1')
form_frame.pack(padx=50, pady=30)

if color1.lower() == color2.lower():
    Label(form_frame, text="You Guessed The Color Right!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)
    flag+=1
else:
    Label(form_frame, text="You Guessed The Color Wrong!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)

if birthdate1.lower() == birthdate2.lower():
    Label(form_frame, text="You Guessed The Birthdate Right!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)
    flag+=1
else:
    Label(form_frame, text="You Guessed The Birthdate Wrong!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)

if movie1.lower() == movie2.lower():
    Label(form_frame, text="You Guessed The Movie Right!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)
    flag+=1
else:
    Label(form_frame, text="You Guessed The Movie Wrong!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)

if hobby1.lower() == hobby2.lower():
    Label(form_frame, text="You Guessed The Hobby Right!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)
    flag+=1
else:
    Label(form_frame, text="You Guessed The Hobby Wrong!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)

if destination1.lower() == destination2.lower():
    Label(form_frame, text="You Guessed The Destination Right!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)
    flag+=1
else:
    Label(form_frame, text="You Guessed The Destination Wrong!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)

footer_frame = Frame(root, bg='goldenrod1', height=60)
footer_frame.pack(fill=X, padx=10, pady=10)

Label(footer_frame, text=f'Your score: {flag}', font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10, pady=10)

if flag==0:
    Label(footer_frame, text="Are you even friends?", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10,pady=10)
    speak("Are you even friends?")
elif flag==1 or flag==2:
    Label(footer_frame, text="Try to know your friend more!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10,pady=10)
    speak("Try to know your friend more!")
elif flag==3:
    Label(footer_frame, text="Nice try!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10,pady=10)
    speak("Nice try!")
elif flag==4:
    Label(footer_frame, text="Played Pretty Well!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10,pady=10)
    speak("Played Pretty Well!")
elif flag==5:
    Label(footer_frame, text="You guys are Best Friends!", font="comicsans 20 bold", bg="goldenrod1", fg="black").pack(padx=10,pady=10)
    speak("You guys are Best Friends!")
root.mainloop()

