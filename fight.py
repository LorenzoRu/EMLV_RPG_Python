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
monster = random_monster()

def open_inventory():
    print(f"--- Inventaire de {player[1]} ---")
    for item in list_inventory:
        textEffect(f"[{item[0]}] {item[1]} : {item[2]}")

def fight():
    textEffect(f"{monster[1]} vous attaque !")

fight()
