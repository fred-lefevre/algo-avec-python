#   __  _  ____     ___   ____  ______  __ __  ______   ___  
#  |  |/ ]|    \   /  _] /    ||      ||  |  ||      | /   \ 
#  |  ' / |  D  ) /  [_ |  o  ||      ||  |  ||      ||     |
#  |    \ |    / |    _]|     ||_|  |_||  |  ||_|  |_||  O  |
#  |     \|    \ |   [_ |  _  |  |  |  |  :  |  |  |  |     |
#  |  .  ||  .  \|     ||  |  |  |  |  |     |  |  |  |     |
#  |__|\_||__|\_||_____||__|__|  |__|   \__,_|  |__|   \___/ 
#                                                            
# exercice-07-correction.py
# Vidéo de la correction commentée : https://youtu.be/A8Dr4FS4350
#

def pair(n):
    return n % 2 == 0

def u(n,k):
    if n == 0:
        return k
    precedent = u(n-1, k)
    if pair(precedent):
        return precedent // 2
    else:
        return precedent * 3 + 1

def calcul(k):
    n = 0
    val = u(0, k)
    resu = [val]
    while val != 1:
        n += 1
        val = u(n, k)
        resu.append(val)
    return resu


print(calcul(7)) # [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(calcul(5)) # [5, 16, 8, 4, 2, 1]

