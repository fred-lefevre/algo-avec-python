#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-01-correction.py
# Vidéo de la correction commentée : https://youtu.be/gmkCiB8WOhU
#

def moyenne(tab):
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    '''
    som = 0
    for nb in tab:
        som += nb
    combien = len(tab)
    moy = som / combien
    return moy

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5
