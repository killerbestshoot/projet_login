import copy
from logging import exception
from random import randint
from time import *
import dispatch as dp

i = 0

list_match, list_match_copy = [], []


class match_info:
    list_match = None

    def __init__(self, identifiant, premier_equipe, seconde_equipe, score_equipe1, score_equipe2):
        text = "enregistrement de donnees d'une match".capitalize()
        progressPoint = '......'
        charet(text, end="")
        letter_by_letter(progressPoint*5)

        self.id1 = identifiant
        self.preE = premier_equipe
        self.secoE = seconde_equipe
        self.sco1 = score_equipe1
        self.sco2 = score_equipe2

    #
    # methode de la classe match_info pour generer les identifiant de la classe
    #
    def atribution(cls):
        match_info.id_match = randint(1000000, 10000000)
        return match_info.id_match

    atribution1 = classmethod(atribution)

    def Mk_list(cls, self):
        match_info.list_match.append(self)
        return match_info.list_match


# fonction pour faire les affectation des valeurs de la classe match_info
def affectation():
    while True:
        charet("<>" * 50)

        charet("Entrer le nom de la premiere equipe  : ", end="")
        NomE1 = input().upper()
        while NomE1 == '':
            charet(
                f"le nom \'{NomE1}\' que vous avez Entrer n'est pas Valide ", end="")
            NomE1 = input().upper()

        charet("Entrer le nom de la seconde equipe  :", end="")
        NomE2 = input().upper()
        while NomE2 == '':
            charet(
                f"le nom \'{NomE2}\' que vous avez Entrer n'est pas Validd ", end="")
            NomE2 = input().upper()

        charet("Entrer le score de la premiere equipe :  ", end="")
        try:
            Scoe1 = int(input())
            while Scoe1 < 0:
                charet("le Score ne peut Pas etre inferieur a 0  :", end="")
                Scoe1 = int(input())
        except:
            charet("le score ne peut pas etre une chaine de caracter")
            sleep(1)
            charet("\rVeuillez re-saisire le Score  :  ", end="")
            Scoe1 = int(input())
            while type(Scoe1) is not int:
                charet("\rVeuillez re-saisire le Score  :  ", end="")
                Scoe1 = int(input())

        charet("Entrer le score de la deuxieme equipe :  ", end="")
        try:
            Scoe2 = int(input())
            while Scoe2 < 0:
                charet("le Score ne peut Pas etre inferieur a 0  :", end="")
                Scoe2 = int(input())
        except:
            charet("le score ne peut pas etre une chaine de caracter")
            sleep(1)
            charet("\rVeuillez re-saisire le Score  :  ", end="")
            Scoe1 = int(input())
            while type(Scoe2) is not int:
                charet("\rVeuillez re-saisire le Score  :  ", end="")
                Scoe2 = int(input())

        MatchInfo: match_info = match_info(match_info.atribution(randint(1000000, 10000000)), NomE1, NomE2, Scoe1,
                                           Scoe2)
        global list_match
        list_match.append(MatchInfo)
        sleep(2)

        charet(f"""\r
            les donnees du match ont bien ete enregistrer 

            Id                                           : {MatchInfo.id1}
            Premier Equipe               : {MatchInfo.preE}
            Seconnd Equipe               : {MatchInfo.secoE}
            Score finale                        : {MatchInfo.sco1} : {MatchInfo.sco2}
            """)
        charet('voulez vous enregistrer d\'autre match  "(O) Oui : (N) Non"  :', end="")
        rep: str = input().capitalize()
        if rep == "OUI" or rep == "O":
            affectation()
        elif rep == "NON" or rep == "N":
            dp.match_data()

#fonction pour faire l'affichage des donnees

def affichage():
    i1 = 1
    titre = "affichage de la liste des matchs".title()
    for i in range(len(titre)):
        sleep(0.1)
        charet(titre[i], end="")
    for MatchInfo in list_match:
        sleep(1)
        charet(f"""\r
            Match :{i1} 

            Id                                           : {MatchInfo.id1}
            Premier Equipe               : {MatchInfo.preE}
            Seconnd Equipe               : {MatchInfo.secoE}
            Score finale                        : {MatchInfo.sco1} : {MatchInfo.sco2}
            
            """)
        i1 += 1
        charet("-" * 90)

#fonction pour test le liste des objets si vide ou pas
def testList():
    test = None
    if len(list_match) > 0:
        test = True
    else:
        test = False
    return test

#fonction pour supprimer les objets match qui prend en parametre un entier (l'identifiant)
def sup_id(supId):
    global list_match_copy
    test = False
    rep = ''
    for MatchInfo in list_match:
        charet(MatchInfo.id1)
        if MatchInfo.id1 == int(supId):

            charet(f"""Voulez vous vraiment supprimer l'objet ({MatchInfo.id1}) ?
            Pressez (O) pour "oui" (N) pour "non" :
            """, end="")
            rep = input().upper()
            while not (rep.isalpha()):
                charet("la reponse n\'est pas correcte ,(O)Oui ,(N)Non  :")
                rep = input().upper()
            if "OUI" == rep or rep == "O":
                list_match.remove(MatchInfo)

            elif rep == "NON" or rep == "N":
                #charet(f"vous avez choisi {rep}".title())
                sleep(2)
                dp.match_data()
            else:
                charet(" \u274C  reponse invalide !!!".upper())
                sleep(2)
                dp.match_data()
            test = True
    if test == bool(False):
        for MatchInfo in list_match:
            if MatchInfo.id1 != int(supId):
                # charet(f"{MatchInfo.id1}!={supId}")
                pcharet1 = f"apres la recherche l\'objet {supId} n\'a pas ete trouve".title(
                )
                letter_by_letter(pcharet1)
                sleep(2)
                dp.match_data()


# ============================================================================================================================
# ============================================================================================================================
# ============================================================================================================================

# fonction pour supprimer un match de la liste des match 
#il effectue un appel a la fonction sup_id() 
# et a la fonction test pour verifier si la liste n'est pas vide
def suppression():
    sup_id1 = ''
    chare = "suppression de match".title()
    letter_by_letter(chare)
    if testList() == True:
        sleep(2)
        while not (sup_id1.isdigit()):
            sup_id1 = input(
                "\rveuillez saisir l\'identifiant du match a supprimer  : ")
    else:
        sleep(2)
        letter_by_letter("\roups la liste est vide".upper())
        sleep(2)
        dp.match_data()
    sup_id(sup_id1)

# fonction pour l'affichage character par character
def letter_by_letter(chare,test):
    if test==bool(True):
        for cha in range(len(chare)):
            print(chare[cha], end="")
            sleep(0.1)
    else:
        for cha in range(len(chare)):
            print(chare[cha],end="")
            sleep(0.1)
