import sqlite3

def generate_classes():
    # Connexion/création à/de la base de données
    connection = sqlite3.connect('Database/classes.db')

    # Création d'un curseur pour exécuter des requêtes
    cursor = connection.cursor()

    # Création de la table si elle n'existe pas
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS classes(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        hp INTEGER,
        attack INTEGER
     )
    """)

    # Ajout des classes si elles n'existent pas
    check = ["Chevalier", "Mage", "Assassin", "Archer"]
    for classe in check:
        cursor.execute("SELECT * FROM classes WHERE name=?", (classe,))
        check = cursor.fetchone()
        if check is None:
            cursor.execute("INSERT INTO classes(name, hp, attack) VALUES(?, ?, ?)", ("Chevalier", 100, 500))
            cursor.execute("INSERT INTO classes(name, hp, attack) VALUES(?, ?, ?)", ("Mage", 1, 100))
            cursor.execute("INSERT INTO classes(name, hp, attack) VALUES(?, ?, ?)", ("Assassin", 75, 75))
            cursor.execute("INSERT INTO classes(name, hp, attack) VALUES(?, ?, ?)", ("Archer", 75, 75))
    
    # Sauvegarde (commit) des modifications
    connection.commit()
    connection.close()

