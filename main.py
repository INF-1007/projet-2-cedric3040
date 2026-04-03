import pygame
from moto import Moto
from auto import Auto
from camion import Camion
from confettis import Confetti
from config import WIDTH, HEIGHT, START_LINE_X, FINISH_LINE_X, START_MOTO_Y, START_AUTO_Y, START_CAMION_Y 


def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulation de course")

    background = pygame.image.load("projet-2-cedric3040/images/background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # TODO : Créer une liste de véhicules qui contient une instance pour chaque
    # type de véhicule : une moto, une auto et un camion
    moto = Moto("vroom, vroom", [START_LINE_X, START_MOTO_Y])
    auto = Auto("flash_mc_queen", [START_LINE_X,START_AUTO_Y])
    camion = Camion("Matere", [START_LINE_X, START_CAMION_Y])
    vehicules = [moto, auto, camion]
    
    running = True
    course_commencee = False
    gagnant = None

    while running:

        screen.blit(background, (0, 0))

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    course_commencee = True

        # TODO : Gérer le début de la course en appelant la méthode `accelerer` des véhicules
        # Si le véhicule franchit la ligne et qu’on n’a pas encore de gagnant, on le note

        for v in vehicules:
            if course_commencee:
                v.accelerer(dt)
                if v.get_position()[0] >= FINISH_LINE_X and gagnant is None:
                    gagnant = v
                    confettis = Confetti(screen, 2000)
        # TODO : Pour chaque véhicule, appeler la méthode `affichage_vehicule`
        for v in vehicules:
            v.affichage_vehicule(screen)

        if not course_commencee and gagnant is None:
            txt = font.render("Appuyez sur ESPACE pour démarrer",
                              True, (0, 0, 0))
            screen.blit(txt, (350, 35))

        # TODO: Si on a un gagnant, afficher le message qui indique le véhicule gagnant avec la méthode `celebrer` 
        
        if gagnant != None:
            texte = gagnant.celebrer()
            txt_gagnant = font.render(texte, True, (0, 0, 0))
            screen.blit(txt_gagnant, (350, 35))
            confettis.afficher()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()