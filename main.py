from modules import dci_fr, interact
from user.data.profil import profil as profil_module

def display_medicine_info(med):
    print(f"\n🧾 DCI : {med['dci']}")
    print(f"📦 Nom(s) commercial(aux) : {', '.join(med.get('region_names', {}).values())}")
    print(f"💊 Classe ATC : {med.get('class_atc', '❓')}")
    print(f"🔗 Interactions : {', '.join(med.get('interactions', [])) or 'Aucune connue'}")
    print(f"⛔ Contre-indications : {', '.join(med.get('contraindications', [])) or 'Non spécifiées'}")
    print(f"⚠️ Précautions : {', '.join(med.get('precautions', [])) or 'Non spécifiées'}")
    print(f"🤰 Avertissement grossesse : {'Oui' if med.get('pregnancy_warning') else 'Non'}")
    print(f"🏃 Substance dopante : {'Oui' if med.get('dopant') else 'Non'}")
    print(f"🧪 Allergènes : {', '.join(med.get('allergens', [])) or 'Aucun'}")
    print(f"🧬 Excipient(s) à risque : {', '.join(med.get('excipient_alert', [])) or 'Aucun'}")
    print(f"📚 Source : {med.get('monograph_source', 'Inconnue')}")

def lookup_medicine():
    name = input("\n🔍 Entrez un nom (DCI ou marque FR) : ").strip()
    med = dci_fr.get_full_medicine_by_name(name)
    if med:
        display_medicine_info(med)
    else:
        print("❌ Médicament non trouvé.")

def interaction_test():
    print("\n🔬 TEST D’INTERACTION")
    drug_a = input("Médicament 1 : ").strip()
    drug_b = input("Médicament 2 : ").strip()

    result = interact.check_interaction(drug_a, drug_b)
    if result is None:
        print("❌ Un des médicaments est inconnu.")
    elif result:
        print("⚠️ Interaction détectée entre les deux médicaments.")
    else:
        print("✅ Aucune interaction connue.")

def profil_menu():
    print("\n🩺 PROFIL SANTÉ")
    profil_obj = profil_module.charger_profil()
    if profil_obj:
        profil_obj.afficher()
    else:
        print("❌ Aucun profil chargé ou erreur lors du chargement.")

def main_menu():
    print("\n🧠 Pythie – Assistant Médicamenteux (mode test CLI)")
    print("----------------------------------------------------")
    print("1️⃣ Rechercher un médicament")
    print("2️⃣ Tester une interaction")
    print("3️⃣ Voir profil santé")
    print("4️⃣ Quitter")

    while True:
        choice = input("\nSélectionnez une option (1/2/3/4) : ").strip()
        if choice == "1":
            lookup_medicine()
        elif choice == "2":
            interaction_test()
        elif choice == "3":
            profil_menu()
        elif choice == "4":
            print("👋 Au revoir.")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    main_menu()
