from random import randint
from re import T
from time import *

import dispatch as sp
import donne_utilisateur.donnee_utilisateur as du
from class_match import match as mt

user, passw, username, salutation = '', '', '', ''
test = None


def connection_id():
    pre_id = 1000000
    id_c = pre_id + randint(100000, 100000000)
    return id_c


# fontion pour controler lheure
def time_watcher():
    temps = localtime().tm_hour
    return temps


# fonction Pour saluuer l'utilisateur connected
def say_hello(username, tm_par=time_watcher()):
    global salutation
    if tm_par >= 12 and tm_par <= 23:
        salutation = "Bonsoir"
    elif tm_par >= 0 and tm_par <= 11:
        salutation = "Bonjour"
    print(f"\n", end="")
    print("-" * 200)
    titre = f"""\
    {salutation} a vous {username}
                                                                                                                        l'heure de la connection est          :  {strftime('%H:%M:%S', localtime())}
                                                                                                                        Zone de Connection                         :  {localtime().tm_zone}
                                                                                                                        Id de Connection                               :  {salutation[0] + username[0:2].upper() + str(connection_id())}
                                                                                                                         """
    mt.letter_by_letter(titre, test)
    print("")
    print("-" * 200)


# fonction pour authentifier l'utilisateur qui essaie de se connecter
def auth() -> object:
    global user, passw, test
    print("\n\rEntrer votre nom utilisateur  : ", end="")
    user = input()
    print("Entrer votre mot de pass  :  ", end="")
    passw = input()

    # test de l'idantifiant de l'utilisateur
    if du.check_username_and_pass(user, passw) != bool(True):
        test = False
        while test != True:
            print(
                '\n l\'utilisateur est inactive ou mot de passe incorrect  \n'.capitalize())
            auth()
    elif du.check_username_and_pass(user, passw) == bool(True):
        test = True
        msg = "connection reussi \u2714".title()
        mt.letter_by_letter(msg, test)
        sleep(1)
        say_hello(user)
        sleep(1)
        sp.dispatcher()
        return test
