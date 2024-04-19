def creer_joueur(nom: str, couleur: str) -> list:
    """
    Permet de créer un joueur
    :param nom: Nom du joueur
    :param couleur: Couleur du joueur
    :return: liste avec les informations du joueur

    >>> j1 = creer_joueur("J1", "Jaune")
    >>> j1
    ['J1', 'Jaune']

    >>> j2 = creer_joueur("J2", "Rouge")
    >>> j2
    ['J2', 'Rouge']
    """
    return [nom, couleur]


def init_plateau(lignes: int = 6, colonnes: int = 7) -> list:
    """
    Permet d'initialiser le plateau via une liste par compréhension
    :param lignes: Nombre de lignes dans le plateau
    :param colonnes: Nombre de colonnes dans le plateau
    :return: liste (Matrice) représantant le plateau

    >>> init_plateau()
    [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    """

    return [[" " for _ in range(colonnes)] for _ in range(lignes)]


def est_vide(plateau: list, ligne: int, colonne: int) -> bool:
    """
    Permet de vérifier si une case est vide
    :param plateau: Matrcice du plateau de jeu
    :param ligne: Ligne de la case
    :param colonne: Colonne de la case
    :return: Booléen représantant la case si elle est vide ou non

    >>> jeu = init_plateau()
    >>> est_vide(jeu, 5, 6)
    True

    >>> est_vide(jeu, 0, 0)
    True

    >>> j1 = creer_joueur("J1", "Jaune")
    >>> jouer(jeu, 0, j1)
    True
    >>> est_vide(jeu, 5, 0)
    False
    """
    return plateau[ligne][colonne] == " "


def couleur_joueur(joueur: list) -> str:
    """
    Donne la couleur du joueur
    :param joueur: Joueur auquel on veut savoir la couleur
    :return: La couleur du joueur

    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> couleur_joueur(j1)
    'Jaune'

    >>> j2 = creer_joueur("Jean", "Rouge")
    >>> couleur_joueur(j2)
    'Rouge'
    """
    return joueur[1]


def jouer(plateau: list, colonne: int, joueur: list):
    """
    Permet de jouer un coup sur le plateau
    :param plateau: Matrice du plateau de jeu
    :param colonne: Colonne dans laquelle le joueur veut jouer
    :param joueur: Joueur qui joue
    :return:

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> jouer(jeu, 0, j1)
    True
    >>> afficher_plateau(jeu)
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |  J |    |    |    |    |    |    |
    -----------------------------------

    >>> jouer(jeu, 0, j1)
    True
    >>> afficher_plateau(jeu)
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |  J |    |    |    |    |    |    |
    -----------------------------------
    |  J |    |    |    |    |    |    |
    -----------------------------------
    """
    place: int = 0
    ligne: int = len(plateau)-1
    while (ligne >= 1 and place == 0):
        if est_vide(plateau, ligne, colonne):
            place = ligne
        ligne -= 1
    if not est_vide(plateau, place, colonne):
        return False
    else:
        plateau[place][colonne] = couleur_joueur(joueur)[0]
        return True


def contenu_case(plateau: list, ligne: int, colonne: int) -> str:
    """
    Retourne le contenu de la case
    :param plateau:  Matrice du plateau de jeu
    :param ligne: Ligne de la case à laquelle on veut voir le contenu
    :param colonne: Colonne de la case à laquelle on veut voir le contenu
    :return: Valeur de la case rechercher

    >>> jeu = init_plateau()
    >>> contenu_case(jeu, 0, 0)
    ' '

    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> jouer(jeu, 0, j1)
    True
    >>> contenu_case(jeu, 5, 0)
    'J'
    """
    return plateau[ligne][colonne]


def nombre_lignes(plateau: list):
    """
    Retourne le nombre de lignes
    :param plateau: Matrice du plateau de jeu
    :return: Le nombre de ligne

    >>> jeu = init_plateau()
    >>> nombre_lignes(jeu)
    6
    """
    return len(plateau)


def nombre_colonnes(plateau: list):
    """
    Retourne le nombre de colonnes
    :param plateau: Matrice du plateau de jeu
    :return: Le nombre de colonnes

    >>> jeu = init_plateau()
    >>> nombre_colonnes(jeu)
    7
    """
    return len(plateau[0])


def afficher_plateau(plateau: list):
    """
    Affiche le plateau de jeu
    :param plateau: Matrice du plateau de jeu
    :return:

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> afficher_plateau(jeu)
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------

    >>> jouer(jeu, 0, j1)
    True
    >>> afficher_plateau(jeu)
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |    |    |    |    |    |    |    |
    -----------------------------------
    |  J |    |    |    |    |    |    |
    -----------------------------------
    """
    trait: int
    ligne: int
    colonne: int
    for trait in range(5*nombre_colonnes(plateau)):
        print('-', end="")
    print("")
    for ligne in range(nombre_lignes(plateau)):
        for colonne in range(nombre_colonnes(plateau)):
            print("| ", contenu_case(plateau, ligne, colonne), end=" ")
        print("|")
        for trait in range(5 * nombre_colonnes(plateau)):
            print('-', end="")
        print("")


