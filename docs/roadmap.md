# 🗺️ Pythie – Feuille de route / Roadmap

Cette feuille de route (roadmap) décrit les étapes prévues du développement de **Pythie**, de la phase de réflexion jusqu'aux premiers modules utilisables.

---

## 📍 Phase 1 – Préparation et fondations (✅ en cours)

- [x] Définir la vision du projet (philosophie, objectifs)
- [x] Créer le dépôt GitHub
- [x] Écrire les fichiers `README.md` et `README.fr.md`
- [x] Structurer le dépôt (dossiers : modules, data, user, docs)
- [ ] Établir les formats des fichiers `.json` (médicaments, profil, alertes)
- [ ] Convertir les données BDPM de base (CSV → JSON)

---

## ⚙️ Phase 2 – Modules essentiels

- [ ] `dci_fr` : Correspondance DCI ↔ spécialités (via BDPM)
- [ ] `interact` : Vérification d’interactions simples (à partir du thésaurus ANSM)
- [ ] `alerts` : Alertes générales selon le profil patient (grossesse, allergies…)

---

## 🔍 Phase 3 – Modules avancés (enrichissement)

- [ ] `alias_international` : Marques étrangères (par pays)
- [ ] `contra` : Contre-indications générales (pathologies courantes)
- [ ] `calendar` *(optionnel)* : Calendrier de prise de traitements
- [ ] `doping` *(optionnel)* : Vérification substances interdites (WADA)

---

## 🧠 Phase 4 – Qualité et ouverture

- [ ] Organiser les fichiers pour faciliter les contributions
- [ ] Ajouter des commentaires explicatifs aux fichiers `.json`
- [ ] Rédiger des exemples (scénarios de test)
- [ ] Fournir un script simple pour convertir BDPM en JSON

---

## 🚀 Phase 5 – Première version publique

- [ ] Publier une version 0.1.0 (au minimum 2 modules fonctionnels)
- [ ] Ouvrir des issues de contribution
- [ ] Créer une mini-annonce (GitHub, X/Twitter, etc.)
- [ ] Ajouter un changelog

---

## 💬 Idées futures

- Interface en ligne de commande plus fluide
- Interface graphique minimale (Tkinter ou autre)
- Export PDF d’une fiche médicament
- Système de QR-code pour ordonnances *(si possible hors-ligne)*
- Traductions : anglais, espagnol, etc.

---

## 💖 Soutenir le projet

Vous pouvez soutenir Pythie de plusieurs façons :

- ⭐ Mettre une étoile sur le dépôt GitHub  
- 💬 Partager des retours via les issues  
- 🧑‍💻 Proposer des améliorations  
- 🪙 Faire un don Monero (XMR)
  
🪙 XMR: 85sZTW44ER3MKnbLhmLwYggc6BjjVW56kSbNN1T79DLDgdg8rgBSXzKfPtdXktXZBZ9s8ttCTgzMiK21k7XYXZsu4cReTMo

---

Merci pour votre soutien aux outils de santé éthiques et ouverts 🙏

