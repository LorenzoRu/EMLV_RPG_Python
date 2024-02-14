import random
from basepartie import initialiser_base_de_donnees, enregistrer_resultat_partie, afficher_stats_parties


    def utiliser_composant(self, composant):
        if composant in self.inventaire and self.inventaire[composant] > 0:
            print("Vous utilisez un(e) {}.".format(composant))
            self.inventaire[composant] -= 1
            print("{} restant(e)(s) : {}".format(composant, self.inventaire[composant]))
        else:
            print("Vous n'avez pas de {}.".format(composant))

    def attaquer(self, ennemi):
        degats_infliges = random.randint(5, 15)
        ennemi["points_de_vie"] -= degats_infliges
        print("Vous attaquez l'ennemi et lui infligez {} points de dégâts.".format(degats_infliges))

    def fuir(self):
        chance_reussite = random.randint(1, 10)
        if chance_reussite <= 5:
            print("Vous parvenez à fuir avec succès.")
            return True
        else:
            print("La fuite a échoué. Préparez-vous au combat.")
            return False

def combat(joueur, ennemi, resultat):
    print("Combat contre un ennemi!")

    while joueur.points_de_vie > 0 and ennemi["points_de_vie"] > 0:
        print("\n{} - Points de vie : {}".format(joueur.nom, joueur.points_de_vie))
        print("Ennemi - Points de vie : {}".format(ennemi["points_de_vie"]))

        print("\n1. Attaquer")
        print("2. Consulter l'inventaire")
        print("3. Fuir")

        choix = input("Que voulez-vous faire? ")

        if choix == "1":
            joueur.attaquer(ennemi)
        elif choix == "2":
            joueur.consulter_inventaire()
            gestion_inventaire(joueur)
        elif choix == "3":
            if joueur.fuir():
                break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

        # Ennemi attaque
        degats_monstre = random.randint(3, 10)
        joueur.points_de_vie -= degats_monstre
        print("L'ennemi vous attaque et vous inflige {} points de dégâts.".format(degats_monstre))

    if joueur.points_de_vie > 0:
        print("Vous avez vaincu l'ennemi! Vous gagnez 10 pièces d'or.")
        joueur.inventaire["Or"] += 10
        
        resultat=1
    else:
        print("Vous avez été vaincu. Game Over.")
        resultat=0

def gestion_inventaire(joueur):
    while True:
        print("\n1. Utiliser un composant")
        print("2. Refermer l'inventaire")
        choix = input("Que voulez-vous faire? ")

        if choix == "1":
            composant = input("Choisissez un composant (Shield, Soins, Potions de force, Potions de vitalité) : ")
            joueur.utiliser_composant(composant)
        elif choix == "2":
            print("Vous refermez l'inventaire.")
            break
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

# Exemple d'utilisation
joueur = Joueur()
ennemi = {"points_de_vie": 30}

combat(joueur, ennemi, resultat)

base partie:

import sqlite3
from combatsrpg import combat
class Joueur:
    def _init_(self):
        self.nom = "Joueur"
        self.points_de_vie = 100
        self.inventaire = {
            "Or": 100,
            "Shield": 1,
            "Soins": 3,
            "Potions de force": 2,
            "Potions de vitalité": 5
        }

    # ... (autres méthodes de la classe Joueur)

def initialiser_base_de_donnees():
    conn = sqlite3.connect("resultats_parties.db")
    cursor = conn.cursor()

    # Création de la table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultats_parties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            victoire BOOLEAN,
            date_partie TEXT
        )
    ''')

    conn.commit()
    conn.close()

def enregistrer_resultat_partie(resultat):
    conn = sqlite3.connect("resultats_parties.db")
    cursor = conn.cursor()

    # Insertion d'un nouveau résultat dans la table
    cursor.execute("INSERT INTO resultats_parties (victoire, date_partie) VALUES (?, CURRENT_TIMESTAMP)", (resultat,))

    conn.commit()
    conn.close()

def afficher_stats_parties():
    conn = sqlite3.connect("resultats_parties.db")
    cursor = conn.cursor()

    # Récupération des statistiques
    cursor.execute("SELECT COUNT(*) FROM resultats_parties")
    total_parties = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM resultats_parties WHERE victoire = 1")
    victoires = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM resultats_parties WHERE victoire = 0")
    defaites = cursor.fetchone()[0]

    conn.close()

    # Affichage des statistiques
    print("\n--- Statistiques des parties ---")
    print("Total de parties jouées : {}".format(total_parties))
    print("Parties gagnées : {}".format(victoires))
    print("Parties perdues : {}".format(defaites))
    print("---------------------------------")

# Exemple d'utilisation
initialiser_base_de_donnees()

joueur = Joueur()
ennemi = {"points_de_vie": 30}

# Simuler une partie gagnée
combat(joueur, ennemi)
enregistrer_resultat_partie(victoire=True)

# Simuler une partie perdue
combat(joueur, ennemi)
enregistrer_resultat_partie(victoire=False)

# Afficher les statistiques
afficher_stats_parties()