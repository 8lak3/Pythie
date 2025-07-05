from modules import dci_fr, interact

def alert_interactions(med_names):
    """
    Vérifie toutes les interactions possibles entre une liste de médicaments.
    med_names : liste de noms (DCI ou marque FR)
    Retourne une liste de tuples (med1, med2) pour les interactions détectées.
    """
    alerts = []
    n = len(med_names)
    for i in range(n):
        for j in range(i + 1, n):
            res = interact.check_interaction(med_names[i], med_names[j])
            if res:
                alerts.append((med_names[i], med_names[j]))
    return alerts

def alert_allergies(med_names, allergies):
    """
    Vérifie si un médicament contient un allergène présent dans la liste d'allergies.
    med_names : liste de noms (DCI ou marque FR)
    allergies : liste d’allergies du patient (ex : ['Pénicilline'])
    Retourne une liste des médicaments posant problème.
    """
    meds_with_allergies = []
    for med_name in med_names:
        med = dci_fr.get_full_medicine_by_name(med_name)
        if med:
            allergens = med.get("allergens", [])
            for allergy in allergies:
                # On compare en minuscules pour éviter problème de casse
                if any(allergy.lower() == a.lower() for a in allergens):
                    meds_with_allergies.append(med_name)
                    break
    return meds_with_allergies

def alert_contraindications(med_names, pathologies):
    """
    Vérifie si un médicament est contre-indiqué avec une pathologie du patient.
    med_names : liste de noms (DCI ou marque FR)
    pathologies : liste des pathologies du patient
    Retourne une liste des médicaments contre-indiqués.
    """
    contraindicated = []
    for med_name in med_names:
        med = dci_fr.get_full_medicine_by_name(med_name)
        if med:
            ci = med.get("contraindications", [])
            for patho in pathologies:
                if any(patho.lower() == c.lower() for c in ci):
                    contraindicated.append(med_name)
                    break
    return contraindicated

def alert_pregnancy(med_names, enceinte):
    """
    Si la personne est enceinte, retourne les médicaments à risque pendant la grossesse.
    med_names : liste de noms (DCI ou marque FR)
    enceinte : booléen
    Retourne la liste des médicaments à risque.
    """
    if not enceinte:
        return []
    risky_meds = []
    for med_name in med_names:
        med = dci_fr.get_full_medicine_by_name(med_name)
        if med and med.get("pregnancy_warning", False):
            risky_meds.append(med_name)
    return risky_meds
