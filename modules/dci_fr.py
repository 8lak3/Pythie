import json
import os

# Charger medicines.json depuis ../data/
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "medicines.json")
with open(data_path, "r", encoding="utf-8") as f:
    medicines = json.load(f)

def get_dci_from_brand(brand_name):
    """
    Retourne la DCI correspondant à un nom commercial français (insensible à la casse).
    """
    brand_name = brand_name.lower()
    for med in medicines:
        fr_name = med.get("region_names", {}).get("FR", "").lower()
        if fr_name == brand_name:
            return med["dci"]
    return None

def get_brand_from_dci(dci):
    """
    Retourne le nom commercial français pour une DCI donnée.
    """
    dci = dci.lower()
    for med in medicines:
        if med["dci"].lower() == dci:
            return med.get("region_names", {}).get("FR")
    return None
