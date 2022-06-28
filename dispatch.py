import donne_utilisateur.donnee_utilisateur as du
from class_match import match as m
import sys

match_list = {}


def match_data():
    Menue = """
    1: Enregistrer Donnees Match
    2: Afficher Donnees des Match
    3: Supprimer Donnees Match
    4: Menue Precedent
    Faite votre choix :"""
    choice_poss = ['1', '2', '3', '4']
    while True:
        user_choice = ''
        while user_choice not in choice_poss:
            user_choice = input(Menue)
            if user_choice == '1':
                m.affectation()
            elif user_choice=='2':
                print("\nAffichage des Matchs...")
                m.affichage()
            elif user_choice=='3':
                m.suppression()
            elif user_choice=='4':
                dispatcher()
            
def user_match_data():
    Menue="""
    1:Afficher les utilisateur 
    2:Ajouter un utilisateur 
    3:Supprimer un utilisateur
    4:Menue Precedent 
    Faite votre Choix  : """
    choice_posi=['1','2','3','4']
    while True:
        user_choic=''
        while user_choic not in choice_posi:
            user_choic=input(Menue)
            if user_choic=='1':
                du.listing_user()
            elif user_choic=='2':
                pass
            elif user_choic=='3':
                pass
            elif user_choic=='4':
                pass
            else:
                message="Veuillez faire une choix valide".upper()
                


def dispatcher():
    Menue = """
    1: Gestion des Donnees
    2:  Gestion des utilisateur
    3: Quiter le Programme
    Votre choix  : """

    choice_poss = ['1', '2', '3']
    while True:
        user_choice = ''
        while user_choice not in choice_poss:
            user_choice = input(Menue)
            if user_choice == '1':
                print('*' * 10, '            Gestion des Donnees                  ', '*' * 10)
                match_data()
            elif user_choice == '2':
                print('*' * 10, '            Gestion des Utilisateur                 ', '*' * 10)
                user_match_data()
            elif user_choice == '3':
                sys.exit()
            else:
                print('*' * 10, '            Faite un choix Valide                 ', '*' * 10)
