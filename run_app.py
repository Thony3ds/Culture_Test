import tkinter as tk
from tkinter import font
from assets import JsonReader, NumConvert
import random

app = tk.Tk()
Ubuntu = font.Font(font="Ubuntu")

class data():
    langue = JsonReader.language_load()
    thetest = "default"
    answer_player = ""
    answer = ""
    question = "1a"
    buttone0 = False
    score = 0
    scoredone = 1
    thewhile = False

def randoniser():
    var = random.randint(1, 2)
    var = NumConvert.text_convert(var)
    var2 = var
    var2 = var2 + "b"
    var = var + "a"
    data.question = var
    data.answer = JsonReader.readJson(toread=var2, langue=data.langue, file=data.thetest)
    return True

def verify():
    data.answer_player = inputer0.get()
    if data.answer == data.answer_player:
        print("Good answer")
        data.score = data.score + data.scoredone
        start()
    else:
        print("error")
        print(f"your answer: {data.answer_player}")

def start():
    if data.buttone0 == False:
        data.buttone0 = True
        button0.destroy()
    randoniser()
    if data.thewhile != True:
        global question
        question = tk.Label(app, text=JsonReader.readJson(toread=data.question, langue=data.langue, file=data.thetest), bg="black", fg="white", font=Ubuntu)
        question.pack(pady=20)
        global inputer0
        inputer0 = tk.Entry(app, textvariable="inputer0", font=Ubuntu)
        inputer0.pack(pady=20)
        button1 = tk.Button(app, text="Send", command=verify, font=Ubuntu)
        button1.pack(pady=20)
    elif data.thewhile == True:
        question.config(text=JsonReader.readJson(toread=data.question, langue=data.langue, file=data.thetest))
    data.thewhile = True
    app.update()

def appli():
    app.title("Culture_Test")
    app.geometry("600x600")
    app.configure(bg="black")

    label0 = tk.Label(app, text="Welcome to Culture_Test", bg="black", fg="white", font=Ubuntu)
    label0.pack(pady=20)
    global button0
    button0 = tk.Button(app, text="Start", command=start, font=Ubuntu)
    button0.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    appli()