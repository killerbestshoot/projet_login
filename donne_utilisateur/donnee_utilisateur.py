from time import *

import Aunthentification as aut
import dispatch as dp
from class_match import match as mt

liste_utilisateur = {'Bastien': 'inactive',
                     'Steph': 'active', 'Louis': 'active'}
liste_utilisateur_pass = ["1804", "1998"]
liste_utilisateur_verify = {}


# fonction pour afficher les utilisateur
def listing_user():
    test = None
    i = 1
    if len(liste_utilisateur) <= 0:
        test = False
        mesg = "il n\'y pas d'utilisateur dans la base de donnee\n".title()
        mt.letter_by_letter(mesg, test)
        sleep(3)
        dp.user_match_data()
    else:
        test = True
        print("# -> nom_utilisateur  |   etat".upper())
        for username, status in liste_utilisateur.items():
            outf = f"{i} -> {username}    :   {status}\n"
            mt.letter_by_letter(outf, test)
            i += 1
        ter = f"\u2714 un total de {i} utilisateur(s) a ete affiche\n".title()
        mt.letter_by_letter(ter, test=True)
        sleep(2)

# Fonction pour verifier l'existance de l'utilisateur dans la base de donne


def check_username_and_pass(username, passw):
    test = None
    for user_name, stat in liste_utilisateur.items():
        if user_name == username and stat == 'active' and passw in liste_utilisateur_pass:
            test = True
        elif user_name == username and stat == 'inactive':
            test = False
    if username not in liste_utilisateur and passw not in liste_utilisateur_pass:
        test = False
        msg = f'\nl\'utilisateur ( {username} ) n\'est pas reconnue\n'.title()
        mt.letter_by_letter(msg, test)
        sleep(2)
        aut.auth()
    return test


def add_username(username):
    test = None
    global liste_utilisateur
    if liste_utilisateur.append(username):
        test = True
    else:
        test = False
    return test


def add_userpass(password):
    test = None
    global liste_utilisateur
    if liste_utilisateur.append(password):
        test = True
    else:
        test = False
    return test
# check_username(input())
