import os 
import Model.classes as classes_db
import Model.player as player_db

def init():
    WIHTE = '\033[0m'
    GREEN = '\033[92m'
    if not os.path.exists('Database/classes.db'):
        os.makedirs('Database')
        print(f"{GREEN}[INFO]{WIHTE} Le dossier Database a été créé !")
        print(f"{GREEN}[INFO]{WIHTE} La base de données a été créée !")
        classes_db.generate_classes()
        player_db.generate_player()