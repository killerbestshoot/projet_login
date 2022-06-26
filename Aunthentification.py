from time import *
from random import randint
import dispatch as sp
import donnee_utilisateur as du

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
    i = 0
    for i in range(len(titre)):
        if titre[i]!=''or titre[i].isspace()==False:
            sleep(0.1)
            print(titre[i], end="")
    print("")
    print("-" * 200)


# fonction pour authentifier l'utilisateur qui essaie de se connecter
def auth() -> object:
    global user, passw, username, test
    print("Entrer votre nom utilisateur  : ", end="")
    username = input()
    user = du.check_username(username)
    while user!=True:
        username = input()
        user = du.check_username(username)
    print("Entrer votre mot de pass  :  ", end="")
    passw = du.check_userpass(input())
    # test de l'idantifiant de l'utilisateur
    if user != True or passw != True:
        test = False
        while test != True:
            print('\n l\'utilisateur est inactive OU mot de passe incorrect  \n'.capitalize())
            auth()
    elif user == True and passw == True:
        test = True
        sleep(1)
        say_hello(username)
        sleep(1)
        sp.dispatcher()
        return test