# Vérification de victoire
def verif_hori(plateau: list) -> tuple:
    """
    Retourne un tuple contenant un booléen et le signe du vainqueur si un joueur gagne en horizontal.
    :param plateau: Matrice du plateau de jeu.
    :return: Tuple contenant le booléen si un joueur gagne ainsi que son signe.

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> j2 = creer_joueur("Jean", "Rouge")
    >>> verif_hori(jeu)
    (False, '')

    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j2)
    True
    >>> jouer(jeu, 1, j1)
    True
    >>> jouer(jeu, 1, j2)
    True
    >>> jouer(jeu, 2, j1)
    True
    >>> jouer(jeu, 2, j2)
    True
    >>> jouer(jeu, 3, j1)
    True
    >>> jouer(jeu, 3, j2)
    True
    >>> jouer(jeu, 4, j1)
    True
    >>> jouer(jeu, 4, j2)
    True
    >>> verif_hori(jeu)
    (True, 'R')
    """
    ligne: int
    colonne: int
    for ligne in range(nombre_lignes(plateau)):
        cpt: int = 0
        signe: str = ""
        for colonne in range(nombre_colonnes(plateau)):
            if (signe == contenu_case(plateau, ligne, colonne) and signe != " "):
                cpt += 1
                if cpt == 4:
                    return True, signe
            else:
                signe = contenu_case(plateau, ligne, colonne)
                cpt = 1
    return False, ""


def verif_verti(plateau: list) -> tuple:
    """
    Retourne un tuple contenant un booléen et le signe du vainqueur si un joueur a gagné en vertical.
    :param plateau: Matrice du plateau de jeu.
    :return: Tuple contenant le booléen si un joueur gagne ainsi que son signe.

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> verif_verti(jeu)
    (False, '')

    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> verif_verti(jeu)
    (True, 'J')
    """
    ligne: int
    colonne: int
    for colonne in range(nombre_colonnes(plateau)):
        cpt: int = 0
        signe: str = ""
        for ligne in range(nombre_lignes(plateau)):
            if (signe == contenu_case(plateau, ligne, colonne) and signe != " "):
                cpt += 1
                if (cpt == 4):
                    return True, signe
            else:
                signe = contenu_case(plateau, ligne, colonne)
                cpt = 1
    return False, ""


def verif_diag(plateau: list) -> tuple:
    """
    Retourne un tuple contenant un booléen et le signe du vainqueur si un joueur a gagné en diagonale.
    :param plateau: Matrice du plateau de jeu.
    :return: Tuple contenant le booléen si un joueur gagne ainsi que son signe.

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> j2 = creer_joueur("Jean", "Rouge")
    >>> verif_diag(jeu)
    (False, '')

    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 1, j2)
    True
    >>> jouer(jeu, 1, j1)
    True
    >>> jouer(jeu, 2, j2)
    True
    >>> jouer(jeu, 2, j2)
    True
    >>> jouer(jeu, 2, j1)
    True
    >>> jouer(jeu, 3, j2)
    True
    >>> jouer(jeu, 3, j2)
    True
    >>> jouer(jeu, 3, j2)
    True
    >>> jouer(jeu, 3, j1)
    True
    >>> verif_diag(jeu)
    (True, 'J')
    """
    ligne: int
    colonne: int
    for ligne in range(nombre_lignes(plateau) - 3):
        for colonne in range(nombre_colonnes(plateau) - 3):
            # Par la droite
            if (
                    contenu_case(plateau, ligne, colonne) == contenu_case(plateau, ligne + 1, colonne + 1)
                    and contenu_case(plateau, ligne + 1, colonne + 1) == contenu_case(plateau, ligne + 2, colonne + 2)
                    and contenu_case(plateau, ligne + 2, colonne + 2) == contenu_case(plateau, ligne + 3, colonne + 3)
                    and contenu_case(plateau, ligne, colonne) != " "
            ):
                return True, contenu_case(plateau, ligne, colonne)
            # Par la gauche
            if (
                    contenu_case(plateau, ligne, colonne + 3) == contenu_case(plateau, ligne + 1, colonne + 2)
                    and contenu_case(plateau, ligne + 1, colonne + 2) == contenu_case(plateau, ligne + 2, colonne + 1)
                    and contenu_case(plateau, ligne + 2, colonne + 1) == contenu_case(plateau, ligne + 3, colonne)
                    and contenu_case(plateau, ligne, colonne + 3) != " "
            ):
                return True, contenu_case(plateau, ligne, colonne + 3)
    return False, ""


