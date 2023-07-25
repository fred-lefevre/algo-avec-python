#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-02-correction.py
# Vidéo de la correction commentée : https://youtu.be/UGf7biupddM
#

def maxliste(tab):
    """
    Le paramètre tab est une liste de nombres non vide
    Retourne le maximum de ces nombres
    """
    assert type(tab) == list, "tab doit être une liste"
    assert len(tab) != 0, "tab ne doit pas être vide"
    maxi = tab[0] # Initialiser avec le premier element
    for element in tab[1:]: # Parcours à partir du second élément
        if element > maxi:
            maxi = element
    return maxi

print(maxliste([98, 12, 104, 23, 131, 9])) # 131
print(maxliste([-27, 24, -3, 15])) # 24
