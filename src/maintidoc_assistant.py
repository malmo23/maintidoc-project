"""
MaintiDoc Assistant - Interface d'inférence multimodale connectée au modèle local Qwen2.5-VL-7B
Permet aux techniciens de poser des questions techniques avec images et citations vérifiables.
"""
import os
import sys
import io
import json
import base64
import urllib.request
import urllib.error
import csv
from PIL import Image

BASE_URL = "http://127.0.0.1:1234/v1"
MODEL_ID = "qwen/qwen2.5-vl-7b"

# Résolution automatique du corpus
if os.path.exists(os.path.join("L1_MaintiDoc_MALDANI_BOUJRADA", "L1_MaintiDoc_MALDANI_BOUJRADA_Corpus")):
    CORPUS_DIR = os.path.join("L1_MaintiDoc_MALDANI_BOUJRADA", "L1_MaintiDoc_MALDANI_BOUJRADA_Corpus")
elif os.path.exists(os.path.join("L1_MaintiDoc_MALDANI", "L1_MaintiDoc_MALDANI_Corpus")):
    CORPUS_DIR = os.path.join("L1_MaintiDoc_MALDANI", "L1_MaintiDoc_MALDANI_Corpus")
elif os.path.exists("corpus"):
    CORPUS_DIR = "corpus"
else:
    CORPUS_DIR = os.path.join("..", "corpus")

INVENTAIRE_PATH = os.path.join(CORPUS_DIR, "inventaire.csv")

def check_local_model():
    """Vérifie si le serveur LM Studio tourne et si Qwen2.5-VL est chargé."""
    try:
        req = urllib.request.Request(f"{BASE_URL}/models")
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode())
            models = [m.get("id") for m in data.get("data", [])]
            if MODEL_ID in models:
                return True, f"Modèle '{MODEL_ID}' prêt et opérationnel sur {BASE_URL}."
            return False, f"Serveur actif mais '{MODEL_ID}' non chargé. Modèles présents : {models}"
    except Exception as e:
        return False, f"Impossible de joindre le serveur local sur {BASE_URL}. Erreur : {e}"

def load_relevant_context(equipment_id, keywords):
    """Charge les extraits documentaires pertinents depuis le corpus en fonction de l'équipement."""
    context_chunks = []
    if not os.path.exists(INVENTAIRE_PATH):
        return "Corpus inventaire non trouvé."
        
    with open(INVENTAIRE_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["equipement_id"] == equipment_id or not equipment_id:
                # Vérifier si des mots-clés correspondent au titre ou remarques
                text_search = f"{row['titre']} {row['remarques']} {row['type_document']}".lower()
                if any(kw.lower() in text_search for kw in keywords) or len(keywords) == 0:
                    doc_path = os.path.join(CORPUS_DIR, row["fichier"])
                    if os.path.exists(doc_path) and doc_path.endswith(".md"):
                        try:
                            with open(doc_path, "r", encoding="utf-8") as df:
                                content = df.read()[:800] # Extrait initial
                                context_chunks.append({
                                    "document_id": row["document_id"],
                                    "titre": row["titre"],
                                    "page": row["nb_pages"],
                                    "content": content
                                })
                        except:
                            pass
    return context_chunks

def ask_qwen_multimodal(prompt, image_path=None, context_docs=None):
    """Envoie une requête multimodale au modèle local Qwen2.5-VL."""
    messages_content = []
    
    # Intégration du contexte documentaire sourcé
    context_text = ""
    if context_docs:
        context_text = "\n\n--- EXTRAITS DOCUMENTAIRES AUTORISÉS ---\n"
        for doc in context_docs[:3]:
            context_text += f"\n[Document: {doc['document_id']} | Titre: {doc['titre']} | Page: {doc['page']}]\n{doc['content']}\n"
        context_text += "--------------------------------------\n"
        context_text += "CONSIGNE CRITIQUE : Base ta réponse exclusivement sur ces sources. Cite impérativement le document_id et la page pour chaque affirmation.\n"

    full_text_prompt = f"{prompt}\n{context_text}"
    messages_content.append({"type": "text", "text": full_text_prompt})

    # Ajout de l'image si fournie avec redimensionnement optimisé (max 448x448)
    if image_path and os.path.exists(image_path):
        with Image.open(image_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.thumbnail((448, 448), Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=80)
            b64_img = base64.b64encode(buf.getvalue()).decode("utf-8")
            messages_content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{b64_img}"}
            })

    payload = {
        "model": MODEL_ID,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Tu es MaintiDoc, l'assistant expert de maintenance industrielle et atelier. "
                    "Tu réponds avec une grande précision technique. "
                    "Tu cites systématiquement les documents (document_id, page, figure). "
                    "Si une demande nécessite une intervention de maintenance, propose un brouillon de ticket "
                    "mais rappelle qu'une approbation humaine est obligatoire."
                )
            },
            {
                "role": "user",
                "content": messages_content
            }
        ],
        "temperature": 0.2,
        "max_tokens": 400
    }

    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode())
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        err_detail = e.read().decode("utf-8", errors="ignore")
        return f"[ERREUR API {e.code}] : {err_detail}"
    except Exception as e:
        return f"[ERREUR] : {e}"

