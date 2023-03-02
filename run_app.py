import tkinter as tk
from tkinter import font
from assets import JsonReader, NumConvert
import random, platform, os, time

app = tk.Tk()
Ubuntu = font.Font(font="Ubuntu")

class data():
    langue = JsonReader.language_load()
    thetest = "default"
    maxtest = float(JsonReader.readJson(toread="maxtest", langue=langue, file=thetest))
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
    var = random.randint(1, float(data.maxtest))
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
    elif data.score == data.objectif_score:
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

class TerminalCommand():

    def whileSession(self):
        running = True
        while running:
            command = input("Culture_Test/terminal: ")
            if command == "help":
                print("please see: 'assets/other/help_terminal.txt' for all commands")
            elif command == "run":
                running = False
                print("Start Culture_Test....")
            elif command == "autorun":
                autorun = input("please chose your autorun mod True/False: ")
                if autorun != "True" and autorun != "False":
                    print(f"error on the answer: {autorun}")
                else:
                    file = open("assets/terminal_assets/autostart.txt", "w")
                    file.write(autorun)
                    file.close()
                    print(f"finish to change the autorun's mod with {autorun} mod")
                    if autorun == "True":
                        print("for start use 'run' command :)")
            elif command == "lang":
                lang = input("Chose your language/Choisis ta langue english/frensh: ")
                if lang == "english" or lang == "frensh":
                    file = open("assets/jsons/langue.txt", "w")
                    file.write(lang)
                    file.close()
                    print(f"pass to {lang} mod succefuly !! (you need to restart the app to have {lang} mod)")
                else:
                    print(f"error !! no find {lang} on language packages.")
            elif command == "test":
                test = input("entry the name of the test: ")
                test2 = test + ".json"
                if os.path.exists(f"assets/jsons/{data.langue}/{test2}") == True:
                    print(f"change test file to {test} test")
                    data.thetest = test
                    data.maxtest = float(JsonReader.readJson(toread="maxtest", langue=data.langue, file=data.thetest))
                else:
                    print(f"error no found {test} file")
            else:
                print(f"error we can read the command {command} please write 'help' to receved some help")

    def startSession(self):
        print("initalisation....")
        print("Welcome !!")
        if os.path.exists(path="assets/terminal_assets/autostart.txt") == True:
            file = open("assets/terminal_assets/autostart.txt", "r")
            infile = file.readlines()
            file.close()
            if infile == ['True']:
                return True
            elif infile == ['False']:
                print("starting terminal....")
                TerminalCommand.whileSession(self=self)
            else:
                print("Error on file system")
                print(f"the system return: {infile}")
        else:
            file = open("assets/terminal_assets/autostart.txt", "w+")
            file.write("False")
            file.close()
            TerminalCommand.startSession(self=self)

if __name__ == "__main__":
    TerminalCommand.startSession(self="self")
    appli()