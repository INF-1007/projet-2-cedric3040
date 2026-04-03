Expliquation confetti

on initie la class avec le nb de confetti et le screen

avec ses argument on fait trois attribut:
- le screen 
- nb_conffetti
- list de conffetti qui aura len == nb_conffetie

ensuite pour faite la liste de confetti => j'ai fait une liste de dict
dans chaque confetti il y a son x, son y, sa vitesse_y, sa couleur, sa grandeur
- le x, y, vitesse_y, grandeur sont => int randomiser
- la couleur est un tuple (rouge, bleu, vert) => dont chaque couleur est random

Pour update et regarder si un conffetti est sortie de l'écran, j'ai fait une boucle qui regarde
chaque confetti et qui soustrait la valeur de vitesse_y a sa position_y
puis on regarde si sa position a dépasser le 500 qui est le HEIGHT et on remove si oui

Pour afficher chaque conffetti on utilise une boucle affiche chaque conffetti avec 
pygame.draw.rect() avec presque tout les argument du dictionnaire d'un confetti
apres la boucle on mets la fonction update_and_erase qui changera la liste de dict

en ce qui est de la fonction en général,¸
je fais apparaitre d'un coup 2000 conffetti au dessus de l'écran a des position différent de x et y pour qu'il sois plus disperser et ils descende a des vitesse différente puis ils update et on les réaffiche

dans le main l'objet confettis a du être mits dans le if du gagant pour qu'il soit crée qu'une fois et qu'on l'affiche dans la if: le gagnant est défénie. pour qu'elle affiche a chaque tour de boucle


