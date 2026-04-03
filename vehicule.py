
import numpy as np
import pygame
from specifications import DENSITE_AIR

# TODO : Créer la classe Vehicule

class Vehicule:

    

    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, Specs, roues, moteur, chassis, image_path):

        # TODO : ajouter les attributs
        self.__nom = nom
        self.__vitesse = np.array([0,0], dtype=float)
        self.__position = np.array((position_dep[0] - Specs.image_width, position_dep[1]), dtype=float)
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__specs = Specs
        self.__poids_total = self.calculer_poids_total()
       
        
        # TODO : ajouter un attribut pour l'image du véhicule
        image = pygame.image.load(image_path)
        self.__image = pygame.transform.scale(image, [Specs.image_width, Specs.image_height])
        
        
    
    def affichage_vehicule(self, screen):
        # TODO : compléter la méthode
        
        screen.blit(self.__image, self.__position)

    def calculer_poids_total(self):
        poids_roue = self.__roues.get_poids()
        poids_moteur = self.__moteur.get_poids()
        poids_chassis = self.__chassis.get_poids()
        
        return poids_chassis + poids_moteur + poids_roue

    def calculer_traction(self):
        # TODO : compléter la méthode 
        poids_moteur = self.__moteur.get_poids()
        acceleration = self.__moteur.get_acceleration()
        return poids_moteur * acceleration

    def calculer_friction(self):
        # TODO : compléter la méthode 
        coefficient_friction = self.__roues.get_coefficient_friction()
        vitesse = self.__vitesse
        return coefficient_friction * vitesse

    def calculer_trainee(self):
        
        coefficient_trainee = self.__chassis.get_coefficient_trainee()
        aire_frontale = self.__chassis.get_aire_frontale()
        vitesse = self.__vitesse
        return 0.5 * coefficient_trainee * aire_frontale * DENSITE_AIR * (vitesse ** 2)

    def accelerer(self, dt):
        # TODO : compléter la méthode 
        acceleration = (np.array((self.calculer_traction(),0.0)) - self.calculer_trainee() - self.calculer_friction()) / self.__poids_total
        self.__vitesse += acceleration * dt
        self.__position += self.__vitesse * dt

    def celebrer(self):
        # TODO : compléter la méthode 
        
        return f"{self.__nom} a remporter la course !!!"
    
    def get_position(self):
        return self.__position