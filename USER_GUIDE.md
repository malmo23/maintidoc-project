# GUIDE D'UTILISATION DU PROJET MAINTIDOC & MODÈLE LOCAL QWEN2.5-VL-7B
**Équipe Projet (Binôme) :** Mostafa MALDANI & Younes BOUJRADA (EMSI-2026)

Ce guide explique comment exécuter, tester et utiliser le projet **MaintiDoc** avec le modèle de vision-langage **Qwen2.5-VL-7B-Instruct** déjà téléchargé sur votre machine.

---

## 1. Localisation et Statut du Modèle Téléchargé

Le modèle officiel recommandé par le projet est déjà présent localement sur votre disque :
* **Emplacement GGUF :** `C:\Users\malda\.lmstudio\models\lmstudio-community\Qwen2.5-VL-7B-Instruct-GGUF\`
* **Fichiers :**
  - Modèle quantifié : `Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf` (4,68 Go)
  - Projecteur multimodal : `mmproj-model-f16.gguf` (1,35 Go)
* **Serveur d'inférence local :** LM Studio (`lms.exe`) servant une API standard compatible OpenAI sur `http://127.0.0.1:1234/v1`.

---

## 2. Commandes de Démarrage Rapide

### Étape 1 : Démarrer le serveur local et charger Qwen2.5-VL
Ouvrez un terminal PowerShell et exécutez :
```powershell
# 1. Démarrer le serveur LM Studio
& "C:\Users\malda\.lmstudio\bin\lms.exe" server start

# 2. Charger le modèle Qwen2.5-VL (optimisé en contexte 4096)
& "C:\Users\malda\.lmstudio\bin\lms.exe" load qwen/qwen2.5-vl-7b -c 4096 --gpu off -y

# 3. Vérifier le statut
& "C:\Users\malda\.lmstudio\bin\lms.exe" status
```
> Le modèle s'initialise en environ 15 à 20 secondes.

---

## 3. Utilisation de l'Assistant MaintiDoc

Vous disposez de deux interfaces pour utiliser l'assistant :

### Option A : Interface Web Graphique (Streamlit)
Pour une expérience interactive complète avec prévisualisation des schémas d'atelier, sélection de pannes et simulation du point de contrôle de création de ticket (Human-in-the-loop) :
```powershell
streamlit run src/app_streamlit.py
```
*L'application s'ouvre automatiquement dans votre navigateur sur `http://localhost:8501`.*

**Fonctionnalités de l'interface Streamlit :**
1. **Sélection de l'équipement :** Basculez entre le *Canon EOS R50* et l'*Epson SureColor SC-P700*.
2. **Choix de l'image d'atelier :** Sélectionnez l'un des 12 schémas du corpus ou téléversez une photo personnelle.
3. **Questions d'atelier préréglées ou libres :** Codes erreurs, voyants d'alarmes, procédures de nettoyage.
4. **Analyse multimodale Qwen2.5-VL :** Le modèle analyse l'image et le contexte documentaire sourcé.
5. **Validation humaine (Point C3) :** Bouton d'approbation explicite avant la création de ticket dans la GMAO via MCP.

---

### Option B : Assistant en Ligne de Commande (CLI)
Pour des tests rapides en console :
```powershell
python src/maintidoc_assistant.py
```
Le script propose un menu interactif avec 4 scénarios d'atelier prédéfinis et un mode de saisie libre.

---

## 4. Organisation des Dossiers du Projet

| Dossier / Fichier | Rôle & Contenu |
| :--- | :--- |
| **`L1_MaintiDoc_MALDANI_BOUJRADA.zip`** | **L'archive officielle à déposer sur Classroom** (rapport 12 pages avec Mostafa MALDANI et Younes BOUJRADA, lien GitHub, README et corpus complet). |
| **`L1_MaintiDoc_MALDANI.zip`** | Archive alternative conforme (alias simple). |
| **`L1_MaintiDoc_MALDANI_BOUJRADA/`** | Dossier racine conforme contenant les éléments requis. |
| **`maintidoc/`** | **Dépôt Git prêt à être publié** (`.gitignore`, `docs/diagrammes/`, `corpus/`, `src/`). |
| **`docs/diagrammes/`** | Les 4 schémas d'architecture haute résolution générés pour le rapport. |
| **`src/`** | Code source de l'assistant (`maintidoc_assistant.py`, `app_streamlit.py`). |

---

## 5. Publication du Dépôt GitHub

Pour publier le dépôt Git sur votre compte GitHub (`malmo23`) :
```powershell
cd maintidoc
git remote set-url origin https://github.com/malmo23/maintidoc-project.git
# ou si l'origine n'est pas encore ajoutée :
# git remote add origin https://github.com/malmo23/maintidoc-project.git
git push -u origin main
```
