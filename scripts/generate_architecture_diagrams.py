"""
Génération des diagrammes d'architecture pour le rapport MaintiDoc L1
Produit des diagrammes professionnels haute résolution pour docs/diagrammes/
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

DOCS_DIR = os.path.join("docs", "diagrammes")
os.makedirs(DOCS_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0

# ------------------------------------------------------------------------------
# 1. Architecture Globale par Blocs Fonctionnels
# ------------------------------------------------------------------------------
def make_global_architecture():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=150)
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 90)
    ax.axis('off')

    def block(x, y, w, h, title, subtitle, bg="#f0f4f8", ec="#004080", title_col="#004080"):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1,rounding_size=2",
                                     facecolor=bg, edgecolor=ec, lw=1.8)
        ax.add_patch(p)
        ax.text(x + w/2, y + h - 3.5, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color=title_col)
        ax.text(x + w/2, y + h/2 - 1.5, subtitle, ha='center', va='center', fontsize=7.5, color="#333333")

    def ctrl_badge(x, y, label):
        b = patches.Circle((x, y), 3.2, facecolor="#c62828", edgecolor="#ffffff", lw=1.5)
        ax.add_patch(b)
        ax.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color="#ffffff")

    def arrow(x1, y1, x2, y2, label=""):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#1a237e", lw=1.6))
        if label:
            ax.text((x1+x2)/2, (y1+y2)/2 + 1.2, label, fontsize=7, color="#0d47a1", fontweight='bold', ha='center')

    # Titre général
    ax.text(70, 86, "ARCHITECTURE CIBLE FONCTIONNELLE DU SYSTÈME MAINTIDOC", 
            ha='center', fontsize=14, fontweight='bold', color="#0d233a")

    # Colonne 1 : Présentation & API
    block(5, 52, 28, 26, "INTERFACE OPÉRATEUR", 
          "Streamlit Web UI\nSaisie questions (texte)\nUpload photographies\nVisualisation réponses & citations\nInterface d'approbation tickets",
          bg="#e8eaf6", ec="#3f51b5")
    
    block(5, 14, 28, 28, "PASSERELLE D'ACCÈS", 
          "FastAPI Backend Gateway\nAuthentification JWT / RBAC\nValidation Pydantic entrées/sorties\nJournalisation d'audit\nRate Limiting & quotas GPU",
          bg="#e8eaf6", ec="#3f51b5")
    
    arrow(19, 52, 19, 42, "Requête HTTP / JSON")
    arrow(15, 42, 15, 52, "Réponse formatée")
    ctrl_badge(33, 28, "C1")
    ax.text(37, 28, "C1: Contrôle d'accès & Auth", fontsize=7.5, color="#c62828", fontweight='bold')

    # Colonne 2 : Orchestration Agentique & Modèle VLM
    block(46, 50, 48, 30, "ORCHESTRATEUR AGENTIQUE (LangGraph)", 
          "Workflow StateGraph avec nœuds conditionnels :\n"
          "1. Analyse de la demande & de l'image (VLM)\n"
          "2. Filtrage groupe & Recherche documentaire (RAG)\n"
          "3. Consultation historique d'interventions (MCP)\n"
          "4. Génération & Vérification des citations (C2)\n"
          "5. Préparation brouillon ticket & Demande validation (C3)\n"
          "6. Appel outil externe de création de ticket (MCP)",
          bg="#fff8e1", ec="#f57f17", title_col="#b78103")

    arrow(33, 24, 46, 60, "Context + Token")
    
    # Modèle Vision-Langage (VLM)
    block(102, 52, 34, 26, "MODÈLE VISION-LANGAGE", 
          "Qwen2.5-VL-7B-Instruct\nInférence vLLM (Quantization AWQ 4-bit)\nCompréhension multimodale conjointe\nAnalyse visuelle panneaux & voyants\nGénération de réponses sourcées",
          bg="#fce4ec", ec="#c2185b", title_col="#880e4f")

    arrow(94, 66, 102, 66, "Prompt + Chunks + Image")
    arrow(102, 60, 94, 60, "Réponse brute + Balises")

    # Colonne 3 : Moteur de Recherche Multimodale
    block(46, 10, 48, 32, "MOTEUR RAG MULTIMODAL & RERANKER", 
          "• Recherche Hybride Vectorielle : Dense + Sparse (BM25)\n"
          "• Embeddings Textuels : BGE-M3 (1024 dims multilingue)\n"
          "• Embeddings Visuels : CLIP / SigLIP (512 dims)\n"
          "• Fusion RRF (Reciprocal Rank Fusion)\n"
          "• Reranking Adapté : BGE-Reranker-Large (Fine-tuning ciblé S5)\n"
          "• Filtrage préalable par groupe d'accès (Metadata Filter)",
          bg="#e0f2f1", ec="#00897b", title_col="#004d40")

    arrow(62, 50, 62, 42, "Requête d'extraction")
    arrow(78, 42, 78, 50, "Top-K Chunks + Images vérifiées")
    ctrl_badge(94, 26, "C2")
    ax.text(98, 26, "C2: Filtrage RBAC Métadonnées", fontsize=7.5, color="#c62828", fontweight='bold')

    # Colonne 4 : Serveur MCP et Stockage
    block(102, 10, 34, 34, "SERVEUR MCP & PERSISTANCE", 
          "Serveur MCP Maintenance :\n"
          "- get_equipment_history(eq_id)\n"
          "- get_open_tickets(eq_id)\n"
          "- create_ticket(token_approbation)\n\n"
          "Bases de Données & Stockage :\n"
          "• Qdrant (Base Vectorielle)\n"
          "• PostgreSQL (Métadonnées & Audit)\n"
          "• MinIO (Fichiers PDF & Images brutes)",
          bg="#ede7f6", ec="#5e35b1", title_col="#311b92")

    arrow(94, 75, 106, 44, "Appel MCP avec Token")
    ctrl_badge(112, 44, "C3")
    ax.text(116, 46, "C3: Validation Humaine Obligatoire", fontsize=7.5, color="#c62828", fontweight='bold')

    # Légende des points de contrôle
    legend_box = patches.FancyBboxPatch((5, 2), 131, 6, boxstyle="square,pad=0.5",
                                        facecolor="#ffffff", edgecolor="#bbbbbb")
    ax.add_patch(legend_box)
    ax.text(70, 5, "POINTS DE CONTRÔLE CRITIQUES :   [C1] Authentification JWT & Contrôle des Droits d'Accès   |   "
                   "[C2] Filtrage Sécurisé du Corpus par Groupe (RBAC)   |   [C3] Interruption LangGraph & Approbation Humaine Ticket",
            ha='center', va='center', fontsize=7.5, fontweight='bold', color="#b71c1c")

    plt.tight_layout()
    plt.savefig(os.path.join(DOCS_DIR, "diagramme_architecture_globale.png"))
    plt.close()
    print("Généré : diagramme_architecture_globale.png")

# ------------------------------------------------------------------------------
# 2. Diagramme Flux d'Ingestion Documentaire
# ------------------------------------------------------------------------------
def make_ingestion_pipeline():
    fig, ax = plt.subplots(figsize=(13, 6), dpi=150)
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 60)
    ax.axis('off')

    def p_box(x, y, w, h, title, sub, bg="#e3f2fd", ec="#1976d2"):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.8", facecolor=bg, edgecolor=ec, lw=1.5)
        ax.add_patch(p)
        ax.text(x + w/2, y + h*0.65, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color="#0d47a1")
        ax.text(x + w/2, y + h*0.28, sub, ha='center', va='center', fontsize=6.8, color="#37474f")

    def ar(x1, y1, x2, y2, txt=""):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#37474f", lw=1.5))
        if txt:
            ax.text((x1+x2)/2, (y1+y2)/2 + 1.2, txt, fontsize=6.5, ha='center', color="#c2185b", fontweight='bold')

    ax.text(65, 56, "PIPELINE D'INGESTION MULTIMODALE & ENRICHISSEMENT DES MÉTADONNÉES",
            ha='center', fontsize=12, fontweight='bold', color="#0d233a")

    p_box(4, 20, 20, 22, "1. DOCUMENTS SOURCES", "PDF manuels, guides,\nschémas PNG, scans\n(Corpus 38 fichiers)", bg="#f5f5f5", ec="#616161")
    
    p_box(29, 32, 22, 18, "2A. EXTRACTION PYMUPDF", "Découpage texte natif,\nextraction tableaux & figures", bg="#e8f5e9", ec="#388e3c")
    p_box(29, 10, 22, 18, "2B. OCR LOCAL CIBLÉ", "Tesseract / PaddleOCR\nsur documents scannés", bg="#fff3e0", ec="#f57c00")

    ar(24, 34, 29, 39, "PDF Texte")
    ar(24, 24, 29, 19, "PDF Scanné")

    p_box(56, 20, 20, 22, "3. SEGMENTATION CHUNKS", "Découpage sémantique\n(500 tokens, 10% overlap)\nPréservation contexte page", bg="#e1f5fe", ec="#0288d1")

    ar(51, 39, 56, 33)
    ar(51, 19, 56, 27)

    p_box(81, 20, 22, 22, "4. MÉTADONNÉES & RBAC", "Ajout doc_id, version, page,\neq_id, groupe_acces\net hachage SHA-256", bg="#ede7f6", ec="#512da8")

    ar(76, 31, 81, 31)

    p_box(108, 32, 20, 18, "5A. EMBEDDINGS DENSES", "BGE-M3 (Texte)\nCLIP/SigLIP (Images)", bg="#fce4ec", ec="#c2185b")
    p_box(108, 10, 20, 18, "5B. INDEXATION VECTOR", "Qdrant Vector DB +\nPostgreSQL + MinIO", bg="#e0f2f1", ec="#00796b")

    ar(103, 33, 108, 39)
    ar(103, 27, 108, 19)

    plt.tight_layout()
    plt.savefig(os.path.join(DOCS_DIR, "diagramme_flux_ingestion.png"))
    plt.close()
    print("Généré : diagramme_flux_ingestion.png")

# ------------------------------------------------------------------------------
# 3. Diagramme Flux d'une Requête et Validation Humaine
# ------------------------------------------------------------------------------
def make_query_state_machine():
    fig, ax = plt.subplots(figsize=(13, 7), dpi=150)
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 70)
    ax.axis('off')

    def state(x, y, w, h, text, bg="#e8eaf6", ec="#3f51b5"):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.8", facecolor=bg, edgecolor=ec, lw=1.5)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.5, color="#1a237e", fontweight='bold')

    def link(x1, y1, x2, y2, lbl="", c="#283593"):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=c, lw=1.5))
        if lbl:
            ax.text((x1+x2)/2 + 2, (y1+y2)/2, lbl, fontsize=6.5, color="#c2185b", fontweight='bold')

    ax.text(65, 66, "MACHINE À ÉTATS D'UNE REQUÊTE ET BOUCLE DE VALIDATION HUMAINE (LANGGRAPH)",
            ha='center', fontsize=12, fontweight='bold', color="#0d233a")

    state(5, 48, 22, 12, "1. RECEPTION_REQUETE\n(Question + Image)")
    state(33, 48, 22, 12, "2. VERIFICATION_ACCES\n(Vérif JWT & Rôles)")
    state(61, 48, 24, 12, "3. RECHERCHE_MULTIMODALE\n(Dense + Sparse + RRF)")
    state(91, 48, 24, 12, "4. RERANKING_CIBLE\n(Top-K Chunks filtrés)")

    link(27, 54, 33, 54)
    link(55, 54, 61, 54)
    link(85, 54, 91, 54)

    state(91, 26, 24, 12, "5. SYNTHESE_VLM\n(Qwen2.5-VL-7B)", bg="#fce4ec", ec="#c2185b")
    link(103, 48, 103, 38)

    state(61, 26, 24, 12, "6. CONTROLE_CITATIONS\n(Vérif ancrage & preuves)")
    link(91, 32, 85, 32)

    # Branche de décision : Ticket nécessaire ?
    state(33, 26, 22, 12, "7. DECISION_ACTION\n(Ticket requis ?)")
    link(61, 32, 55, 32)

    # Réponse simple sans ticket
    state(5, 26, 22, 12, "8A. REPONSE_SOURCÉE\n(Retour direct client)", bg="#e8f5e9", ec="#2e7d32")
    link(33, 32, 27, 32, "Non")

    # Branche ticket avec validation humaine
    state(33, 6, 22, 12, "8B. PREPARATION_TICKET\n(Brouillon Pydantic)", bg="#fff8e1", ec="#f57f17")
    link(44, 26, 44, 18, "Oui")

    state(61, 6, 24, 12, "9. ATTENTE_HUMAIN\n[INTERRUPT]\n(Approbation token)", bg="#ffebee", ec="#c62828")
    link(55, 12, 61, 12)

    state(91, 6, 24, 12, "10. CREATION_TICKET_MCP\n(Appel idempotent)", bg="#ede7f6", ec="#512da8")
    link(85, 12, 91, 12, "Validé")

    state(118, 6, 11, 12, "FIN\n(Succès)", bg="#e8f5e9", ec="#2e7d32")
    link(115, 12, 118, 12)

    plt.tight_layout()
    plt.savefig(os.path.join(DOCS_DIR, "diagramme_flux_requete_agentique.png"))
    plt.close()
    print("Généré : diagramme_flux_requete_agentique.png")

# ------------------------------------------------------------------------------
# 4. Modèle de Données et Matrice d'Accès RBAC
# ------------------------------------------------------------------------------
def make_rbac_matrix_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), dpi=150)

    # Volet 1 : Schéma Métadonnées Chunk
    ax1.set_xlim(0, 60)
    ax1.set_ylim(0, 60)
    ax1.axis('off')
    ax1.set_title("Schéma JSON des Métadonnées d'un Chunk Indexé", fontsize=10.5, fontweight='bold', color="#0d233a")

    meta_text = (
        "{\n"
        '  "chunk_id": "chk_canon_r50_004_p02_c01",\n'
        '  "document_id": "proc_nettoyage_capteur_officiel",\n'
        '  "version": "v1.0 (2026-01)",\n'
        '  "page": 2,\n'
        '  "element_type": "procedure_paragraphe",\n'
        '  "famille_equipement": "Appareil Photo Hybride",\n'
        '  "equipement_id": "Canon_EOS_R50",\n'
        '  "groupes_acces": ["techniciens_audiovisuel", "responsables"],\n'
        '  "source_sha256": "e3b0c44298fc1c149afbf4c8996fb924...",\n'
        '  "has_visual_element": true,\n'
        '  "linked_image_id": "schema_chambre_capteur_nettoyage",\n'
        '  "usage_test": "contradictoire"\n'
        "}"
    )
    p = patches.FancyBboxPatch((2, 5), 56, 50, boxstyle="round,pad=1", facecolor="#263238", edgecolor="#37474f", lw=1.5)
    ax1.add_patch(p)
    ax1.text(5, 50, meta_text, family='monospace', fontsize=7.2, color="#80cbc4", va='top')

    # Volet 2 : Matrice des Droits d'Accès (RBAC)
    ax2.set_xlim(0, 70)
    ax2.set_ylim(0, 60)
    ax2.axis('off')
    ax2.set_title("Modèle d'Accès aux Documents et Actions MCP", fontsize=10.5, fontweight='bold', color="#0d233a")

    table_data = [
        ["Groupe d'utilisateurs", "Famille 1 (Canon)", "Famille 2 (Epson)", "Tickets MCP"],
        ["techniciens_audiovisuel", "ACCÈS TOTAL", "ACCÈS REFUSÉ", "Création soumise visa"],
        ["techniciens_impression", "ACCÈS REFUSÉ", "ACCÈS TOTAL", "Création soumise visa"],
        ["responsables_maintenance", "ACCÈS TOTAL", "ACCÈS TOTAL", "Validation & Visa direct"],
        ["operateurs_invites", "Manuels Base", "Manuels Base", "LECTURE SEULE"]
    ]

    t = ax2.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.32, 0.22, 0.22, 0.24])
    t.auto_set_font_size(False)
    t.set_fontsize(7.5)
    t.scale(1, 1.8)

    # Couleurs du tableau
    for col in range(4):
        t[(0, col)].set_facecolor("#0d47a1")
        t[(0, col)].get_text().set_color("white")
        t[(0, col)].get_text().set_weight("bold")

    for row in range(1, 5):
        t[(row, 0)].set_facecolor("#f5f5f5")
        t[(row, 0)].get_text().set_weight("bold")

    t[(1, 1)].set_facecolor("#e8f5e9")
    t[(1, 2)].set_facecolor("#ffebee")
    t[(2, 1)].set_facecolor("#ffebee")
    t[(2, 2)].set_facecolor("#e8f5e9")
    t[(3, 1)].set_facecolor("#e8f5e9")
    t[(3, 2)].set_facecolor("#e8f5e9")

    plt.tight_layout()
    plt.savefig(os.path.join(DOCS_DIR, "diagramme_modele_donnees_acces.png"))
    plt.close()
    print("Généré : diagramme_modele_donnees_acces.png")

if __name__ == "__main__":
    make_global_architecture()
    make_ingestion_pipeline()
    make_query_state_machine()
    make_rbac_matrix_diagram()
    print("Tous les diagrammes d'architecture ont été générés dans docs/diagrammes/.")
