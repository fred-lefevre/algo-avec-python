#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-04-correction.py
# Vidéo de la correction commentée : https://youtu.be/zcRCAuaVYcY
#

def correspond(mot,  mot_a_trous):
    """ Renvoie :
    True si on peut obtenir mot en remplaçant convenablement les caractères '*' de mot_a_trous.
    False sinon"""
    if len(mot) != len(mot_a_trous):
        return False
    for ind in range(len(mot)):
        if mot_a_trous[ind] != '*' and mot_a_trous[ind] != mot[ind]:
            return False
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) # True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) # False

