import random
import sqlite3

from style import textEffect


def player():
    connection = sqlite3.connect('Database/player.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM player ORDER BY id DESC LIMIT 1")
    player = cursor.fetchone()
    connection.close()
    return player


def list_inventory():
    connection = sqlite3.connect('Database/inventory.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    connection.close()
    return inventory


def random_monster():
    connection = sqlite3.connect('Database/monsters.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM monsters ORDER BY RANDOM() LIMIT 1")
    monster = cursor.fetchone()
    connection.close()
    return monster


player = player()
list_inventory = list_inventory()


def list_stats():
    key = player[2]
    connection = sqlite3.connect('Database/classes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM classes WHERE name=?", (key,))
    stats = cursor.fetchone()
    connection.close()
    return stats
stats = list_stats()

def open_inventory():
    print(f"--- Inventaire de {player[1]} ---")
    for item in list_inventory:
        textEffect(f"[{item[0]}] {item[1]} : {item[2]}")



def fight():
    monster = random_monster()
    hp_hero = stats[2]
    attack_hero = stats[3]
    attack_monster = monster[2]
    hp_monster = monster[3]
    print(f"{monster[1]} vous attaque !")
    while hp_hero > 0 and hp_monster > 0:
        print("--- Infos sur le combat ---")
        textEffect(f"{player[1]} : \n PV :{hp_hero} \n ATK : {attack_hero}")
        textEffect(f"{monster[1]} : \n PV :{hp_monster} \n ATK : {attack_monster}")
        print("---------------------------")
        textEffect("Que voulez-vous faire ?")
        textEffect("[1] Attaquer")
        textEffect("[2] Utiliser un objet")
        textEffect("[3] Fuir")
        choice = input()
        if choice == "1":
            print(f"Vous attaquez {monster[1]} !")
            break
        elif choice == "2":
            open_inventory()
            textEffect("Quel objet voulez-vous utiliser ?")
            item_choice = input()
            item_found = False
            for item in list_inventory:
                if item_choice == str(item[0]):
                    item_found = True
                    while True:
                        if item_choice == "1":
                            textEffect("Vous essayer de corrompre votre opposant avec votre fortune mais rien ne se passe !")
                            textEffect("Quel objet voulez-vous utiliser ?")
                            item_choice = input()
                        elif item_choice == "2":
                            print("2")
                            break
                        elif item_choice == "3": 
                            textEffect(f"Vous utlilisez {item[2]}, en suivant les précaution de votre druide préféré votre attack augmente de 5")
                            connection = sqlite3.connect('Database/classes.db')
                            cusor = connection.cursor()
                            cusor.execute("UPDATE classes SET  attack = attack + 5 WHERE id=?", (player[2],))
                            break
                        elif item_choice == "4":
                            print("4")
                            break
                        else:
                            textEffect("Quel objet voulez-vous utiliser ?")
                            textEffect("Tu es créatif mais je ne suis pas sûr que cette qualité t'aide")
                            textEffect("Quel objet voulez-vous utiliser ?")
                            item_choice = input()
            if not item_found:
                textEffect("Cet objet n'est pas dans votre inventaire !")
        elif choice == "3":
            print("Vous fuyez le combat...")
            break
        else:
            textEffect("Nan sérieux pourtant c'est pas compliqué tu n'as que 3 choix !")
    
fight() 

