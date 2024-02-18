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


def list_stats():
    key = player[2]
    connection = sqlite3.connect('Database/classes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM classes WHERE name=?", (key,))
    stats = cursor.fetchone()
    connection.close()
    return stats
stats = list_stats()
hpi_hero = stats[2]


def update_stats():
    connection = sqlite3.connect('Database/classes.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM classes WHERE name=?", (player[2],))
    stats = cursor.fetchone()
    connection.close()
    return stats

def update_inventory():
    connection = sqlite3.connect('Database/inventory.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    connection.close()
    return inventory
        
def open_inventory():
    inventory = update_inventory()
    print(f"--- Inventaire de {player[1]} ---")
    for item in inventory:
        textEffect(f"[{item[0]}] {item[1]} : {item[2]}")

def fight():
    victory = None
    monster = random_monster()
    hp_hero = stats[2]
    attack_hero = stats[3]
    attack_monster = monster[2]
    hp_monster = monster[3]
    print(f"{monster[1]} vous attaque !")
    while hp_hero > 0 and hp_monster > 0:
        stat = update_stats()
        inventory_update = update_inventory()
        hp_hero = stat[2]
        attack_hero = stat[3]
        print("--- Infos sur le combat ---")
        textEffect(f"{player[1]} : \n PV :{hp_hero} \n ATK : {attack_hero}")
        textEffect(f"{monster[1]} : \n PV :{hp_monster} \n ATK : {attack_monster}")
        print("---------------------------")
        textEffect("Que veux-tu faire ?")
        textEffect("[1] Attaquer")
        textEffect("[2] Utiliser un objet")
        textEffect("[3] Fuir")
        choice = input()
        #! Attaque
        if choice == "1":
            textEffect("Tu sors ton dé à 20 faces et tu lances le dé !")
            atk = int(attack_hero)
            damage = random.randint(25, atk)
            textEffect(f"Tu infliges {damage} points de dégats à {monster[1]}")
            hp_monster -= damage
        #! Item
        elif choice == "2":
            open_inventory()
            textEffect("Quel objet veux-tu utiliser ?")
            item_choice = input()
            item_found = False
            for item in inventory_update:
                if item_choice == str(item[0]):
                    item_found = True
                    while True:
                        if item_choice == "1":
                            textEffect("Tu essayes de corrompre ton opposant avec ta fortune mais rien ne se passe !")
                            break
                        elif item_choice == "2":
                            if item[2] == 0:
                                textEffect(f"Tu n'as plus {item[1]}")
                                break
                            else:
                                if hp_hero == hpi_hero:
                                    textEffect(f"Tu n'as pas besoin de {item[1]}")
                                    break
                                else:
                                    textEffect(f"Tu utlilises {item[1]}, un, deux, trois, tu te soignes de 5 hp !")
                                    connection = sqlite3.connect('Database/classes.db')
                                    cusor = connection.cursor()
                                    cusor.execute("UPDATE classes SET  hp = hp + 5 WHERE name=?", (player[2],))
                                    connection.commit()
                                    connection.close()
                                    connection = sqlite3.connect('Database/inventory.db')
                                    cursor = connection.cursor()
                                    cursor.execute("UPDATE inventory SET quantity = quantity - 1 WHERE id=?", (item[0],))
                                    connection.commit()
                                    connection.close()
                            break
                        elif item_choice == "3": 
                            if item[2] == 0:
                                textEffect(f"Tu n'as plus {item[1]}")
                                break
                            else:
                                textEffect(f"Tu utlilises {item[1]}, en suivant les précaution de ton druide préféré ton attack augmente de 5")
                                connection = sqlite3.connect('Database/classes.db')
                                cusor = connection.cursor()
                                cusor.execute("UPDATE classes SET  attack = attack + 5 WHERE name=?", (player[2],))
                                connection.commit()
                                connection.close()
                                connection = sqlite3.connect('Database/inventory.db')
                                cursor = connection.cursor()
                                cursor.execute("UPDATE inventory SET quantity = quantity - 1 WHERE id=?", (item[0],))
                                connection.commit()
                                connection.close()
                            break
                        elif item_choice == "4":
                            if item[2] == 0:
                                textEffect(f"Tu n'as plus {item[1]}")
                                break
                            else:
                                textEffect(f"Tu utlilises {item[1]}, en suivant les précaution de ton druide préféré tes pv augmentent de 5")
                                connection = sqlite3.connect('Database/classes.db')
                                cusor = connection.cursor()
                                cusor.execute("UPDATE classes SET  hp = hp + 5 WHERE name=?", (player[2],))
                                connection.commit()
                                connection.close()
                                connection = sqlite3.connect('Database/inventory.db')
                                cursor = connection.cursor()
                                cursor.execute("UPDATE inventory SET quantity = quantity - 1 WHERE id=?", (item[0],))
                                connection.commit()
                                connection.close()
                            break
                        else:
                            textEffect("Tu es créatif mais je ne suis pas sûr que cette qualité t'aide")
                            textEffect("Quel objet veux-tu utiliser ?")
                            item_choice = input()
            if not item_found:
                textEffect("Cet objet n'est pas dans ton inventaire !")
        #! Fuite
        elif choice == "3":
            luck = random.randint(1, 10)
            if luck <= 5:
                textEffect("Tu t'enfuis comme un lâche !")
                victory = None
                break
            else:
                textEffect("Dans ta fuite, tu glisses sur une peau de banane et ton adversaire te ratrape !")
        else:
            textEffect("Nan sérieux pourtant c'est pas compliqué tu n'as que 3 choix !")
            #! Attaque du monstre
        if hp_monster > 0:
            atk = int(attack_monster)
            damage = random.randint(3, atk)
            textEffect(f"{monster[1]} passe à l'attaque et t'inflige {damage} points de dégâts.  Ça pique !")
            hp_hero -= damage
            connection = sqlite3.connect('Database/classes.db')
            cusor = connection.cursor()
            cusor.execute("UPDATE classes SET  hp = hp - ? WHERE name=?", (damage, player[2]))
            connection.commit()
            connection.close() 
        if hp_hero <= 0:
            textEffect("Tu as perdu tout tes point de vie. Game Over.")
            victory = False
            break
      #! Vérification de la fin du combat
        if hp_monster <= 0:
            textEffect(f"Tu as vaincu {monster[1]} ! Tu gagne 10 pièces d'or. Elle ne sont pas spécialement belles mais elles sont à toi !")
            connection = sqlite3.connect('Database/inventory.db')
            cursor = connection.cursor()
            cursor.execute("UPDATE inventory SET quantity = quantity + 10 WHERE name='Or'")
            connection.commit()
            connection.close()
            victory = True
            break
    return victory


