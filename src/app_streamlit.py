"""
Application Web Interactive MaintiDoc (Streamlit)
Connectée au modèle local Qwen2.5-VL-7B et au corpus documentaire.
"""
import streamlit as st
import os
import io
import json
import base64
import urllib.request
import urllib.error
import csv
from PIL import Image

st.set_page_config(
    page_title="MaintiDoc — Assistant Multimodal",
    page_icon="🔧",
    layout="wide"
)

BASE_URL = "http://127.0.0.1:1234/v1"
MODEL_ID = "qwen/qwen2.5-vl-7b"
# Résolution automatique du chemin du corpus
if os.path.exists(os.path.join("L1_MaintiDoc_MALDANI_BOUJRADA", "L1_MaintiDoc_MALDANI_BOUJRADA_Corpus")):
    CORPUS_DIR = os.path.join("L1_MaintiDoc_MALDANI_BOUJRADA", "L1_MaintiDoc_MALDANI_BOUJRADA_Corpus")
elif os.path.exists(os.path.join("L1_MaintiDoc_MALDANI", "L1_MaintiDoc_MALDANI_Corpus")):
    CORPUS_DIR = os.path.join("L1_MaintiDoc_MALDANI", "L1_MaintiDoc_MALDANI_Corpus")
elif os.path.exists("corpus"):
    CORPUS_DIR = "corpus"
else:
    CORPUS_DIR = os.path.join("..", "corpus")

INVENTAIRE_PATH = os.path.join(CORPUS_DIR, "inventaire.csv")
IMAGES_DIR = os.path.join(CORPUS_DIR, "documents", "images")

# --- En-tête ---
st.title("🔧 MaintiDoc : Assistant Documentaire Multimodal & Agentique")
st.markdown("**Module IA Générative Multimodale (EMSI-2026)** | Équipe : **MALDANI & BOUJRADA** (Mostafa MALDANI, Younes BOUJRADA) | Modèle local : **Qwen2.5-VL-7B-Instruct**")

# --- Vérification du statut du modèle local ---
@st.cache_data(ttl=10)
def check_model_status():
    try:
        req = urllib.request.Request(f"{BASE_URL}/models")
        with urllib.request.urlopen(req, timeout=2) as resp:
            data = json.loads(resp.read().decode())
            models = [m.get("id") for m in data.get("data", [])]
            return MODEL_ID in models, models
    except:
        return False, []

is_online, active_models = check_model_status()

# Barre latérale : Paramètres & Statut
with st.sidebar:
    st.header("⚙️ Configuration Système")
    if is_online:
        st.success(f"🟢 Modèle Qwen2.5-VL-7B Actif sur {BASE_URL}")
    else:
        st.error("🔴 Modèle Hors Ligne")
        st.info("Pour démarrer le serveur local :\n```bash\nlms server start\nlms load qwen/qwen2.5-vl-7b -c 4096 --gpu off -y\n```")

    st.subheader("📋 Sélection de l'Équipement")
    famille = st.selectbox(
        "Famille d'équipements :",
        ["Canon EOS R50 (Hybride)", "Epson SureColor SC-P700 (Traceur)"]
    )
    equipment_id = "CANON-R50-01" if "Canon" in famille else "EPSON-P700-01"

    st.subheader("👥 Groupe d'accès (RBAC)")
    groupe = st.selectbox(
        "Profil de l'opérateur connecté :",
        ["techniciens_audiovisuel", "techniciens_impression", "responsables_maintenance"]
    )

# --- Zone Principale ---
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("📷 Photographie / Schéma d'Atelier")
    
    # Choix de l'image
    image_mode = st.radio("Source de l'élément visuel :", ["Sélectionner dans le corpus", "Téléverser une image"], horizontal=True)
    selected_image_path = None

    if image_mode == "Sélectionner dans le corpus":
        available_images = [f for f in os.listdir(IMAGES_DIR) if f.endswith(".png")] if os.path.exists(IMAGES_DIR) else []
        # Filtrer selon famille
        if "Canon" in famille:
            available_images = [img for img in available_images if "canon" in img]
        else:
            available_images = [img for img in available_images if "epson" in img]

        chosen_img = st.selectbox("Choisir un schéma technique :", available_images)
        if chosen_img:
            selected_image_path = os.path.join(IMAGES_DIR, chosen_img)
            st.image(selected_image_path, use_container_width=True, caption=chosen_img)
    else:
        uploaded_file = st.file_uploader("Charger une photo (PNG/JPEG) :", type=["png", "jpg", "jpeg"])
        if uploaded_file:
            tmp_path = os.path.join("tmp_upload.png")
            with open(tmp_path, "wb") as f:
                f.write(uploaded_file.read())
            selected_image_path = tmp_path
            st.image(selected_image_path, use_container_width=True, caption="Image opérateur téléversée")