def a_gagner(plateau: list, joueur1: list, joueur2: list) -> tuple:
    """
    Retourne un tuple contenant un booléen et le nom du joueur gagnant
    :param plateau: Matrice du plateau de jeu
    :param joueur1: Liste contenant les informations du joueur 1
    :param joueur2: Liste contenant les informations du joueur 2
    :return: Tuple contenant le booléen si un joueur gagne ainsi que le nom du joueur gagnant

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> j2 = creer_joueur("Jean", "Rouge")
    >>> a_gagner(jeu, j1, j2)
    (False, '')

    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> a_gagner(jeu, j1, j2)
    (True, 'Michel')
    """
    if (verif_hori(plateau)[0] or verif_verti(plateau)[0] or verif_diag(plateau)[0]):
        signe_gagnant: str = verif_hori(plateau)[1] or verif_verti(plateau)[1] or verif_diag(plateau)[1]
        return True, joueur1[0] if signe_gagnant == joueur1[1][0] else joueur2[0]
    else:
        return False, ""


def egalite(plateau: list, cpt: int) -> bool:
    """
    Retourne un booléen dans le cas où les joueurs ont joué 42 fois
    :param plateau: Matrice du plateau du jeu
    :param cpt: Compteur du nombre de coups joué
    :return: Un booléen dans le cas où les joueurs ont joué 42 fois

    >>> jeu = init_plateau()
    >>> egalite(jeu, 0)
    False

    >>> jeu = init_plateau()
    >>> egalite(jeu, 42)
    True
    """
    if (cpt == nombre_lignes(plateau)*nombre_colonnes(plateau)):
        return True
    else:
        return False


def message_fin(plateau: list, cpt: int, joueur1: list, joueur2: list):
    """
    Affiche le message de fin de partie si un joueur à gagné
    :param plateau: Matrice du plateau de jeu
    :param cpt: Compteur de nombre de coups joué
    :param joueur1: Liste contenant les informations du joueur 1
    :param joueur2: Liste contenant les informations du joueur 2
    :return:

    >>> jeu = init_plateau()
    >>> j1 = creer_joueur("Michel", "Jaune")
    >>> j2 = creer_joueur("Jean", "Rouge")
    >>> message_fin(jeu, 0, j1, j2)
    (False,)
    
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> jouer(jeu, 0, j1)
    True
    >>> message_fin(jeu, 4, j1, j2)
    (True, 'Vous avez gagné Michel')

    >>> jeu = init_plateau()
    >>> jouer(jeu, 0, j2)
    True
    >>> jouer(jeu, 0, j2)
    True
    >>> jouer(jeu, 0, j2)
    True
    >>> jouer(jeu, 0, j2)
    True
    >>> message_fin(jeu, 8, j1, j2)
    (True, 'Vous avez gagné Jean')
    """
    gagnant: tuple = a_gagner(plateau, joueur1, joueur2)
    if (gagnant[0]):
        return(True, f"Vous avez gagné {gagnant[1]}")
    elif (egalite(plateau, cpt)):
        return(True, "Egalité")
    else:
        return (False,)


def verif_input(plateau: list, inp: str) -> bool:
    """
    Vérifie l'input du joueur
    :param plateau: Matrice du plateau de jeu
    :param inp: Input du joueur
    :return: Booléen si l'input est valide ou non

    >>> jeu = init_plateau()
    >>> verif_input(jeu, '10')
    False

    >>> verif_input(jeu, '7')
    True
    """
    try:
        inp = int(inp)
        return 1 <= inp <= nombre_colonnes(plateau)
    except ValueError:
        return False
    
    
def lancer_partie():
    """
    Permet de lancer une partie
    :return:
    """
    joueur: list
    colonne: int
    for i in range(1, 3):
        j_input: str = input(f"Entrez le pseudo d'un joueur {i} : ")
        while len(j_input) == 0:
            j_input = input("Pseudo non valide veuillez le réécrire : ")
        if i == 1:
            j1: list = creer_joueur(j_input, "Jaune")
        else:
            j2: list = creer_joueur(j_input, "Rouge")
    tour: int = 1
    jeu = init_plateau()
    while not a_gagner(jeu, j1, j2)[0]:
        afficher_plateau(jeu)
        if (tour % 2 == 1):
            joueur = j1
        else:
            joueur = j2

        while True:
            pose: str = input(f"Selectionnez une colonne pour placer le pion ({joueur[0]}) : ")
            if verif_input(jeu, pose):
                colonne = int(pose) - 1
                jeu_lancer = jouer(jeu, colonne, joueur)
                if jeu_lancer:
                    break
                else:
                    print("La colonne est pleine. Réessayez.")
            else:
                print("Entrée invalide. Veuillez entrer un nombre entre 1 et", nombre_colonnes(jeu))

        tour += 1
        if message_fin(jeu, tour, j1, j2)[0]:
            afficher_plateau(jeu)
            print(message_fin(jeu, tour, j1, j2)[1])

    rejouer: str = input("Voulez-vous rejouer ? (Oui/Non) : ").strip().lower()
    if rejouer == "oui" or rejouer == "o":
        lancer_partie()
    else:
        print("A bientôt")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    lancer_partie()