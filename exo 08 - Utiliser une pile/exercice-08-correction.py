#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-08-correction.py
# Vidéo de la correction commentée : https://youtu.be/h07GM8dmgDU
#
def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

# T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
assert positif([-1,0,5,-3,4,-6,10,9,-8 ]) == [0, 5, 4, 10, 9]


