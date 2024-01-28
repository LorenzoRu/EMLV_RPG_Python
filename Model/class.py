import sqlite3

# Connexion/création à/de la base de données
connection = sqlite3.connect('Database/classes.db')

# Création d'un curseur pour exécuter des requêtes
cursor = connection.cursor()

# Création de la table si elle n'existe pas
cursor.execute("""
     CREATE TABLE IF NOT EXISTS classes(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        spell1 TEXT,
        spell2 TEXT,
        ultimate TEXT
     )
""")
# Ajout des classes si elles n'existent pas
check = ["Chevalier", "Mage", "Assassin", "Archer"]
for classe in check:
    cursor.execute("SELECT * FROM classes WHERE name=?", (classe,))
    check = cursor.fetchone()
if check is None:
    cursor.execute("INSERT INTO classes(name,spell1, spell2, ultimate) VALUES(?, ?, ?, ?)", ("Mage", "Boule de feu", "Gel", "Météore"))
    cursor.execute("INSERT INTO classes(name,spell1, spell2, ultimate) VALUES(?, ?, ?, ?)", ("Chevalier", "Bouclier", "Charge", "Coup de grâce"))
    cursor.execute("INSERT INTO classes(name,spell1, spell2, ultimate) VALUES(?, ?, ?, ?)", ("Assassin", "Invisibilité", "Poison", "Assassinat"))
    cursor.execute("INSERT INTO classes(name,spell1, spell2, ultimate) VALUES(?, ?, ?, ?)", ("Archer", "Flèche", "Flèche empoisonnée", "Flèche explosive"))

# Sauvegarde (commit) des modifications
connection.commit()
connection.close()
