import os, shutil
from git import Repo

def exctraction():
    print("start....")
    file_analyse = os.path.dirname(os.path.abspath(__file__)) + "/Culture_Test_Extentions/extentions_download"
    try :
        print("start exctracting....")
        source_folder = file_analyse
        destination_folder = os.path.dirname(os.path.abspath(__file__))

        shutil.move(source_folder, destination_folder)
        print("extract succeful finalising....")
        dossier_a_supprimer = "Culture_Test_Extentions"

        shutil.rmtree(dossier_a_supprimer)
        print("Finish")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    repo_url = "https://github.com/Thony3ds/Culture_Test_Extentions"
    repo_dir = os.path.dirname(os.path.abspath(__file__)) + "/Culture_Test_Extentions"
    Repo.clone_from(repo_url, repo_dir)
    print("File found and download. Extracting....")
    exctraction()