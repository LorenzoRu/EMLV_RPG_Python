import sqlite3
from style import textEffect
def connect_classes():
    connection = sqlite3.connect('Database/classes.db')
    # Création d'un curseur pour exécuter des requêtes
    cursor = connection.cursor()
    return cursor
    # Fontion pour afficher les classes

def nameClasses(cursor):
    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()
    for classe in classes:
        textEffect(classe[1])

def classesSelector(cursor):
    cursor.execute("SELECT * FROM classes")
    classes = cursor.fetchall()
    classes_dictionary = {}
    for classe in classes:
         classes_dictionary[classe[0]] = classe[1]
    return classes_dictionary

def savePlayer(username, choice):
    connection = sqlite3.connect('Database/player.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO player(name, class) VALUES(?, ?)", (username, choice))
    connection.commit()
    connection.close()
    textEffect(f"Félécitations {username} ! Tu es maintenant {choice} !")

def getPlayer(cursor):
    connection = sqlite3.connect('Database/player.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM player")
    player = cursor.fetchone()
    connection.close()
    return player

