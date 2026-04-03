from vehicule import Vehicule
from roue import Roue
from moteur import Moteur
from chassis import Chassis
from specifications import CamionSpecs

class Camion(Vehicule): 
    
    def __init__(self, nom, position_dep):
        specs = CamionSpecs
        nb_roue = 6
        roues = Roue(specs.roue_nom, specs.roue_poids * nb_roue, specs.roue_friction, specs.roue_support)
        moteur = Moteur(specs.moteur_nom, specs.moteur_poids, specs.moteur_acceleration)
        chassis = Chassis(specs.chassis_nom, specs.chassis_poids, specs.chassis_aire, specs.chassis_trainee)
        
        super().__init__(nom=nom, position_dep=position_dep, Specs=specs, roues=roues, moteur=moteur, chassis=chassis, image_path="projet-2-cedric3040/images/camion.png")
        
        
        

