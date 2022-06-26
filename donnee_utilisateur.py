liste_utilisateur = {'Bastien': 'inactive', 'Steph': 'active', 'Louis': 'active'}
liste_utilisateur_pass = ["1804", "1998"]
liste_utilisateur_verify={}

#Fonction pour verifier l'existance de l'utilisateur dans la base de donne
def check_username(username):
    test=None
    for user_name,stat in liste_utilisateur.items():
        if user_name == username and stat=='active':
            test =True
        elif user_name == username and stat=='inactive':
            test=False
    if username not  in liste_utilisateur:
        test=False
        print(f'l\'utilisateur {username} n\'est pas reconnue')
        print("Entrer votre nom utilisateur  : ", end="")
    return test


def add_username(username):
    test = None
    global liste_utilisateur
    if liste_utilisateur.append(username):
        test = True
    else:
        test = False
    return test


def check_userpass(password: object) -> object:
    test = None
    if password not in liste_utilisateur_pass:
        test = False
    else:
        test = True
    return test
    print(test)


def add_userpass(password):
    test = None
    global liste_utilisateur
    if liste_utilisateur.append(password):
        test = True
    else:
        test = False
    return test
#check_username(input())