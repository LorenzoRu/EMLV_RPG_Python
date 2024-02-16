import sqlite3

def generate_player():
    # Connexion/création à/de la base de données
    connection = sqlite3.connect('Database/player.db')
    # Création d'un curseur pour exécuter des requêtes
    cursor = connection.cursor()
    # Création de la table si elle n'existe pas
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS player(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        class TEXT
     )
""")
    # Sauvegarde (commit) des modifications
    connection.commit()
    connection.close()