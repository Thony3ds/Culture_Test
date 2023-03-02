import os, run_app

def whileSession():
    running = True
    while running:
        command = input("Culture_Test/terminal: ")
        if command == "help":
            print("please see: 'assets/other/help_terminal.txt' for all commands") # to parametre
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
            test = input("entry the name of the test")
            test = test + ".json"
            if os.path.exists(f"assets/jsons/{run_app.data.langue}/{test}") == True:
                print("change test file")
                run_app.data.thetest = test
            else:
                print(f"error no found {test} file")
        else:
            print(f"error we can read the command {command} please write 'help' to receved some help")

def startSession():
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
            whileSession()
        else:
            print("Error on file system")
            print(f"the system return: {infile}")
    else:
        file = open("assets/terminal_assets/autostart.txt", "w+")
        file.write("False")
        file.close()
        startSession()