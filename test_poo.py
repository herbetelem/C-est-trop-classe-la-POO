import random

class DataAnalyst:
    
    # set des var de base
    def __init__(self, nom, prenom, age, sexe, ecole, motiv, prog):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.formationPrecedante = ecole
        self.motivation = motiv
        self.progression = prog
        self.tour = 1
        
    # method qui update les stats
    def suivreFormation(self):
        self.motivation -= random.randint(5, 25)
        self.progression += random.randint(20, 30)
        print("La méthode suivreFormation() a été utilisée.")
        print(f"motivation vaut maintenant {self.motivation}")
        print(f"progression vaut maintenant {self.progression}")
        
    # method qui update les stats
    def bosserPlus(self):
        self.motivation += random.randint(10, 30)
        self.progression += random.randint(10, 30)
        print("La méthode bosserPlus() a été utilisée.")
        print(f"motivation vaut maintenant {self.motivation}")
        print(f"progression vaut maintenant {self.progression}")
        
    # method qui update les stats
    def echouer(self):
        self.motivation -= random.randint(20, 40)
        self.progression += random.randint(20, 40)
        print("La méthode echouer() a été utilisée.")
        print(f"motivation vaut maintenant {self.motivation}")
        print(f"progression vaut maintenant {self.progression}")
        
    # method qui update les stats
    def reussir(self):
        self.motivation += random.randint(20, 40)
        self.progression += random.randint(10, 20)
        print("La méthode reussir() a été utilisée.")
        print(f"motivation vaut maintenant {self.motivation}")
        print(f"progression vaut maintenant {self.progression}")
        
        
        
objet_instancier = DataAnalyst("Herbet", "Hadrien", 25, "Homme", "Startech Normandy", 100, 0)

while objet_instancier.motivation > 0 and objet_instancier.progression < 100:
    method = random.randint(1, 4)
    if method == 1:
        objet_instancier.suivreFormation()
        
    if method == 2:
        objet_instancier.bosserPlus()
        
    if method == 3:
        objet_instancier.echouer()
        
    if method == 4:
        objet_instancier.reussir()
        
if objet_instancier.motivation <= 0:
    print("BRAVO TU AS GAGNÉ !!!")
    
if objet_instancier.progression >= 100:
    print("BRAVO TU AS APPRIS !!!")