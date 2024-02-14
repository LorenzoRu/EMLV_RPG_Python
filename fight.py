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
    hp_monster = monster[3]
    print(f"{monster[1]} vous attaque !")
    while hp_hero > 0 and hp_monster > 0:
        print("--- Infos sur le combat ---")
        textEffect(f"{player[1]} : {hp_hero}")
        textEffect(f"{monster[1]} : {hp_monster}")
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
            print("Vous fuyez le combat...")
            break
        else:
            textEffect("Nan sérieux pourtant c'est pas compliqué tu n'as que 3 choix !")
    
fight() 

