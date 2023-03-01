import tkinter as tk
from tkinter import font
from assets import JsonReader, NumConvert
import random, platform

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
    objectif_score = 1
    scoredone = 1
    thewhile = False
    exploitation_system = platform.system()

def end_test():
    print("end")
    question.destroy(), inputer0.destroy(), button1.destroy(), score_label.destroy(), end_button.destroy()
    label0.config(text="You have finish goodbye !!")
    app.update()
    import time
    time.sleep(2)
    app.destroy()
def is_number():
    try:
        text = inputer1.get()
        data.objectif_score = float(text)
        start()
    except ValueError:
        print("return False")
        return False

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
        data.score = data.score + data.scoredone
        score_label.config(text=f"Score: {data.score} / {data.objectif_score}")
        inputer0.delete(0, 'end')
        start()
    elif data.answer_player == "Error not good answer :(":
        inputer0.delete(0, 'end')
        button1.config(text="Send")
    else:
        inputer0.delete(0, 'end')
        inputer0.insert(0, "Error not good answer :(")
        button1.config(text="Ok")

def start():
    if data.buttone0 == False:
        data.buttone0 = True
        data.objectif_score = inputer1.get()
        button0.destroy()
        inputer1.destroy()
        label0.config(text="Your are on the test !")
    randoniser()
    if data.thewhile != True:
        global question
        question = tk.Label(app, text=JsonReader.readJson(toread=data.question, langue=data.langue, file=data.thetest), bg="black", fg="white", font=Ubuntu)
        question.pack(pady=20)
        global inputer0
        inputer0 = tk.Entry(app, textvariable="inputer0", font=Ubuntu)
        inputer0.pack(pady=20)
        global button1
        button1 = tk.Button(app, text="Send", command=verify, font=Ubuntu)
        button1.pack(pady=20)
        global score_label
        score_label = tk.Label(app, text=f"Score: {data.score} / {data.objectif_score}", bg="black", fg="white", font=Ubuntu)
        score_label.pack(pady=20)
        global end_button
        end_button = tk.Button(app, text="Finish", command=end_test, font=Ubuntu)
        end_button.pack(pady=20)
    elif data.thewhile == True:
        question.config(text=JsonReader.readJson(toread=data.question, langue=data.langue, file=data.thetest))
    if data.objectif_score != data.score:
        data.thewhile = True
        print(f"not objectif {data.score} / {data.objectif_score}")
    elif data.score == data.objectif_score:
        print("object good")
        data.thewhile = False
        end_test()
    app.update()

def appli():
    app.title("Culture_Test")
    app.geometry("600x600")
    app.configure(bg="black")
    if data.exploitation_system == "Windows":
        app.iconbitmap("assets/logo/logo.svg")

    global label0
    label0 = tk.Label(app, text="Welcome to Culture_Test please entry your objective of score:", bg="black", fg="white", font=Ubuntu)
    label0.pack(pady=20)
    global inputer1
    inputer1 = tk.Entry(app, textvariable="inputer_objective", font=Ubuntu)
    inputer1.pack(pady=20)
    validate_command = app.register(is_number)
    global button0
    button0 = tk.Button(app, text="Start", command=validate_command, font=Ubuntu)
    button0.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    appli()