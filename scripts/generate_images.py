"""
Script de génération des éléments visuels techniques pour MaintiDoc
Génère 12 schémas et diagrammes techniques haute résolution (PNG).
"""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = os.path.join("L1_MaintiDoc_TeamName_Corpus", "documents", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configuration générale de matplotlib
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.0

# -------------------------------------------------------------
# 1. Canon R50 - Panneau Supérieur
# -------------------------------------------------------------
def make_canon_top_panel():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Corps appareil vue du dessus
    body = patches.FancyBboxPatch((15, 10), 70, 40, boxstyle="round,pad=3,rounding_size=5", 
                                  facecolor="#2b2b2b", edgecolor="#111111", linewidth=2)
    ax.add_patch(body)
    
    # Viseur saillie
    evf = patches.Rectangle((40, 42), 20, 10, facecolor="#1a1a1a", edgecolor="#444444", linewidth=1.5)
    ax.add_patch(evf)
    
    # Griffe flash multifonction
    shoe = patches.Rectangle((43, 38), 14, 12, facecolor="#c0c0c0", edgecolor="#222222", linewidth=1.5)
    ax.add_patch(shoe)
    
    # Molette de sélection de mode (Mode Dial)
    mode_dial = patches.Circle((28, 35), 8, facecolor="#444444", edgecolor="#888888", linewidth=1.5)
    ax.add_patch(mode_dial)
    
    # Déclencheur & bague alimentation
    shutter = patches.Circle((75, 42), 5, facecolor="#e0e0e0", edgecolor="#333333", linewidth=1.5)
    ax.add_patch(shutter)
    power_switch = patches.Arc((75, 42), 16, 16, angle=0, theta1=45, theta2=225, color="#ff9900", linewidth=3)
    ax.add_patch(power_switch)
    
    # Molette principale (Main Dial)
    main_dial = patches.Rectangle((70, 48), 10, 4, facecolor="#555555", edgecolor="#222222")
    ax.add_patch(main_dial)
    
    # Bouton Enregistrement Vidéo (Point rouge)
    rec_btn = patches.Circle((66, 36), 3, facecolor="#cc0000", edgecolor="#ffffff", linewidth=1)
    ax.add_patch(rec_btn)
    
    # Bouton ISO
    iso_btn = patches.Circle((76, 30), 3, facecolor="#555555", edgecolor="#ffffff", linewidth=1)
    ax.add_patch(iso_btn)
    
    # Annotations
    ax.annotate("Griffe multifonction\n(Flash / Accessoires)", xy=(50, 48), xytext=(50, 56),
                ha='center', fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle="->", color="#0066cc", lw=1.5))
    
    ax.annotate("Molette de mode\n(P, Tv, Av, M, Auto, SCN)", xy=(28, 43), xytext=(12, 54),
                ha='center', fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle="->", color="#0066cc", lw=1.5))
    
    ax.annotate("Déclencheur +\nCommutateur ON/OFF", xy=(78, 44), xytext=(88, 52),
                ha='center', fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle="->", color="#0066cc", lw=1.5))
    
    ax.annotate("Molette principale\n(Réglages Vitesse/Ouverture)", xy=(75, 50), xytext=(88, 40),
                ha='left', fontsize=8,
                arrowprops=dict(arrowstyle="->", color="#0066cc", lw=1.2))

    ax.annotate("Bouton Enreg. Vidéo\n(Touche REC dédiée)", xy=(66, 36), xytext=(55, 20),
                ha='center', fontsize=8,
                arrowprops=dict(arrowstyle="->", color="#0066cc", lw=1.2))
                
    ax.annotate("Touche de réglage ISO", xy=(76, 30), xytext=(85, 22),
                ha='left', fontsize=8,
                arrowprops=dict(arrowstyle="->", color="#0066cc", lw=1.2))

    plt.title("Canon EOS R50 - Schéma Technique du Panneau Supérieur (Commandes)", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_CANON_01_Panneau_Superieur_Commandes.png"))
    plt.close()

# -------------------------------------------------------------
# 2. Canon R50 - Panneau Arrière
# -------------------------------------------------------------
def make_canon_back_panel():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Boîtier arrière
    body = patches.FancyBboxPatch((10, 8), 80, 46, boxstyle="round,pad=2,rounding_size=4",
                                  facecolor="#262626", edgecolor="#111111", linewidth=2)
    ax.add_patch(body)
    
    # Écran orientable LCD 3.0"
    lcd = patches.Rectangle((15, 12), 48, 36, facecolor="#102030", edgecolor="#666666", linewidth=2)
    ax.add_patch(lcd)
    ax.text(39, 30, "Écran LCD Tactile Orientable\n3.0 pouces (1,62 Mpx)", 
            color="#88bbff", fontsize=9, ha='center', va='center')
    
    # Viseur OLED (EVF)
    evf = patches.Rectangle((42, 48), 16, 9, facecolor="#0a0a0a", edgecolor="#777777", linewidth=1.5)
    ax.add_patch(evf)
    capteur_oeil = patches.Circle((44, 53), 1.5, facecolor="#00ffff")
    ax.add_patch(capteur_oeil)
    
    # Boutons à droite
    # Touche MENU
    menu_btn = patches.Circle((72, 44), 3, facecolor="#3d3d3d", edgecolor="#ffffff", linewidth=1)
    ax.add_patch(menu_btn)
    ax.text(72, 44, "MENU", color="white", fontsize=6, ha='center', va='center', fontweight='bold')
    
    # Touche INFO
    info_btn = patches.Circle((82, 44), 3, facecolor="#3d3d3d", edgecolor="#ffffff", linewidth=1)
    ax.add_patch(info_btn)
    ax.text(82, 44, "INFO", color="white", fontsize=6, ha='center', va='center', fontweight='bold')
    
    # Pavé directionnel en croix (Cross Keys) & Q/SET au centre
    q_set = patches.Circle((77, 28), 4.5, facecolor="#0055aa", edgecolor="#ffffff", linewidth=1.5)
    ax.add_patch(q_set)
    ax.text(77, 28, "Q/SET", color="white", fontsize=6, ha='center', va='center', fontweight='bold')
    
    # 4 touches directionnelles
    up_key = patches.Rectangle((75, 33), 4, 3, facecolor="#444444", edgecolor="#888888")
    down_key = patches.Rectangle((75, 20), 4, 3, facecolor="#444444", edgecolor="#888888")
    left_key = patches.Rectangle((70, 26), 3, 4, facecolor="#444444", edgecolor="#888888")
    right_key = patches.Rectangle((81, 26), 3, 4, facecolor="#444444", edgecolor="#888888")
    for k in [up_key, down_key, left_key, right_key]:
        ax.add_patch(k)
        
    # Touche Lecture (Play)
    play_btn = patches.Circle((72, 14), 3, facecolor="#3d3d3d", edgecolor="#ffffff", linewidth=1)
    ax.add_patch(play_btn)
    ax.text(72, 14, "▶", color="white", fontsize=7, ha='center', va='center')
    
    # Touche Corbeille
    trash_btn = patches.Circle((82, 14), 3, facecolor="#3d3d3d", edgecolor="#ffffff", linewidth=1)
    ax.add_patch(trash_btn)
    ax.text(82, 14, "DEL", color="white", fontsize=5.5, ha='center', va='center', fontweight='bold')

    # Annotations
    ax.annotate("Viseur Électronique EVF (0.39\")\navec capteur oculaire", xy=(50, 52), xytext=(50, 61),
                ha='center', fontsize=8, fontweight='bold',
                arrowprops=dict(arrowstyle="->", color="#ff9900", lw=1.2))
                
    ax.annotate("Touche Q/SET\nMenu rapide & validation", xy=(77, 28), xytext=(92, 28),
                ha='left', fontsize=8,
                arrowprops=dict(arrowstyle="->", color="#ff9900", lw=1.2))

    ax.annotate("Touches de navigation en croix :\nHaut : Correction exposition\nBas : Effacement\nGauche : Autofocus MF/AF\nDroite : Mode d'entraînement", 
                xy=(79, 21), xytext=(65, 3), ha='center', fontsize=7,
                bbox=dict(boxstyle="square,pad=0.3", fc="#f0f0f0", ec="#cccccc"))

    plt.title("Canon EOS R50 - Panneau Arrière et Commandes Opérateur", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_CANON_02_Panneau_Arriere_Ecran_Commandes.png"))
    plt.close()

# -------------------------------------------------------------
# 3. Canon R50 - Connectique et Batterie
# -------------------------------------------------------------
def make_canon_connectors():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5), dpi=150)
    
    # Volet gauche : Ports latéraux
    ax1.set_xlim(0, 50)
    ax1.set_ylim(0, 80)
    ax1.axis('off')
    ax1.set_title("Flanc Gauche (Connectique)", fontsize=11, fontweight='bold')
    
    body1 = patches.Rectangle((10, 10), 30, 60, facecolor="#303030", edgecolor="#111111", linewidth=2)
    ax1.add_patch(body1)
    
    # Port USB-C
    usb = patches.FancyBboxPatch((20, 50), 10, 5, boxstyle="round,pad=0.5", facecolor="#d0d0d0", edgecolor="#000000")
    ax1.add_patch(usb)
    ax1.annotate("Port USB-C (Hi-Speed 2.0)\nAlimentation / Charge PD\nWebcam UVC / UAC", xy=(25, 52), xytext=(2, 63),
                 ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#0066cc"))
    
    # Port Micro-HDMI
    hdmi = patches.Rectangle((21, 35), 8, 4, facecolor="#d0d0d0", edgecolor="#000000")
    ax1.add_patch(hdmi)
    ax1.annotate("Sortie Micro-HDMI (Type D)\nFlux vidéo externe non compressé", xy=(25, 37), xytext=(2, 40),
                 ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#0066cc"))
                 
    # Prise Micro 3.5mm
    mic = patches.Circle((25, 22), 3, facecolor="#cc2222", edgecolor="#ffffff", linewidth=1.5)
    ax1.add_patch(mic)
    ax1.annotate("Entrée Micro 3.5mm stéréo\n(Casque non supporté directement)", xy=(25, 22), xytext=(2, 20),
                 ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#0066cc"))

    # Volet droit : Compartiment inférieur
    ax2.set_xlim(0, 60)
    ax2.set_ylim(0, 80)
    ax2.axis('off')
    ax2.set_title("Base Inférieure (Batterie & SD)", fontsize=11, fontweight='bold')
    
    bottom_body = patches.Rectangle((5, 15), 50, 50, facecolor="#262626", edgecolor="#111111", linewidth=2)
    ax2.add_patch(bottom_body)
    
    # Pas de vis trépied
    tripod = patches.Circle((18, 40), 5, facecolor="#888888", edgecolor="#222222", linewidth=2)
    ax2.add_patch(tripod)
    ax2.annotate("Pas de vis 1/4\"\npour trépied standard", xy=(18, 40), xytext=(18, 68),
                 ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#333333"))

    # Trappe batterie
    door = patches.Rectangle((30, 22), 20, 36, facecolor="#3a3a3a", edgecolor="#ff9900", linewidth=1.5, linestyle="--")
    ax2.add_patch(door)
    
    # Batterie LP-E17
    bat = patches.Rectangle((32, 33), 16, 22, facecolor="#4488cc", edgecolor="#003366")
    ax2.add_patch(bat)
    ax2.text(40, 44, "LP-E17\n(7.2V\n1040mAh)", color="white", fontsize=6, ha='center', va='center')
    
    # Logement SD Card
    sd = patches.Rectangle((34, 25), 12, 6, facecolor="#ffcc00", edgecolor="#665500")
    ax2.add_patch(sd)
    ax2.text(40, 28, "Carte SD (UHS-I)", color="black", fontsize=5.5, ha='center', va='center', fontweight='bold')

    ax2.annotate("Verrou de sécurité\nde batterie", xy=(48, 52), xytext=(55, 60),
                 ha='center', fontsize=7, arrowprops=dict(arrowstyle="->", color="#ff9900"))

    plt.suptitle("Canon EOS R50 - Schéma des Connecteurs et Alimentation", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_CANON_03_Schema_Connectique_Batterie.png"))
    plt.close()

# -------------------------------------------------------------
# 4. Canon R50 - Chambre Capteur et Nettoyage
# -------------------------------------------------------------
def make_canon_sensor_cleaning():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis('off')
    
    # Bague monture RF
    mount_outer = patches.Circle((40, 35), 25, facecolor="#777777", edgecolor="#222222", linewidth=3)
    mount_inner = patches.Circle((40, 35), 21, facecolor="#1a1a1a", edgecolor="#555555", linewidth=2)
    ax.add_patch(mount_outer)
    ax.add_patch(mount_inner)
    
    # Contacts électroniques or
    for angle in np.linspace(220, 320, 12):
        rad = np.radians(angle)
        cx = 40 + 19 * np.cos(rad)
        cy = 35 + 19 * np.sin(rad)
        contact = patches.Circle((cx, cy), 0.9, facecolor="#ffd700", edgecolor="#997700")
        ax.add_patch(contact)
        
    # Capteur CMOS APS-C
    sensor = patches.Rectangle((30, 26), 20, 18, facecolor="#006644", edgecolor="#00ff88", linewidth=1.5)
    ax.add_patch(sensor)
    ax.text(40, 35, "Capteur CMOS\n24.2 Mpx\n(Filtre passe-bas)", color="white", fontsize=7.5, ha='center', va='center')
    
    # Poire soufflante (Blower)
    ax.annotate("", xy=(42, 38), xytext=(80, 52),
                arrowprops=dict(arrowstyle="->", color="#0088cc", lw=3))
    
    blower_bulb = patches.Ellipse((85, 55), 14, 10, angle=25, facecolor="#3377bb", edgecolor="#113366", lw=2)
    ax.add_patch(blower_bulb)
    blower_tip = patches.Polygon([(80, 52), (72, 47), (74, 45)], facecolor="#dd3333")
    ax.add_patch(blower_tip)
    
    # Lignes d'air soufflé
    for dy in [-2, 0, 2]:
        ax.plot([70, 48], [46 + dy, 37 + dy], color="#00bbff", linestyle="--", linewidth=1.5)
        
    # Règles de sécurité
    warning_box = patches.FancyBboxPatch((5, 2), 90, 12, boxstyle="round,pad=1",
                                         facecolor="#fff3cd", edgecolor="#ffeeba", linewidth=1.5)
    ax.add_patch(warning_box)
    ax.text(50, 8, "PRÉCAUTIONS CRITIQUES : Distance embout-capteur >= 15 mm. Ne JAMAIS toucher la surface.\n"
                   "INTERDICTION ABSOLUE de solvants liquides ou bombes à air comprimé sous pression.",
            color="#856404", fontsize=8, fontweight='bold', ha='center', va='center')

    ax.annotate("Contacts or de communication RF\n(Nettoyer délicatement si Err 01)", xy=(40, 16), xytext=(15, 8),
                ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#ffd700", lw=1.2))

    ax.annotate("Poire soufflante manuelle\n(Sans contact physique)", xy=(76, 50), xytext=(80, 65),
                ha='center', fontsize=8, fontweight='bold', arrowprops=dict(arrowstyle="->", color="#3377bb"))

    plt.title("Canon EOS R50 - Procédure de Nettoyage Manuel du Capteur CMOS", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_CANON_04_Schema_Chambre_Capteur_Nettoyage.png"))
    plt.close()

# -------------------------------------------------------------
# 5. Canon R50 - Organigramme Erreurs Err 01 & Err 02
# -------------------------------------------------------------
def make_canon_error_flowchart():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    def box(x, y, w, h, text, bg="#e3f2fd", ec="#1e88e5", bold=False):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1", facecolor=bg, edgecolor=ec, lw=1.5)
        ax.add_patch(p)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8, fontweight=weight)
        
    def link(x1, y1, x2, y2, label=""):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#37474f", lw=1.5))
        if label:
            ax.text((x1+x2)/2 + 2, (y1+y2)/2, label, fontsize=7.5, color="#d32f2f", fontweight='bold')

    # Départ
    box(35, 88, 30, 8, "Message d'erreur affiché\nsur l'écran LCD", bg="#ffebee", ec="#c62828", bold=True)
    
    # Séparation Err 01 vs Err 02
    box(10, 72, 35, 8, "Code : Err 01\n(Communication Objectif)", bg="#fff8e1", ec="#f57f17", bold=True)
    box(55, 72, 35, 8, "Code : Err 02\n(Accès Carte Mémoire)", bg="#fff8e1", ec="#f57f17", bold=True)
    
    link(45, 88, 27, 80)
    link(55, 88, 72, 80)
    
    # Branche Err 01
    box(10, 54, 35, 9, "Étape 1 : Retirer l'objectif et\nnettoyer les contacts dorés au chiffon sec")
    link(27, 72, 27, 63)
    
    box(10, 36, 35, 9, "Étape 2 : Réinstaller fermement\nl'objectif jusqu'au déclic du verrou")
    link(27, 54, 27, 45)
    
    box(10, 18, 35, 9, "Erreur résolue ?\nNon -> Tester avec autre optique RF\nSi persiste -> Atelier SAV Canon", bg="#e8f5e9", ec="#2e7d32")
    link(27, 36, 27, 27)

    # Branche Err 02
    box(55, 54, 35, 9, "Étape 1 : Éteindre appareil,\nretirer et réinsérer la carte SD")
    link(72, 72, 72, 63)
    
    box(55, 36, 35, 9, "Étape 2 : Sauvegarder données\net formater dans l'appareil (Formatage bas niveau)")
    link(72, 54, 72, 45)
    
    box(55, 18, 35, 9, "Erreur résolue ?\nNon -> Remplacer carte SD (UHS-I)\nSi persiste -> Contrôleur slot SAV", bg="#e8f5e9", ec="#2e7d32")
    link(72, 36, 72, 27)

    plt.title("Canon EOS R50 - Arbre Diagnostic des Pannes Fréquentes (Err 01 & Err 02)", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_CANON_05_Organigramme_Diagnostic_Erreur_Err01_Err02.png"))
    plt.close()

# -------------------------------------------------------------
# 6. Canon R50 - Indicateurs LED & Écran
# -------------------------------------------------------------
def make_canon_led_indicators():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    indicators = [
        ("Témoin d'accès carte (LED rouge clignotante)", "Écriture / Lecture en cours sur la carte SD. NE PAS retirer la carte ni la batterie.", "#d32f2f"),
        ("Témoin de charge USB-PD (LED verte fixe)", "Batterie LP-E17 en cours de chargement via adaptateur USB Power Delivery compatible.", "#388e3c"),
        ("Icône Température interne (Thermomètre blanc)", "Montée en température interne (vidéo 4K). Réduire la charge ou interrompre temporairement.", "#f57c00"),
        ("Icône Température critique (Thermomètre rouge)", "Arrêt thermique d'urgence imminent. Sauvegarde automatique et coupure d'alimentation.", "#c62828"),
        ("Témoin retardateur / Lampe AF (LED orange frontale)", "Compte à rebours du retardateur actif ou faisceau d'assistance autofocus en basse lumière.", "#ffa000")
    ]
    
    y = 48
    for title, desc, col in indicators:
        p = patches.Circle((8, y), 3.5, facecolor=col, edgecolor="#333333", lw=1.5)
        ax.add_patch(p)
        ax.text(15, y + 1, title, fontsize=9, fontweight='bold', color="#111111")
        ax.text(15, y - 3, desc, fontsize=7.5, color="#444444")
        y -= 10
        
    plt.title("Canon EOS R50 - Guide de Décryptage des Indicateurs Lumineux & Alertes", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_CANON_06_Schema_Eclairage_Indicateurs_LED.png"))
    plt.close()

# -------------------------------------------------------------
# 7. Epson P700 - Vue Face & Panneau Tactile
# -------------------------------------------------------------
def make_epson_front_view():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Chassis de l'imprimante
    chassis = patches.FancyBboxPatch((10, 10), 80, 42, boxstyle="round,pad=2,rounding_size=3",
                                     facecolor="#1e1e1e", edgecolor="#000000", lw=2)
    ax.add_patch(chassis)
    
    # Capot transparent supérieur
    cover = patches.Rectangle((18, 30), 64, 18, facecolor="#2b2b2b", edgecolor="#444444", lw=1.5)
    ax.add_patch(cover)
    ax.text(50, 39, "Capot Supérieur & Fenêtre de Visualisation Tête", color="#aaaaaa", fontsize=8, ha='center')
    
    # Écran tactile inclinable 4.3"
    touch_screen = patches.Rectangle((56, 14), 28, 14, facecolor="#0a1a2a", edgecolor="#0088cc", lw=2)
    ax.add_patch(touch_screen)
    ax.text(70, 23, "Écran Tactile 4.3\"\nStatut Encre & Menu", color="#4db8ff", fontsize=7.5, ha='center', va='center', fontweight='bold')
    
    # Bouton Power
    pwr = patches.Circle((52, 21), 2.5, facecolor="#333333", edgecolor="#00e676", lw=1.5)
    ax.add_patch(pwr)
    
    # Bac de sortie papier avant
    tray = patches.Rectangle((18, 14), 30, 12, facecolor="#141414", edgecolor="#333333")
    ax.add_patch(tray)
    ax.text(33, 20, "Bac de Sortie Rétractable", color="#777777", fontsize=7, ha='center')

    # Annotations
    ax.annotate("Écran LCD tactile couleur 4.3 pouces\n(Interface de maintenance autonome)", xy=(70, 28), xytext=(70, 48),
                ha='center', fontsize=8, fontweight='bold',
                arrowprops=dict(arrowstyle="->", color="#0088cc", lw=1.5))
                
    ax.annotate("Bouton d'alimentation Marche/Arrêt", xy=(52, 24), xytext=(40, 5),
                ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#00e676", lw=1.2))

    ax.annotate("Fente d'alimentation manuelle Fine Art avant\n(Pour médias épais jusqu'à 1.5 mm)", xy=(33, 14), xytext=(15, 3),
                ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#ffaa00", lw=1.2))

    plt.title("Epson SureColor SC-P700 - Vue de Face et Interface Opérateur", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_EPSON_01_Vue_Face_Panneau_Tactile_P700.png"))
    plt.close()

# -------------------------------------------------------------
# 8. Epson P700 - Boîtier de Maintenance C12C935711
# -------------------------------------------------------------
def make_epson_maintenance_box():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    
    # Châssis flanc droit
    side = patches.Rectangle((10, 10), 35, 42, facecolor="#222222", edgecolor="#111111", lw=2)
    ax.add_patch(side)
    
    # Logement ouvert du boîtier de maintenance
    slot = patches.Rectangle((18, 15), 22, 22, facecolor="#0a0a0a", edgecolor="#555555", lw=1.5, linestyle="--")
    ax.add_patch(slot)
    
    # Boîtier de maintenance C12C935711 extrait
    mbox = patches.Rectangle((55, 15), 32, 22, facecolor="#424242", edgecolor="#000000", lw=2)
    ax.add_patch(mbox)
    ax.text(71, 28, "Boîtier de Maintenance\nRéf: C12C935711\n(Collecteur d'encre usagée)", 
            color="white", fontsize=7.5, ha='center', va='center', fontweight='bold')
            
    # Puce électronique IC verte
    chip = patches.Rectangle((56, 17), 5, 8, facecolor="#2e7d32", edgecolor="#ffd700", lw=1.5)
    ax.add_patch(chip)
    ax.text(58.5, 21, "IC", color="white", fontsize=5.5, ha='center', va='center')
    
    # Flèche d'extraction
    ax.annotate("", xy=(53, 26), xytext=(42, 26),
                arrowprops=dict(arrowstyle="<-", color="#ff9800", lw=3))
    ax.text(47, 30, "Extraction", color="#ff9800", fontsize=8, ha='center', fontweight='bold')

    # Avertissement Puce
    ax.annotate("ATTENTION : Ne jamais toucher les contacts\nde la puce électronique verte (risque d'erreur permanente)", 
                xy=(58, 17), xytext=(40, 5), ha='center', fontsize=8, fontweight='bold', color="#d32f2f",
                arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.5))
                
    # Sachets hermétiques
    ax.annotate("Placer le boîtier usagé dans le sac plastique\nhermétique fourni pour éviter toute fuite", 
                xy=(80, 37), xytext=(80, 50), ha='center', fontsize=7.5,
                arrowprops=dict(arrowstyle="->", color="#0088cc", lw=1.2))

    plt.title("Epson SC-P700 - Procédure de Remplacement du Boîtier de Maintenance (C12C935711)", 
              fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_EPSON_02_Schema_Remplacement_Boitier_Maintenance.png"))
    plt.close()

# -------------------------------------------------------------
# 9. Epson P700 - Pattern Nozzle Check (Test des buses)
# -------------------------------------------------------------
def make_epson_nozzle_pattern():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5), dpi=150)
    
    for ax, title, is_clogged in [(ax1, "État Normal (Buses 100% Fonctionnelles)", False),
                                  (ax2, "État Obstrué (Nettoyage Tête Requis)", True)]:
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_facecolor("#fafafa")
        ax.set_title(title, fontsize=10, fontweight='bold', color="#111111" if not is_clogged else "#c62828")
        
        # 10 canaux de couleurs
        colors_list = [
            ("PB", "#111111"), ("C", "#00bcd4"), ("VM", "#d81b60"), ("Y", "#fbc02d"),
            ("LC", "#80deea"), ("VLM", "#f48fb1"), ("GY", "#757575"), ("LGY", "#bdbdbd"),
            ("MB", "#212121"), ("V", "#7b1fa2")
        ]
        
        y = 90
        for code, col in colors_list:
            ax.text(10, y, code, color=col, fontsize=7.5, fontweight='bold', va='center')
            # Grille en escalier
            for step in range(12):
                x_pos = 25 + step * 5
                y_offset = (step % 3) * 1.5
                if is_clogged and code in ["C", "PB", "VLM"] and step in [4, 5, 8]:
                    continue # Buse manquante !
                ax.plot([x_pos, x_pos + 4], [y + y_offset, y + y_offset], color=col, lw=1.8)
            y -= 8.5
            
        ax.axis('off')
        
    plt.suptitle("Epson SureColor P700 - Motif de Vérification des Buses (Nozzle Check Pattern)", 
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_EPSON_03_Pattern_Test_Buses_Nozzle_Check.png"))
    plt.close()

# -------------------------------------------------------------
# 10. Epson P700 - Disposition Cartouches T46S
# -------------------------------------------------------------
def make_epson_cartridges_layout():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    
    # Baie de chargement
    bay = patches.Rectangle((5, 10), 90, 32, facecolor="#262626", edgecolor="#111111", lw=2)
    ax.add_patch(bay)
    
    cartridges = [
        ("PB", "Photo\nBlack", "#1a1a1a", "white"),
        ("C", "Cyan", "#00bcd4", "black"),
        ("VM", "Vivid\nMag.", "#e91e63", "white"),
        ("Y", "Yellow", "#ffeb3b", "black"),
        ("LC", "Light\nCyan", "#b2ebf2", "black"),
        ("VLM", "Vivid\nLt Mag", "#f8bbd0", "black"),
        ("GY", "Gray", "#757575", "white"),
        ("LGY", "Light\nGray", "#e0e0e0", "black"),
        ("MB", "Matte\nBlack", "#37474f", "white"),
        ("V", "Violet", "#6a1b9a", "white"),
    ]
    
    x = 8
    for code, name, bg, fg in cartridges:
        c = patches.Rectangle((x, 15), 7.5, 22, facecolor=bg, edgecolor="#000000", lw=1.2)
        ax.add_patch(c)
        ax.text(x + 3.75, 27, code, color=fg, fontsize=8, fontweight='bold', ha='center', va='center')
        ax.text(x + 3.75, 19, name, color=fg, fontsize=5.5, ha='center', va='center')
        # Levier de verrouillage
        lock = patches.Rectangle((x + 1.5, 38), 4.5, 2.5, facecolor="#616161", edgecolor="#000000")
        ax.add_patch(lock)
        x += 8.6
        
    ax.text(50, 6, "10 Cartouches d'encre pigmentaire UltraChrome PRO10 (Série T46S - Capacité 25 ml)", 
            ha='center', fontsize=8.5, fontweight='bold', color="#222222")

    plt.title("Epson SC-P700 - Baie et Ordre des Cartouches d'Encre T46S", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_EPSON_04_Disposition_Cartouches_T46S.png"))
    plt.close()

# -------------------------------------------------------------
# 11. Epson P700 - Cheminement Papier & Bourrages
# -------------------------------------------------------------
def make_epson_paper_path():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis('off')
    
    # Schéma en coupe
    # Bac supérieur arrière
    p1 = patches.Polygon([(15, 65), (25, 45), (32, 45), (22, 65)], facecolor="#90caf9", edgecolor="#1565c0", lw=1.5)
    ax.add_patch(p1)
    ax.text(18, 67, "1. Bac Arrière Feuille à Feuille\n(Papier ordinaire & photo standard)", fontsize=7.5, fontweight='bold', color="#0d47a1")
    
    # Entrée manuelle avant Fine Art
    p2 = patches.Polygon([(80, 35), (55, 35), (55, 32), (80, 32)], facecolor="#a5d6a7", edgecolor="#2e7d32", lw=1.5)
    ax.add_patch(p2)
    ax.text(82, 33, "2. Chargement Manuel Avant Fine Art\n(Médias d'art épais jusqu'à 1.5mm)", fontsize=7.5, fontweight='bold', color="#1b5e20")
    
    # Tête d'impression et platine
    platen = patches.Rectangle((30, 28), 35, 4, facecolor="#424242", edgecolor="#000000")
    head = patches.Rectangle((42, 35), 12, 8, facecolor="#d32f2f", edgecolor="#b71c1c", lw=1.5)
    ax.add_patch(platen)
    ax.add_patch(head)
    ax.text(48, 39, "Tête MicroPiezo\n(10 canaux)", color="white", fontsize=6, ha='center', va='center')
    
    # Rouleaux d'entraînement
    r1 = patches.Circle((32, 34), 3, facecolor="#757575", edgecolor="#212121")
    r2 = patches.Circle((62, 34), 3, facecolor="#757575", edgecolor="#212121")
    ax.add_patch(r1)
    ax.add_patch(r2)
    
    # Chemin papier fléché
    ax.plot([25, 32, 48, 62, 75], [45, 34, 33, 33, 20], color="#ff9800", lw=2.5, linestyle=":")
    
    # Points de bourrage
    ax.annotate("Point de bourrage A :\nRouleaux d'alimentation arrière", xy=(32, 37), xytext=(12, 25),
                ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.2))
                
    ax.annotate("Point de bourrage B :\nSous le chariot d'impression", xy=(48, 32), xytext=(48, 15),
                ha='center', fontsize=7.5, arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.2))

    plt.title("Epson SC-P700 - Cheminement Papier et Zones Fréquentes de Bourrage", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_EPSON_05_Cheminement_Papier_Bourrage.png"))
    plt.close()

# -------------------------------------------------------------
# 12. Epson P700 - Organigramme Dépannage Qualité Impression
# -------------------------------------------------------------
def make_epson_troubleshooting_flow():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    def b(x, y, w, h, text, bg="#e8eaf6", ec="#3f51b5", bold=False):
        p = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1", facecolor=bg, edgecolor=ec, lw=1.5)
        ax.add_patch(p)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=7.5, fontweight=weight)
        
    def ar(x1, y1, x2, y2, label=""):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color="#263238", lw=1.5))
        if label:
            ax.text((x1+x2)/2 + 2, (y1+y2)/2, label, fontsize=7, color="#d81b60", fontweight='bold')

    b(30, 88, 40, 8, "Symptôme : Lignes blanches / Banding\nou décoloration sur tirage", bg="#ffebee", ec="#c62828", bold=True)
    
    b(30, 72, 40, 8, "1. Exécuter un Test des Buses\n(Nozzle Check) via l'écran tactile")
    ar(50, 88, 50, 80)
    
    b(10, 54, 35, 8, "Motif Parfait sans coupure\n-> Problème réglage média ou profil ICC")
    b(55, 54, 35, 8, "Segments manquants détectés\n-> Procéder au Nettoyage standard")
    ar(40, 72, 27, 62, "Normal")
    ar(60, 72, 72, 62, "Coupures")
    
    b(55, 36, 35, 9, "Lancer 1 à 2 cycles de\nNettoyage Standard (Tête)")
    ar(72, 54, 72, 45)
    
    b(35, 18, 30, 10, "Buses débouchées ?\nOUI -> Reprendre l'impression\nNON -> Pause repos 6 à 12h requise", bg="#e8f5e9", ec="#2e7d32", bold=True)
    ar(65, 36, 55, 28)
    
    b(70, 18, 25, 10, "Si échec après 12h :\nPower Cleaning\n(Cartouches > 33% requises)", bg="#fff3e0", ec="#ef6c00")
    ar(78, 36, 82, 28)

    plt.title("Epson SC-P700 - Organigramme Décisionnel de Maintenance des Buses", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "IMG_EPSON_06_Organigramme_Depannage_Qualite_Impression.png"))
    plt.close()

if __name__ == "__main__":
    print("Génération des 12 images techniques...")
    make_canon_top_panel()
    make_canon_back_panel()
    make_canon_connectors()
    make_canon_sensor_cleaning()
    make_canon_error_flowchart()
    make_canon_led_indicators()
    make_epson_front_view()
    make_epson_maintenance_box()
    make_epson_nozzle_pattern()
    make_epson_cartridges_layout()
    make_epson_paper_path()
    make_epson_troubleshooting_flow()
    print("12 images générées avec succès dans", OUTPUT_DIR)
