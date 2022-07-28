import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import tkinter as tk
from PIL import Image, ImageTk

listener = sr.Recognizer()
listener.energy_threshold = 4000
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            instruction = listener.recognize_google(voice)
    except LookupError:
        print("Speech not understood")
    return instruction


def run_robot():
    try:
        user_command = take_command()
        if 'robot' in user_command:
            user_command = user_command.replace('robot', '')
            if 'play' in user_command:
                playcommand = user_command.replace('play', '')
                speak("I am playing" + playcommand)
                print("I am playing" + playcommand)
                pywhatkit.playonyt(playcommand)
            if 'time' in user_command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is now' + time)
                print(time)
            else:
                speak('Please say it again')
    except:
        pass

root = tk.Tk()
root.title('Voice assistant Sylvia')
im = ImageTk.PhotoImage(Image.open("back.jpg").resize((800, 600)))
canvas = tk.Canvas(root, width=300, height=500)
canvas.pack()  # place(), etc.
Canvas_Image = canvas.create_image(0, 0, image=im, anchor="nw")
btn = tk.Button(root, text="this is a button", command=run_robot)

# Set the position of button on the top of window
btn.pack(side='top')
root.mainloop()
