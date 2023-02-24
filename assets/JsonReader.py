import json
def language_load():
    file = open("assets/jsons/langue.txt", "r")
    infile = file.readlines()
    file.close()
    if "english" in infile:
        langue = "english"
    elif "frensh" in infile:
        langue = "frensh"
    else:
        langue = "error"
        print("error")
    return langue

def readJson(toread, langue, file):
    if langue == "english":
        filetoread = f"assets/jsons/english/{file}.json"
    elif langue == "frensh":
        filetoread = f"assets/jsons/frensh/{file}.json"
    else:
        filetoread = f"assets/jsons/english/{file}.json"
    with open(filetoread) as f:
        injson = json.load(f)

    toreturn = injson[toread]
    return toreturn