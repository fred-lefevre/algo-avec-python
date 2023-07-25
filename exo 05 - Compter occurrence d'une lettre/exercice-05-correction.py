#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-05-correction.py
# Vidéo de la correction commentée : https://youtu.be/oourqcW36-M
#

def recherche(caractere, mot):
    combien = 0
    for c in mot:
        if c == caractere:
            combien += 1
    return combien

print(recherche('e', "sciences"))   # 2
print(recherche('i',"mississippi")) # 4
print(recherche('a',"mississippi")) # 0
