import sqlite3

def generate_monsters():
    # Connexion/création à/de la base de données
    connection = sqlite3.connect('Database/monsters.db')
    # Création d'un curseur pour exécuter des requêtes
    cursor = connection.cursor()
    # Création de la table si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monsters(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE,
            attack INTEGER,
            pv INTEGER
        )
    """)

    # Ajout des classes si elles n'existent pas
    monster_names = ["Loup Démonique", "Gargouille", "Hydre", "Sphinx Noir"]
    for monster in monster_names:
        cursor.execute("SELECT * FROM monsters WHERE name=?", (monster,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO monsters(name, attack, pv) VALUES(?, ?, ?)", ("Loup Démonique", 50, 100))
            cursor.execute("INSERT INTO monsters(name, attack, pv) VALUES(?, ?, ?)", ("Gargouille", 10, 50))
            cursor.execute("INSERT INTO monsters(name, attack, pv) VALUES(?, ?, ?)", ("Hydre", 7, 75))
            cursor.execute("INSERT INTO monsters(name, attack, pv) VALUES(?, ?, ?)", ("Sphinx Noir", 5, 90))
            
    # Sauvegarde (commit) des modifications
    connection.commit()
    connection.close()
