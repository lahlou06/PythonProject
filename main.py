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

    def sortirVoiture(self, voiture: voiture) -> None:
        # Vérifier si la voiture est présente
        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                self.listeVoitures.remove(v)
                print(f"La voiture {voiture.matricule} est sortie du parc.")

    def calculerNbrPlacesLibres(self) -> int:
        return self.capacite - len(self.listeVoitures)

    parc = parc(1, "Toronto", 3)
v1 = voiture("ABC 123", "Toyota", "Rouge")
v2 = voiture("AYAX 410", "Honda", "Noir")
v3 = voiture("OOOSAM", "Ford", "Blanc")
v4 = voiture("5OFL01", "BMW", "Bleu")
parc.entrerVoiture(v1)
parc.entrerVoiture(v2)
parc.entrerVoiture(v3)


