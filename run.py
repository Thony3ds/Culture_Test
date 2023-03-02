import subprocess
var = float(input("Chose an option 1= run app 2= run create app: "))
if var == 1:
    print("run....")
    # chemin vers le script à lancer
    chemin_script = 'main_app.py'

    # lancer le script avec subprocess.run()
    subprocess.run(['python3', chemin_script])
elif var == 2:
    print("run create_app....")
    # chemin vers le script à lancer
    chemin_script = 'create_app.py'

    # lancer le script avec subprocess.run()
    subprocess.run(['python3', chemin_script])