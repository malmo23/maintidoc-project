# MAINTIDOC — ASSISTANT DOCUMENTAIRE MULTIMODAL & AGENTIQUE POUR LA MAINTENANCE
**Module :** IA Générative Multimodale — EMSI-2026  
**Enseignante :** Prof. Mariam CHERRABI  
**Équipe :** MALDANI & BOUJRADA  
**Membres de l'équipe (Binôme) :**  
- **Mostafa MALDANI** (Ingénierie & Data Science / Architecture RAG) — `maldanirachid2016@gmail.com`
- **Younes BOUJRADA** (Systèmes Agentiques, MCP & VLM) — `boujrada.younes@emsi.ma`

---

## 1. Objectif du Projet
MaintiDoc est un assistant intelligent d'aide à la décision pour techniciens et superviseurs de maintenance. Il combine :
- Un moteur **RAG Multimodal** (texte et vision) pour rechercher et citer avec précision les passages et figures des manuels officiels constructeurs.
- Une analyse visuelle directe par **modèle Vision-Langage (VLM)** open-weights (Qwen2.5-VL-7B-Instruct) pour identifier les équipements, voyants et anomalies à partir de photos d'atelier.
- Un workflow agentique orchestré avec **LangGraph** connecté à un serveur **MCP (Model Context Protocol)** pour consulter l'historique d'interventions et préparer des tickets de maintenance.
- Une **boucle d'approbation humaine obligatoire (Human-in-the-loop)** interdisant toute écriture ou création de ticket sans validation explicite.

---

## 2. Contenu de cette Archive (L1_MaintiDoc_MALDANI.zip)
L'archive respecte rigoureusement la nomenclature requise :
```text
L1_MaintiDoc_MALDANI/
├── L1_MaintiDoc_MALDANI.pdf               # Rapport PDF officiel (12 pages, parties 2.1 à 2.6)
├── L1_MaintiDoc_MALDANI_LienGitHub.txt    # URL vers le dépôt GitHub public de l'équipe
├── README.md                        # Présentation synthétique du projet et de l'équipe
└── L1_MaintiDoc_MALDANI_Corpus/           # Corpus multimodal validé (38 documents & schémas)
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