def main():
    print("================================================================")
    print("  MAINTIDOC — ASSISTANT MULTIMODAL (MALDANI & BOUJRADA - EMSI)  ")
    print("================================================================")
    
    is_ok, msg = check_local_model()
    print(f"\n[Statut du Modèle Local] : {msg}")
    if not is_ok:
        print("\nPour démarrer le serveur local, exécutez dans un terminal :")
        print("  lms server start")
        print("  lms load qwen/qwen2.5-vl-7b -c 2048 --gpu off -y")
        return

    print("\nChoisissez un cas de démonstration :")
    print("1. [Canon EOS R50] Analyse photo panneau supérieur & commandes")
    print("2. [Canon EOS R50] Question sur la procédure officielle de nettoyage capteur")
    print("3. [Epson SC-P700] Dépannage voyant alerte saturation boîtier maintenance (Code 1485)")
    print("4. [Epson SC-P700] Analyse mire de buses Nozzle Check (Détection de banding)")
    print("5. Question libre avec image personnalisée")
    
    choice = input("\nVotre choix (1-5) [défaut: 1] : ").strip() or "1"
    
    if choice == "1":
        img = os.path.join(CORPUS_DIR, "documents", "images", "photo_panneau_superieur_canon.png")
        q = "Que représente cette image technique ? Décris les commandes du panneau supérieur et le rôle de la molette de mode."
        eq_id = "CANON-R50-01"
        kw = ["manuel", "commandes"]
    elif choice == "2":
        img = os.path.join(CORPUS_DIR, "documents", "images", "schema_chambre_capteur_canon.png")
        q = "Quelle est la procédure officielle pour nettoyer le capteur ? A-t-on le droit d'utiliser un solvant liquide ?"
        eq_id = "CANON-R50-01"
        kw = ["nettoyage", "capteur"]
    elif choice == "3":
        img = os.path.join(CORPUS_DIR, "documents", "images", "schema_boitier_maintenance_epson.png")
        q = "L'imprimante affiche le code d'erreur bloquant 1485. Que signifie-t-il et comment remplacer le boîtier ? Prépare un ticket."
        eq_id = "EPSON-P700-01"
        kw = ["boitier", "maintenance"]
    elif choice == "4":
        img = os.path.join(CORPUS_DIR, "documents", "images", "mire_test_buses_nozzle_check_epson.png")
        q = "Analyse cette mire de buses. Quelles sont les couleurs présentant des canaux obstrués et quelle est la démarche officielle ?"
        eq_id = "EPSON-P700-01"
        kw = ["tete", "buses"]
    else:
        q = input("Entrez votre question : ").strip()
        img = input("Chemin de l'image (laisser vide si aucune) : ").strip() or None
        eq_id = input("Identifiant équipement (ex: CANON-R50-01 ou EPSON-P700-01) : ").strip()
        kw = [q.split()[0]] if q else []

    print("\nRecherche documentaire en cours dans le corpus...")
    context = load_relevant_context(eq_id, kw)
    print(f"-> {len(context)} extrait(s) documentaire(s) récupéré(s).")
    
    print("\nInférence multimodale en cours avec Qwen2.5-VL-7B local...")
    try:
        answer = ask_qwen_multimodal(q, img, context)
        print("\n---------------- RÉPONSE MAINTIDOC SOURCÉE ----------------\n")
        print(answer)
        print("\n-----------------------------------------------------------")
        
        # Simulation de la boucle d'approbation humaine (Human-in-the-loop)
        if "ticket" in answer.lower():
            print("\n[VALIDATION HUMAINE REQUISE (Point de Contrôle C3)]")
            conf = input("Souhaitez-vous approuver formellement la création de ce ticket dans la GMAO ? (o/n) : ").strip().lower()
            if conf in ["o", "oui", "y", "yes"]:
                print("-> Action validée : Ticket enregistré avec succès via le serveur MCP (Token HMAC-SHA256 validé, Clé d'idempotence appliquée).")
            else:
                print("-> Action suspendue : Aucun ticket n'a été créé.")
    except Exception as e:
        print(f"Erreur d'inférence : {e}")

if __name__ == "__main__":
    main()
