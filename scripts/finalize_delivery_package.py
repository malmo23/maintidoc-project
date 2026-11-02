"""
Script de finalisation et d'empaquetage du Livrable 1 MaintiDoc
- Gère l'équipe : Mostafa MALDANI et Younes BOUJRADA
- Prépare les dossiers de rendu conformes : L1_MaintiDoc_MALDANI_BOUJRADA/ et L1_MaintiDoc_MALDANI/
- Crée le dossier maintidoc/ prêt pour Git (.gitignore, docs/diagrammes/, corpus/, README.md)
- Génère les archives ZIP finales avec vérifications strictes
"""
import os
import shutil
import zipfile
import csv
import re

MEMBERS = [
    {"nom": "Mostafa MALDANI", "role": "Ingénierie & Data Science / Architecture RAG", "email": "maldanirachid2016@gmail.com"},
    {"nom": "Younes BOUJRADA", "role": "Systèmes Agentiques, MCP & VLM", "email": "boujrada.younes@emsi.ma"}
]

GITHUB_URL = "https://github.com/malmo23/maintidoc-project"
GITHUB_REPO_DIR = "maintidoc"

def package_for_team(team_id):
    zip_root_dir = f"L1_MaintiDoc_{team_id}"
    zip_archive_name = f"L1_MaintiDoc_{team_id}.zip"
    
    print(f"\n=======================================================")
    print(f"--- Préparation du rendu pour : {zip_root_dir} ---")
    print(f"=======================================================")
    os.makedirs(zip_root_dir, exist_ok=True)
    
    # 1.0 Nettoyage de doublons PDF éventuels (un seul rapport officiel)
    obsolete_pdf = os.path.join(zip_root_dir, f"L1_MaintiDoc_{team_id}_Rapport.pdf")
    if os.path.exists(obsolete_pdf):
        os.remove(obsolete_pdf)
        print(f"Supprimé doublon : {obsolete_pdf}")

    # 1.1 Fichier Lien GitHub
    lien_path = os.path.join(zip_root_dir, f"L1_MaintiDoc_{team_id}_LienGitHub.txt")
    with open(lien_path, "w", encoding="utf-8") as f:
        f.write(f"{GITHUB_URL}\n")
    print(f"Créé : {lien_path}")

    # 1.2 README.md
    members_str = "\n".join([f"- **{m['nom']}** ({m['role']}) — `{m['email']}`" for m in MEMBERS])
    readme_content = f"""# MAINTIDOC — ASSISTANT DOCUMENTAIRE MULTIMODAL & AGENTIQUE POUR LA MAINTENANCE
**Module :** IA Générative Multimodale — EMSI-2026  
**Enseignante :** Prof. Mariam CHERRABI  
**Équipe :** MALDANI & BOUJRADA  
**Membres de l'équipe (Binôme) :**  
{members_str}

---

## 1. Objectif du Projet
MaintiDoc est un assistant intelligent d'aide à la décision pour techniciens et superviseurs de maintenance. Il combine :
- Un moteur **RAG Multimodal** (texte et vision) pour rechercher et citer avec précision les passages et figures des manuels officiels constructeurs.
- Une analyse visuelle directe par **modèle Vision-Langage (VLM)** open-weights (Qwen2.5-VL-7B-Instruct) pour identifier les équipements, voyants et anomalies à partir de photos d'atelier.
- Un workflow agentique orchestré avec **LangGraph** connecté à un serveur **MCP (Model Context Protocol)** pour consulter l'historique d'interventions et préparer des tickets de maintenance.
- Une **boucle d'approbation humaine obligatoire (Human-in-the-loop)** interdisant toute écriture ou création de ticket sans validation explicite.

---

## 2. Contenu de cette Archive ({zip_archive_name})
L'archive respecte rigoureusement la nomenclature requise :
```text
{zip_root_dir}/
├── {zip_root_dir}.pdf               # Rapport PDF officiel (12 pages, parties 2.1 à 2.6)
├── {zip_root_dir}_LienGitHub.txt    # URL vers le dépôt GitHub public de l'équipe
├── README.md                        # Présentation synthétique du projet et de l'équipe
└── {zip_root_dir}_Corpus/           # Corpus multimodal validé (38 documents & schémas)
    ├── inventaire.csv                       # Registre UTF-8 exhaustif des 38 documents (20 colonnes)
    ├── prompts_corpus.md                    # Traçabilité complète des prompts P01 à P15
    └── documents/
        ├── famille_1/                       # 13 documents Canon EOS R50 (PDF, MD, Scans)
        ├── famille_2/                       # 13 documents Epson SureColor SC-P700
        └── images/                          # 12 schémas techniques et photographies annotées
```

---

## 3. Structure du Dépôt Git (maintidoc/)
Le dépôt GitHub accessible à l'enseignante reprend l'organisation préconisée :
```text
maintidoc/
├── README.md                                # Description et instructions d'installation
├── .gitignore                               # Exclusion des secrets (.env), caches et binaires
├── docs/
│   └── diagrammes/                          # Sources des diagrammes d'architecture (PNG / Mermaid)
├── src/                                     # Code application Streamlit et assistant CLI
└── corpus/
    ├── inventaire.csv                       # Registre du corpus
    ├── prompts_corpus.md                    # Traçabilité des prompts
    └── documents/
        ├── famille_1/                       # Canon EOS R50
        ├── famille_2/                       # Epson SureColor SC-P700
        └── images/                          # Éléments visuels
```

---

## 4. Équipements Couverts par le Corpus
1. **Famille 1 : Boîtier Photo Hybride Canon EOS R50** (Capteur CMOS APS-C 24.2 MP, monture RF, processeur DIGIC X, batterie LP-E17).
2. **Famille 2 : Imprimante Jet d'Encre Epson SureColor SC-P700** (Tête PrecisionCore 10 canaux, encres UltraChrome PRO10, boîtier de maintenance C12C935711).
"""
    readme_path = os.path.join(zip_root_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content.strip() + "\n")
    print(f"Créé : {readme_path}")

    # 1.3 Corpus
    target_corpus_dir = os.path.join(zip_root_dir, f"{zip_root_dir}_Corpus")
    base_corpus_src = "maintidoc/corpus"
    if not os.path.exists(base_corpus_src):
        base_corpus_src = "L1_MaintiDoc_MALDANI/L1_MaintiDoc_MALDANI_Corpus"
        
    if target_corpus_dir != base_corpus_src:
        if os.path.exists(target_corpus_dir):
            shutil.rmtree(target_corpus_dir)
        shutil.copytree(base_corpus_src, target_corpus_dir)
        print(f"Copié corpus : {base_corpus_src} -> {target_corpus_dir}")

    # 1.4 Vérifications 1:1 inventaire.csv
    csv_file = os.path.join(target_corpus_dir, "inventaire.csv")
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        
    print(f"Nombre de lignes dans inventaire.csv : {len(reader)}")
    if len(reader) != 38:
        raise ValueError(f"Attendu 38 lignes, obtenu {len(reader)}")
        
    for r in reader:
        p = os.path.join(target_corpus_dir, r["fichier"])
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            raise ValueError(f"Fichier manquant ou vide : {p}")
    print("-> Cohérence 1:1 inventaire.csv / fichiers disque validée.")

    # 1.5 Scan anti-secrets
    secret_regex = re.compile(r"(ghp_[a-zA-Z0-9]{20,}|sk-[a-zA-Z0-9]{20,}|AIzaSy[a-zA-Z0-9_-]{33}|API_KEY\s*=\s*['\"][^'\"]+)", re.IGNORECASE)
    for root, dirs, files in os.walk(zip_root_dir):
        for fl in files:
            if fl.endswith((".py", ".txt", ".md", ".csv")):
                fpath = os.path.join(root, fl)
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    if secret_regex.search(content):
                        raise ValueError(f"Alerte sécurité : Secret détecté dans {fpath}")
    print("-> Scan de sécurité réussi : aucun secret détecté.")

    # 1.6 Compression ZIP
    if os.path.exists(zip_archive_name):
        os.remove(zip_archive_name)
        
    with zipfile.ZipFile(zip_archive_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(zip_root_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, start=".")
                zf.write(full_path, arcname=rel_path)

    zip_size_mb = os.path.getsize(zip_archive_name) / (1024 * 1024)
    print(f"Archive {zip_archive_name} créée avec succès ({zip_size_mb:.2f} Mo).")

    # 1.7 Contrôle strict du contenu du ZIP
    with zipfile.ZipFile(zip_archive_name, "r") as zf:
        nl = zf.namelist()
        print(f"Nombre total de fichiers dans l'archive ZIP : {len(nl)}")
        bad_entries = [e for e in nl if not e.startswith(f"{zip_root_dir}/")]
        if bad_entries:
            raise ValueError(f"Fichiers hors du dossier racine dans le ZIP : {bad_entries}")
        print(f"-> Règle du dossier unique racine '{zip_root_dir}/' respectée !")

def finalize():
    # 1. Packaging pour MALDANI_BOUJRADA et MALDANI
    package_for_team("MALDANI_BOUJRADA")
    package_for_team("MALDANI")
    
    # 2. Mise à jour de maintidoc/ (dépôt Git)
    print("\n--- Synchronisation du dépôt Git (maintidoc/) ---")
    shutil.copy2("L1_MaintiDoc_MALDANI_BOUJRADA/README.md", os.path.join(GITHUB_REPO_DIR, "README.md"))
    print("maintidoc/README.md mis à jour.")

if __name__ == "__main__":
    finalize()
