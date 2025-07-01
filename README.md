

---
<p align="center">
  <strong style="font-size: 1.6rem;">P&nbsp;&nbsp;Y&nbsp;&nbsp;T&nbsp;&nbsp;H&nbsp;&nbsp;I&nbsp;&nbsp;E</strong><br>
  <em>Pharmaceutical Help Agent – Personal Medication Guide (FR-Focused)</em>
</p>

---
---

# 🧠 Pythie – Personal Medication Guide

**Pythie** is a privacy-first, open-source assistant that helps patients understand their medications, detect general alerts, and access verified medical sources — without collecting any personal data.

🔍 Simple  
🔐 Respectful  
🌐 Local-first, with optional online lookups

---

## 🎯 Vision

Pythie empowers patients with clarity on medications and treatments, based on trustworthy sources (ANSM, WHO, WADA).  
It does not replace a doctor — it **guides, informs, and protects**.

---

## 🧱 Modules (planned)

- `dci_fr` – French DCI ↔ Brand mapping (via BDPM)
- `alias_international` – Foreign brand aliases by country
- `interact` – Drug interaction checker (via ANSM Thesaurus)
- `contra` – Global contraindications (pregnancy, allergies, renal failure)
- `alerts` – General alerts based on patient profile
- `calendar` *(optional)* – Medication intake planner
- `doping` *(optional)* – WADA substance checker

---

## 🛡️ Privacy First

- No login  
- No cloud  
- No tracking

📁 All data is stored locally as `.json` files.  
External sources are accessed only via user-initiated links.

---

## 📁 Structure

pythie/

├── main.py

├── modules/

├── data/

├── user/

├── docs/

---

## 📚 Official Sources

- ANSM / BDPM (France)
- WHO (ATC / DDD index)
- EMA (Europe)
- WADA (Banned substances list)

➡️ See [`docs/sources.md`](docs/sources.md) for full details

---

## 📄 License

Apache 2.0 License  
Based on public sources: ANSM, BDPM, WHO, EMA, WADA

---

## 📊 Development Roadmap

➡️ [`docs/roadmap.md`](docs/roadmap.md)

---

## 💵 Donations

 If you would like to make a donation 
 
 🪙 XMR: 85sZTW44ER3MKnbLhmLwYggc6BjjVW56kSbNN1T79DLDgdg8rgBSXzKfPtdXktXZBZ9s8ttCTgzMiK21k7XYXZsu4cReTMo 
 
 Thank you!


