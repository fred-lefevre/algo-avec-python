#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-03-correction.py
# Vidéo de la correction commentée : https://youtu.be/ff-wINNYx6s
#

def a_doublon(li):
    """
    Retourne True lorsque la liste li contient un doublon.
    Retourne False lorsque li ne contient pas de doublon
    """
    for ind in range(0, len(li) -1):
        # print(li[ind], li[ind + 1])
        if li[ind] == li[ind + 1]:
            return True
    
    return False

print(a_doublon([]))
print(a_doublon([1, 2, 4, 4, 6]))
print(a_doublon([2, 5, 7, 7, 7, 9]))
print(a_doublon([ 1 ]))
print(a_doublon([ 0, 2, 3 ]))