import sys
import time
# Ajout effet d'écriture au texte
def textEffect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\n')
    sys.stdout.flush()