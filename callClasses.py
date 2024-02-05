import sqlite3
from style import textEffect
# Connexion à la BDD
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
