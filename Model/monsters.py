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
            mana INTEGER
        )
    """)

    # Ajout des classes si elles n'existent pas
    monster_names = ["Loup Démonique", "Gargouille", "Hydre", "Sphinx Noir"]
    for monster in monster_names:
        cursor.execute("SELECT * FROM monsters WHERE name=?", (monster,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO monsters(name, attack, mana) VALUES(?, ?, ?)", (monster, 100, 50)) 
    # Sauvegarde (commit) des modifications
    connection.commit()
    connection.close()
