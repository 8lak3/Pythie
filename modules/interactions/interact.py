import json
import os
from modules import dci_fr

data_path = os.path.join(os.path.dirname(__file__), "..", "data", "medicines.json")
with open(data_path, "r", encoding="utf-8") as f:
    medicines = json.load(f)

def check_interaction(name1, name2):
    drug1 = dci_fr.get_full_medicine_by_name(name1)
    drug2 = dci_fr.get_full_medicine_by_name(name2)

    if not drug1 or not drug2:
        return None

    dci1 = drug1["dci"].lower()
    dci2 = drug2["dci"].lower()

    interactions = [i.lower() for i in drug1.get("interactions", [])]

    return dci2 in interactions
