from modules import dci_fr, interact

def alert_interactions(traitements):
    """Retourne une liste de couples (med1, med2) présentant une interaction."""
    interactions = []
    for i in range(len(traitements)):
        for j in range(i + 1, len(traitements)):
            if interact.check_interaction(traitements[i], traitements[j]):
                interactions.append((traitements[i], traitements[j]))
    return interactions

def alert_allergies(traitements, allergies_patient):
    """Retourne la liste des médicaments contenant des allergènes présents dans le profil."""
    alertes = []
    allergies_patient_lower = [a.lower() for a in allergies_patient]
    for med_name in traitements:
        med = dci_fr.get_full_medicine_by_name(med_name)
        if not med:
            continue
        allergens = med.get("allergens", [])
        for allergen in allergens:
            if allergen.lower() in allergies_patient_lower:
                alertes.append(med_name)
                break
    return alertes

def alert_contraindications(traitements, pathologies_patient):
    """Retourne la liste des médicaments contre-indiqués par les pathologies."""
    alertes = []
    pathologies_lower = [p.lower() for p in pathologies_patient]
    for med_name in traitements:
        med = dci_fr.get_full_medicine_by_name(med_name)
        if not med:
            continue
        contra = med.get("contraindications", [])
        for c in contra:
            # Simplification : on compare directement les chaînes en lowercase
            if c.lower() in pathologies_lower:
                alertes.append(med_name)
                break
    return alertes

def alert_pregnancy(traitements, enceinte):
    """Retourne la liste des médicaments à risque pendant la grossesse si enceinte."""
    if not enceinte:
        return []
    alertes = []
    for med_name in traitements:
        med = dci_fr.get_full_medicine_by_name(med_name)
        if not med:
            continue
        if med.get("pregnancy_warning"):
            alertes.append(med_name)
    return alertes