with col_right:
    st.subheader("💬 Question Technique de Maintenance")
    
    # Exemples prédéfinis selon équipement
    if "Canon" in famille:
        examples = [
            "Que représente cette image technique et quelles sont les commandes du panneau supérieur ?",
            "Quelle est la procédure officielle pour nettoyer le capteur ? A-t-on le droit d'utiliser un solvant liquide ?",
            "Mon boîtier affiche le code Err 01. Quelle est la cause et comment y remédier ?",
            "Comment mettre à jour le firmware sans risquer d'endommager l'appareil ?"
        ]
    else:
        examples = [
            "L'écran affiche le code 1485. Que signifie-t-il et comment remplacer le boîtier de maintenance ? Prépare un ticket.",
            "Analyse cette mire de buses (Nozzle Check). Quelles sont les couleurs bouchées et quelle est la démarche officielle ?",
            "Peut-on enchaîner 4 Power Cleanings d'affilée sans attendre ?",
            "Comment dégager un bourrage papier sans risquer d'abîmer la tête d'impression ?"
        ]
        
    preset_q = st.selectbox("Questions types d'atelier :", ["Saisie libre..."] + examples)
    if preset_q == "Saisie libre...":
        user_query = st.text_area("Votre question :", value="Que signifie ce voyant et comment procéder ?", height=80)
    else:
        user_query = st.text_area("Votre question :", value=preset_q, height=80)

    btn_submit = st.button("🚀 Interroger MaintiDoc (Qwen2.5-VL-7B)", type="primary", use_container_width=True)

# --- Traitement de l'inférence ---
if btn_submit:
    if not is_online:
        st.error("Impossible de lancer l'inférence : le modèle local Qwen2.5-VL n'est pas actif.")
    else:
        with st.spinner("Recherche RAG dans le corpus et inférence multimodale en cours avec Qwen2.5-VL-7B..."):
            try:
                # 1. Extraction du contexte documentaire
                context_chunks = []
                if os.path.exists(INVENTAIRE_PATH):
                    with open(INVENTAIRE_PATH, "r", encoding="utf-8") as f:
                        for row in csv.DictReader(f):
                            if row["equipement_id"] == equipment_id:
                                doc_path = os.path.join(CORPUS_DIR, row["fichier"])
                                if os.path.exists(doc_path) and doc_path.endswith(".md"):
                                    with open(doc_path, "r", encoding="utf-8") as df:
                                        context_chunks.append({
                                            "doc_id": row["document_id"],
                                            "titre": row["titre"],
                                            "page": row["nb_pages"],
                                            "content": df.read()[:350]
                                        })

                context_prompt = "\n\n--- SOURCES DOCUMENTAIRES AUTORISÉES ---\n"
                for doc in context_chunks[:2]:
                    context_prompt += f"[Document: {doc['doc_id']} | Titre: {doc['titre']} | Page: {doc['page']}]\n{doc['content']}\n\n"
                context_prompt += "--------------------------------------\nCONSIGNE : Réponds avec rigueur en citant obligatoirement le document_id et la page.\n"

                # 2. Construction de la requête multimodale avec redimensionnement d'image
                messages_content = [{"type": "text", "text": f"{user_query}\n{context_prompt}"}]
                
                if selected_image_path and os.path.exists(selected_image_path):
                    with Image.open(selected_image_path) as img:
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                        # Redimensionnement optimisé pour l'inférence vision locale (~256 tokens)
                        img.thumbnail((448, 448), Image.Resampling.LANCZOS)
                        buf = io.BytesIO()
                        img.save(buf, format="JPEG", quality=80)
                        b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
                        messages_content.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{b64}"}
                        })

                payload = {
                    "model": MODEL_ID,
                    "messages": [
                        {"role": "system", "content": "Tu es MaintiDoc, l'assistant expert de maintenance industrielle et atelier. Tu réponds de manière concise et précise en citant rigoureusement les sources officielles (document_id, page)."},
                        {"role": "user", "content": messages_content}
                    ],
                    "temperature": 0.2,
                    "max_tokens": 400
                }

                req = urllib.request.Request(
                    f"{BASE_URL}/chat/completions",
                    data=json.dumps(payload).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )

                with urllib.request.urlopen(req, timeout=120) as resp:
                    res = json.loads(resp.read().decode())
                    answer = res["choices"][0]["message"]["content"]

                st.success("✅ Réponse multimodale générée avec succès !")
                st.markdown("### 📝 Réponse Sourcée de MaintiDoc :")
                st.markdown(answer)

                # Simulation Point de Contrôle C3 : Validation Ticket
                if "ticket" in answer.lower() or "1485" in user_query:
                    st.warning("⚠️ **Point de Contrôle C3 (Human-in-the-loop) :** Une action sensible (création de ticket GMAO) a été proposée.")
                    col_t1, col_t2 = st.columns([3, 1])
                    with col_t1:
                        st.info("Brouillon : **Remplacement Boîtier C12C935711 — Équipement: EPSON-P700-01 — Sévérité: Critique (Bloquant)**")
                    with col_t2:
                        if st.button("✅ Approuver le Ticket (MCP)", type="primary"):
                            st.success("Ticket créé avec succès via l'outil MCP `create_ticket()` ! Jeton validé.")

            except urllib.error.HTTPError as e:
                err_msg = e.read().decode("utf-8", errors="ignore")
                st.error(f"Erreur d'inférence HTTP {e.code} : {err_msg}")
            except Exception as e:
                st.error(f"Erreur d'inférence : {e}")

# Footer
st.divider()
st.caption("Projet MaintiDoc — Livrable 1 (Cadrage, Corpus & Architecture Cible) | EMSI-2026")
