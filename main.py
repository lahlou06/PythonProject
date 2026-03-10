class voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

        def afficherInformations(self) -> None:
            print(f"Matricule : {self.matricule} | Marque : {self.marque} | Couleur : {self.couleur}")

class parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoiture = []

    def entrerVoiture(self, voiture) -> None:
        if len(self.listeVoitures) >= self.capacite:
            print("Erreur : le parc est plein.")
            return

        self.listeVoitures.append(voiture)
        print(f"La voiture {voiture.matricule} est entrée dans le parc.")
        print(f"Places libres : {self.calculerNbrPlacesLibres()}")