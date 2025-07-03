from modules import dci_fr

print("🧪 Pythie – Medication Lookup")
print("-----------------------------")

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


while True:
    user_input = input("\n🔎 Entrez un nom de médicament (DCI ou FR), ou 'exit' : ").strip()

    if user_input.lower() == "exit":
        print("👋 Au revoir !")
        break

    med = dci_fr.get_full_medicine_by_name(user_input)
    if med:
        display_medicine_info(med)
    else:
        print("❌ Médicament non trouvé.")
