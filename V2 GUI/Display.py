import pygame
import Controller as ct

JAUNE = (255, 243, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 31, 255)
NOIR = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((900, 900))

def saisi_joueur(j: int, couleur: str):
    """
    Affiche une fenêtre pour saisir le pseudo du joueur j avec la couleur couleur.
    :param j: Numéro du joueur.
    :param couleur: Couleur du joueur.
    :return: Une liste contenant le pseudo et la couleur du joueur.
    """
    affiche: bool = True
    pseudo_joueur: str = ""
    while affiche:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                affiche = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(pseudo_joueur) != 0:
                        affiche = False
                elif event.key == pygame.K_BACKSPACE:
                    pseudo_joueur = pseudo_joueur[:-1]
                else:
                    pseudo_joueur += event.unicode
        screen.fill(WHITE)
        myfont = pygame.font.Font(None, 45)
        label = myfont.render(f"Entrez le pseudo de joueur {j} : {pseudo_joueur}", 1, NOIR)
        screen.blit(label, (100, 350))
        pygame.display.flip()
    return ct.creer_joueur(pseudo_joueur, couleur)


def jouer(pos: list) -> int:
    """
    Vérifie la position du clic de la souris et renvoie la colonne cliquée si elle est dans un intervalle enregistré.
    :param pos: Position de la souris.
    :return: La colonne dans laquelle le joueur a cliqué, ou -1 si le clic est en dehors des limites.
    """
    if 170 <= pos[1] <= 900:
        if pos[0] <= 155:
            return 0
        elif pos[0] <= 270:
            return 1
        elif pos[0] <= 385:
            return 2
        elif pos[0] <= 500:
            return 3
        elif pos[0] <= 615:
            return 4
        elif pos[0] <= 730:
            return 5
        elif pos[0] <= 845:
            return 6
        else:
            return -1
    else: 
        return -1
        
def jeu(j1: list, j2: list):
    """
    Affiche la fenêtre de jeu contenant le plateau et les informations sur le joueur qui joue, prend en compte les clics du joueur en cours pour placer son pion.
    :param j1: Liste contenant les informations du joueur 1.
    :param j2: Liste contenant les informations du joueur 2.
    """
    affiche: bool = True
    plateau: list = ct.init_plateau()
    joueur_actu: list = j1
    tour: int = 0
    while affiche:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                affiche = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                colonne: int = jouer(pos)
                if colonne != -1:
                    if ct.jouer(plateau, colonne, joueur_actu):
                        joueur_actu = j1 if joueur_actu == j2 else j2
                        tour += 1
                        a_gagner: tuple = ct.message_fin(plateau, tour, j1, j2)
                        if a_gagner[0]:
                            affiche = False
                            menu_fin(a_gagner[1], plateau)
        screen.fill(BLEU)
        myfont = pygame.font.Font(None, 45)
        label = myfont.render(f"Joueur qui joue : {joueur_actu[0]} de couleur {joueur_actu[1]}", 1, NOIR)
        screen.blit(label, (100, 50))
        y: int = 230
        for i in range(ct.nombre_lignes(plateau)):
            x = 100
            for j in range(ct.nombre_colonnes(plateau)):
                if ct.est_vide(plateau, i, j):
                    pygame.draw.circle(screen, WHITE, (x, y), 50, 0)
                else:
                    if ct.contenu_case(plateau, i, j) == "J":
                       pygame.draw.circle(screen, JAUNE, (x, y), 50, 0) 
                    else:
                        pygame.draw.circle(screen, ROUGE, (x, y), 50, 0)
                x += 115
            y += 115
        pygame.display.flip() 

def menu_fin(message: str, plateau: list):
    """
    Affiche la fenêtre de fin de jeu avec le message de fin et le plateau final, propose aux joueurs de relancer une partie ou de quitter.
    :param message: Message de fin de jeu (qui a gagné ou égalité).
    :param plateau: Plateau final.
    """
    affiche: bool = True
    while affiche:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                affiche = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    affiche = False
                    pygame.quit()
                else:
                    if event.unicode == "r":
                        lancer_jeu()
        screen.fill(BLEU)
        myfont = pygame.font.Font(None, 45)
        label = myfont.render(message, 1, NOIR)
        label2 = myfont.render("Presser R pour relancer ou Entrer pour quitter", 1, NOIR)
        screen.blit(label, (100, 50))
        screen.blit(label2, (100, 80))
        y: int = 230
        for i in range(ct.nombre_lignes(plateau)):
            x = 100
            for j in range(ct.nombre_colonnes(plateau)):
                if ct.est_vide(plateau, i, j):
                    pygame.draw.circle(screen, WHITE, (x, y), 50, 0)
                else:
                    if ct.contenu_case(plateau, i, j) == "J":
                       pygame.draw.circle(screen, JAUNE, (x, y), 50, 0) 
                    else:
                        pygame.draw.circle(screen, ROUGE, (x, y), 50, 0)
                x += 115
            y += 115
        pygame.display.flip()

def lancer_jeu():
    """
    Lance le jeu en demandant les pseudos des joueurs et en lançant la partie.
    """
    j1: list = saisi_joueur(1, "Jaune")
    j2: list = saisi_joueur(2, "Rouge")
    jeu(j1, j2)
    
if __name__ == "__main__":
    lancer_jeu()