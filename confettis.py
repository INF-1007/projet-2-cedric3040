import random
import pygame

class Confetti: 
    # TODO : Compléter la classe
    def __init__(self,screen, nb_confetti):
        self.nb_confetti = nb_confetti
        self.screen = screen
        self.confettis = self.faire_list_confetti()
        
        
        
    def faire_list_confetti(self):
        list_confetti = []
        for i in range(self.nb_confetti):
            position_x = random.randint(25, 975)
            position_y = random.randint(-150, 0)
            vitesse_y = random.uniform(0.5, 2)
            couleur = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            grandeur = random.randint(3,6)
            confetti = {"x" : position_x, "y" : position_y, "v_y" : vitesse_y, "color" :couleur, "size" : grandeur}
            list_confetti.append(confetti)
        return list_confetti
    
    @staticmethod
    def update_and_erase(list):
        for l in list:
            l["y"] += l["v_y"]
            
            if l["y"] >= 500:
                list.remove(l)
        return list
    
    
    def afficher(self):
        for conf in self.confettis:
            pygame.draw.rect(self.screen, conf["color"], (conf["x"], conf["y"], conf["size"], conf["size"]))

            
        self.confettis = self.update_and_erase(self.confettis) 
        

        
    
        