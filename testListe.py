# liste_utilisateur = {'Bastien': 'active', 'Steph': 'inactive', 'Louis': 'active'}
# print(liste_utilisateur)
# for u,i in liste_utilisateur.items():
#     print(u,i)
from time import *
# titre="affichage de la liste des matchs".title()
# i=0
# for i in range(len(titre)):
#     sleep(0.1)
#     print(titre[i],end="")
# i=0
# t=50
# text="enregistrement de donnees d'une match".capitalize()
# progressPoint='......'
# print(text,end="")
# for i in range(len(progressPoint)-1):
#     sleep(0.3)
#     progressPoint='.....'*5
#     print(progressPoint[i]*15,end="")
import time
from threading import Thread


def collect_data():
    pass

t = Thread(target=collect_data)
t.start()

timeout = 30.0

while t.is_alive():
    time.sleep(0.1)
    timeout -= 0.1
    if timeout == 0.0:
        print('Please wait...')
        timeout = 30.0