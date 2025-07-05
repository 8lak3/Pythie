import json
import os

class ProfilSante:
    def __init__(self, identifiant, age, sexe, enceinte, poids_kg, taille_cm,
                 groupe_sanguin, pathologies, allergies, antecedents,
                 traitements, vaccinations, medecin_traitant, habitudes_vie):
        self.identifiant = identifiant
        self.age = age
        self.sexe = sexe
        self.enceinte = enceinte
        self.poids_kg = poids_kg
        self.taille_cm = taille_cm
        self.groupe_sanguin = groupe_sanguin
        self.pathologies = pathologies
        self.allergies = allergies
        self.antecedents = antecedents
        self.traitements = traitements
        self.vaccinations = vaccinations
        self.medecin_traitant = medecin_traitant
        self.habitudes_vie = habitudes_vie

    def to_dict(self):
        return self.__dict__

    def afficher(self):
        print(f"🩺 Profil de : {self.identifiant}")
        print(f"Âge : {self.age} ans")
        print(f"Sexe : {self.sexe}")
        print(f"Femme enceinte : {'Oui' if self.enceinte else 'Non'}")
        print(f"Poids : {self.poids_kg} kg - Taille : {self.taille_cm} cm")
        print(f"Groupe sanguin : {self.groupe_sanguin}")
        print(f"Pathologies : {', '.join(self.pathologies) if self.pathologies else 'Aucune'}")
        print(f"Allergies : {', '.join(self.allergies) if self.allergies else 'Aucune'}")
        print(f"Antécédents : {', '.join(self.antecedents) if self.antecedents else 'Aucun'}")
        print(f"Traitements en cours : {', '.join(self.traitements) if self.traitements else 'Aucun'}")
        print("Vaccinations :")
        for v, d in self.vaccinations.items():
            print(f"  - {v} : {d}")
        print(f"Médecin : {self.medecin_traitant['nom']} ({self.medecin_traitant['telephone']})")
        print("Habitudes de vie :")
        for k, v in self.habitudes_vie.items():
            print(f"  {k.capitalize()} : {v}")
        print("-" * 30)


def creer_profil_exemple():
    return ProfilSante(
        identifiant="patient_001",
        age=72,
        sexe="Femme",
        enceinte=False,
        poids_kg=68,
        taille_cm=165,
        groupe_sanguin="O+",
        pathologies=["Insuffisance rénale", "Hypertension"],
        allergies=["Pénicilline"],
        antecedents=["Appendicectomie", "Covid long"],
        traitements=["Lévothyrox"],
        vaccinations={
            "Covid": "2023-10-10",
            "Grippe": "2024-11-01"
        },
        medecin_traitant={
            "nom": "Dr Dupont",
            "telephone": "00 00 00 00 00"
        },
        habitudes_vie={
            "tabac": False,
            "alcool": "rare",
            "sport": "modéré"
        }
    )

def sauvegarder_profil(profil, nom_fichier=None):
    if not nom_fichier:
        # Chemin par défaut relatif au fichier
        nom_fichier = os.path.join(os.path.dirname(__file__), "profil.json")
    with open(nom_fichier, "w", encoding="utf-8") as f:
        json.dump(profil.to_dict(), f, indent=2, ensure_ascii=False)
    print(f"✅ Profil sauvegardé dans {nom_fichier}")

def charger_profil(nom_fichier=None):
    if not nom_fichier:
        nom_fichier = os.path.join(os.path.dirname(__file__), "profil.json")
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
        profil = ProfilSante(**data)
        return profil
    except Exception as e:
        print(f"❌ Erreur lors du chargement du profil : {e}")
        return None

if __name__ == "__main__":
    profil = creer_profil_exemple()
    profil.afficher()
    sauvegarder_profil(profil)
