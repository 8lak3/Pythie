
---

<p align="center">
  <strong style="font-size: 1.6rem;">P&nbsp;&nbsp;Y&nbsp;&nbsp;T&nbsp;&nbsp;H&nbsp;&nbsp;I&nbsp;&nbsp;E</strong><br>
  <em>Pharmaceutical Help Agent – Personal Medication Guide (FR-Focused)</em>
</p>

---

# 🧠 Pythie – Personal Medication Guide

**Pythie** is a privacy-first, open-source assistant that helps patients better understand their medications, detect basic health risks, and access verified medical sources — all without collecting personal data.

🔍 Simple  
🔐 Respectful  
🌐 Local-first, with optional online access

---

## 🎯 Vision

Pythie empowers patients with clarity on treatments, based on trusted medical data (ANSM, WHO, WADA).  
It does not replace a healthcare provider — it **guides, informs, and protects**.

---

## 🧱 Planned Modules

- `dci_fr` – French DCI ↔ Brand mapping (via BDPM)
- `alias_international` – International brand name matching
- `interact` – Drug interaction checker (from ANSM Thesaurus)
- `contra` – Global contraindications (pregnancy, allergies, etc.)
- `alerts` – Warnings based on user profile (age, chronic illness, etc.)
- `calendar` *(optional)* – Treatment reminder and intake calendar
- `doping` *(optional)* – WADA doping substance checker

---

## 🛡️ Privacy First

- No account required  
- No cloud storage  
- No tracking

📁 All user data is stored locally in `.json` files.  
Online sources are accessed only through manual clicks by the user.

---

## 📁 Project Structure

pythie/

├── main.py

├── modules/

├── data/

├── user/

└── docs/

---

## 📚 Official Sources

- ANSM / BDPM (France)
- WHO (ATC / DDD index)
- EMA (Europe)
- WADA (Prohibited substance list)

📄 See [`docs/sources.en.md`](docs/sources.en.md) for full details


---

## 📄 License

Distributed under the **Apache 2.0 License**  
Based on official public data: ANSM, BDPM, WHO, EMA, WADA

---

## 📊 Development Roadmap

🧱 [`docs/roadmap.en.md`](roadmap.en.md)

---

## 🙏 Support

If you'd like to support the project:

- ⭐ Star the repository  
- 🧑‍💻 Contribute or suggest improvements  
- 📢 Share the project  
- 🪙 Or donate anonymously via Monero (XMR)

---

## 💵 Donation 

If you would like to make a donation 
 
🪙 XMR: 85sZTW44ER3MKnbLhmLwYggc6BjjVW56kSbNN1T79DLDgdg8rgBSXzKfPtdXktXZBZ9s8ttCTgzMiK21k7XYXZsu4cReTMo 
 
Thank you!

---

## 👤 Author / Maintainer

This project is developed and maintained by @8lak3 (Blake)

Feedback and contributions are welcome via [GitHub issues] (https://github.com/8lak3/pythie/issues)


---

Thank you for supporting open, privacy-respecting tools 🙏

---

📝 This project is also available in French: [README.fr.md](README.fr.md)

