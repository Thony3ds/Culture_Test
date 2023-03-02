import tkinter as tk
from tkinter import font
import platform, time
app = tk.Tk()
Ubuntu = font.Font(font="Ubuntu")

class data():
    size = 0
    towrite = "{"
    file_name = "test"
def create_test():
    data.file_name = inputer2.get()
    inputer2.destroy()
    button3.destroy()
    label0.config(text="Building....")
    towrite = data.towrite + f' "maxtest": "{data.size}"' + " }"
    with open(f"assets/jsons/english/{data.file_name}.json", "w+") as file:
        file.write(towrite)
        file.close()
    with open(f"assets/jsons/frensh/{data.file_name}.json", "w+") as file:
        file.write(towrite)
        file.close()
    app.geometry("800x500")
    label0.config(text="We have finish !! use assets/other/help_terminal.txt if you have problems")
    app.update()
    time.sleep(3)
    app.destroy()

def finalising():
    inputer0.destroy()
    inputer1.destroy()
    button1.destroy()
    button2.destroy()
    label0.config(text="Finalising please entry the name of the test:")
    global inputer2
    inputer2 = tk.Entry(app, textvariable="name", font=Ubuntu)
    inputer2.pack(pady=20)
    global button3
    button3 = tk.Button(app, text="Send", command=create_test, font=Ubuntu)
    button3.pack(pady=20)
def craft_question():
    entry_var = inputer0.get()
    exit_var = inputer1.get()
    data.towrite = data.towrite + f' "{entry_var}": "{exit_var}",'
    inputer0.delete(0, 'end')
    inputer1.delete(0, 'end')
    data.size = data.size + 1

def start():
    button0.destroy()
    label0.config(text="Entry the question")
    global inputer0
    inputer0 = tk.Entry(app, textvariable="entry", font=Ubuntu)
    inputer0.pack(pady=20)
    global label1
    label1 = tk.Label(app, text="Entry the answer", bg="black", fg="white", font=Ubuntu)
    label1.pack()
    global inputer1
    inputer1 = tk.Entry(app, textvariable="exit", font=Ubuntu)
    inputer1.pack(pady=20)
    global button1
    button1 = tk.Button(app, text="Create the question", command=craft_question, font=Ubuntu)
    button1.pack(pady=20)
    global button2
    button2 = tk.Button(app, text="Finalising test", command=finalising, font=Ubuntu)
    button2.pack(pady=20)

def appli():
    app.title("Culture_App_Creator")
    app.geometry("500x500")
    app.minsize(width=500, height=500)
    app.config(bg="black")
    if platform.system() == "Windows":
        app.iconbitmap("assets/logo/logo_creator.svg")

    global label0
    label0 = tk.Label(app, text="Welcome to Culture_Test Creator !!", bg="black", fg="white", font=Ubuntu)
    label0.pack(pady=20)
    global button0
    button0 = tk.Button(app, text="Start", command=start, font=Ubuntu)
    button0.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    appli()