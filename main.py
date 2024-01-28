import time
from style import textEffect
from callClasses import nameClasses, classesSelector


textEffect("Bonjour Héro ! Quel est ton nom ? ")
username = input()
textEffect(f"Bienvenue {username} !")
time.sleep(0.5)
textEffect("Il est temps de choisir ta classe !")
time.sleep(0.5)
textEffect("Voici les classes disponibles :")
nameClasses()

while True:
    textEffect(f"{username}, veux-tu en savoir plus sur les classes ? \n[O]. Oui \n[N]. Non")
    answer = input().capitalize()
    if answer == "O":
            while True:         
                textEffect("Sur quelle classe veux-tu en savoir plus ? \n[Q]. Quitter")
                for key, value in classesSelector().items():
                    textEffect(f"[{key}]. {value}")
                a = input()
                if a == "1":
                    textEffect("Mage")
                    textEffect("Le mage est un personnage qui utilise la magie pour combattre ses ennemis. Il est capable de lancer des sorts de feu et de glace. Son sort ultime est une météore qui s'abat sur ses ennemis.")
                elif a == "2":
                    textEffect("Chevalier")
                    textEffect("Le chevalier est un personnage qui utilise son épée pour combattre ses ennemis. Il est capable de se protéger avec son bouclier et de charger ses ennemis. Son sort ultime est un coup de grâce qui inflige de lourds dégâts à son ennemi.")
                elif answer == "3":
                    textEffect("Assassin")
                    textEffect("L'assassin est un personnage qui utilise son agilité pour combattre ses ennemis. Il est capable de se rendre invisible et d'empoisonner ses ennemis. Son sort ultime est un assassinat qui inflige de lourds dégâts à son ennemi.")
                elif answer == "4":
                    textEffect("Archer")
                    textEffect("L'archer est un personnage qui utilise son arc pour combattre ses ennemis. Il est capable de tirer des flèches et de les empoisonner. Son sort ultime est une flèche explosive qui inflige de lourds dégâts à son ennemi.")
                elif a == "Q" or a == "q":
                    break
    elif answer == "N":
        break

textEffect("Choisis ta classe :")