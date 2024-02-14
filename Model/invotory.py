import sqlite3

def generate_inventory():
    # Connexion/création à/de la base de données
    connection = sqlite3.connect('Database/inventory.db')
    # Création d'un curseur pour exécuter des requêtes
    cursor = connection.cursor()
    # Vérifier si la table inventory existe déjà
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory'")
    table_exists = cursor.fetchone()
    if not table_exists:
        # Création de la table si elle n'existe pas
        cursor.execute("""
         CREATE TABLE inventory(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT,
            quantity INTEGER
         )
    """)
        # Ajout des objets si ils n'existent pas
        items = [
            ("Or", 100),
            ("Soins", 3),
            ("Potion de force", 2),
            ("Potion de vitalité", 5)
        ]
        cursor.executemany("INSERT INTO inventory(name, quantity) VALUES(?, ?)", items)
        # Sauvegarde (commit) des modifications
        connection.commit()
    # Fermeture de la connexion
    connection.close()


