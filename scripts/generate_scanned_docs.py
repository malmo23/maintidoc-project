"""
Script de génération des 2 documents scannés simulés (PDF basés sur des images raster pures).
Destinés à tester l'OCR local (extraction de texte par vision).
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

DIR_FAMILLE_1 = os.path.join("L1_MaintiDoc_TeamName_Corpus", "documents", "famille_1")
DIR_FAMILLE_2 = os.path.join("L1_MaintiDoc_TeamName_Corpus", "documents", "famille_2")
os.makedirs(DIR_FAMILLE_1, exist_ok=True)
os.makedirs(DIR_FAMILLE_2, exist_ok=True)

W, H = 1654, 2338 # A4 à ~200 DPI

def get_font(size, bold=False):
    # Polices standard Windows
    try:
        font_name = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(font_name, size)
    except:
        return ImageFont.load_default()

def create_paper_texture():
    # Fond papier légèrement vieilli / crème
    base = np.full((H, W, 3), [250, 248, 243], dtype=np.uint8)
    # Bruit de scan léger
    noise = np.random.normal(0, 3, (H, W, 3)).astype(np.int16)
    textured = np.clip(base + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(textured)

def draw_rubber_stamp(draw, cx, cy, text_lines, color=(160, 30, 30, 200)):
    # Tampon d'atelier circulaire
    r = 95
    for dr in range(3):
        draw.ellipse([cx - r + dr, cy - r + dr, cx + r - dr, cy + r - dr], outline=color, width=3)
    draw.ellipse([cx - r + 15, cy - r + 15, cx + r - 15, cy + r - 15], outline=color, width=1)
    
    f = get_font(18, bold=True)
    for i, line in enumerate(text_lines):
        bbox = draw.textbbox((0, 0), line, font=f)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw / 2, cy - 25 + i * 22), line, fill=color, font=f)

def generate_canon_scan():
    img = create_paper_texture()
    draw = ImageDraw.Draw(img)
    
    f_title = get_font(34, bold=True)
    f_header = get_font(20, bold=True)
    f_body = get_font(18, bold=False)
    f_hand = get_font(20, bold=True) # texte d'intervention
    f_small = get_font(15, bold=False)
    
    # En-tête officiel
    draw.rectangle([80, 80, W - 80, 210], outline=(40, 40, 40), width=3)
    draw.text((110, 100), "CENTRE TECHNIQUE AUDIOVISUEL RÉGIONAL - SAV AGRÉÉ", fill=(10, 10, 10), font=f_title)
    draw.text((110, 150), "FICHE D'INTERVENTION TERRAIN & CONTRÔLE QUALITÉ MATÉRIEL", fill=(60, 60, 60), font=f_header)
    
    # Métadonnées
    draw.rectangle([80, 230, W - 80, 440], outline=(80, 80, 80), width=2)
    draw.line([80, 300, W - 80, 300], fill=(120, 120, 120), width=1)
    draw.line([80, 370, W - 80, 370], fill=(120, 120, 120), width=1)
    draw.line([850, 230, 850, 440], fill=(120, 120, 120), width=1)
    
    draw.text((100, 255), "Équipement :", font=f_header, fill=(30, 30, 30))
    draw.text((280, 255), "Canon EOS R50 (Boîtier Hybride APS-C)", font=f_hand, fill=(10, 20, 120))
    
    draw.text((870, 255), "N° Série :", font=f_header, fill=(30, 30, 30))
    draw.text((1000, 255), "SN-R50-4892019-EU", font=f_hand, fill=(10, 20, 120))
    
    draw.text((100, 325), "Date intervention :", font=f_header, fill=(30, 30, 30))
    draw.text((330, 325), "14 Janvier 2026", font=f_hand, fill=(10, 20, 120))
    
    draw.text((870, 325), "Compteur Oburateur :", font=f_header, fill=(30, 30, 30))
    draw.text((1150, 325), "12 450 cycles", font=f_hand, fill=(10, 20, 120))
    
    draw.text((100, 395), "Technicien :", font=f_header, fill=(30, 30, 30))
    draw.text((270, 395), "M. Laurent DUPUIS (Matricule 409)", font=f_hand, fill=(10, 20, 120))
    
    draw.text((870, 395), "Statut garantie :", font=f_header, fill=(30, 30, 30))
    draw.text((1080, 395), "Sous contrat PRO-MAINT", font=f_hand, fill=(10, 20, 120))

    # Section 1 : Symptôme & Diagnostic initial
    draw.rectangle([80, 470, W - 80, 720], outline=(80, 80, 80), width=2)
    draw.text((100, 485), "1. SYMPTÔMES SIGNALÉS PAR L'UTILISATEUR & CONSTAT INITIAL", font=f_header, fill=(20, 20, 20))
    draw.text((110, 530), "• Taches sombres récurrentes visibles sur toutes les photos à ouverture f/8 et f/16.", font=f_body, fill=(40, 40, 40))
    draw.text((110, 570), "• Apparition sporadique du code erreur Err 01 avec l'optique RF-S 18-45mm f/4.5-6.3 IS STM.", font=f_body, fill=(40, 40, 40))
    draw.text((110, 610), "• Constat atelier : Poussières grasses et filaments déposés sur la lamelle extérieure du filtre capteur.", font=f_hand, fill=(10, 20, 120))
    draw.text((110, 650), "• Dépôt d'oxydation superficielle sur le 4e plot de contact monture côté boîtier.", font=f_hand, fill=(10, 20, 120))

    # Section 2 : Travaux de maintenance effectués
    draw.rectangle([80, 750, W - 80, 1300], outline=(80, 80, 80), width=2)
    draw.text((100, 765), "2. OPÉRATIONS TECHNIQUES RÉALISÉES (PROTOCOLE CANON STANDARD)", font=f_header, fill=(20, 20, 20))
    
    items = [
        ("[X] Démontage optique et aspiration en chambre blanche classe 1000", True),
        ("[X] Nettoyage manuel capteur CMOS à la poire soufflante dépoussiérée (15 mm distance)", True),
        ("[X] Traitement chiffon microfibre sec sans solvant sur bague monture et contacts RF", True),
        ("[X] Mise à niveau firmware boîtier de la v1.1.0 vers v1.2.0 (correctif communication Err 01)", True),
        ("[X] Test de déclenchement obturateur électronique : 50 cycles sans anomalie", True),
        ("[X] Vérification tension accumulateur LP-E17 : 8.12V en pleine charge (Conforme)", True),
        ("[X] Calibrage balance des blancs et contrôle centrage capteur autofocus Dual Pixel II", True),
        ("[X] Test prise de vue ciel clair à f/22 : Aucun résidu de poussière détecté", True)
    ]
    
    y = 820
    for txt, ok in items:
        draw.text((120, y), txt, font=f_body, fill=(10, 10, 10))
        y += 55

    # Section 3 : Recommandations pour l'opérateur
    draw.rectangle([80, 1330, W - 80, 1700], outline=(80, 80, 80), width=2)
    draw.text((100, 1345), "3. RECOMMANDATIONS & CONSIGNES DE SÉCURITÉ TRANSMISES AU CLIENT", font=f_header, fill=(20, 20, 20))
    draw.text((110, 1395), "1. Ne JAMAIS vaporiser de gaz comprimé ni d'alcool isopropylique directement dans la cage.", font=f_body, fill=(180, 20, 20))
    draw.text((110, 1445), "2. Activer l'option 'Nettoyage capteur automatique à l'extinction' dans le menu Configuration 4.", font=f_body, fill=(40, 40, 40))
    draw.text((110, 1495), "3. Conserver l'appareil en environnement sec (taux d'humidité recommandé < 60%).", font=f_body, fill=(40, 40, 40))
    draw.text((110, 1545), "4. Prochaine visite de contrôle préventif programmée à 25 000 déclenchements ou dans 12 mois.", font=f_hand, fill=(10, 20, 120))

    # Section 4 : Signatures et Tampon d'Atelier
    draw.rectangle([80, 1730, W - 80, 2180], outline=(80, 80, 80), width=2)
    draw.text((120, 1760), "Visa du Responsable d'Atelier :", font=f_header, fill=(30, 30, 30))
    draw.text((120, 1810), "L. Dupuis (Signé numériquement)", font=f_hand, fill=(10, 20, 120))
    
    draw.text((1000, 1760), "Signature & Accord Client :", font=f_header, fill=(30, 30, 30))
    draw.text((1000, 1810), "Bon pour réception - Matériel testé conforme", font=f_small, fill=(70, 70, 70))
    
    # Tampon rouge
    draw_rubber_stamp(draw, 500, 1980, ["ATELIER CENTRAL", "MAINTENANCE SAV", "VALIDÉ CONFORME", "14 JAN 2026"])

    # Rotation légère pour simuler le passage dans le scanner vitre
    tilted = img.rotate(0.7, resample=Image.BICUBIC, expand=False, fillcolor=(235, 230, 222))
    
    # Sauvegarde temporaire image puis PDF
    tmp_path = os.path.join(DIR_FAMILLE_1, "tmp_scan_canon.png")
    pdf_path = os.path.join(DIR_FAMILLE_1, "DOC_CANON_09_Fiche_Intervention_Terrain_Scan.pdf")
    tilted.save(tmp_path, "PNG")
    
    # Assemblage PDF raster sans flux texte
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.drawImage(tmp_path, 0, 0, width=A4[0], height=A4[1])
    c.save()
    os.remove(tmp_path)
    print("PDF scanné Canon généré :", pdf_path)

def generate_epson_scan():
    img = create_paper_texture()
    draw = ImageDraw.Draw(img)
    
    f_title = get_font(32, bold=True)
    f_header = get_font(20, bold=True)
    f_body = get_font(18, bold=False)
    f_hand = get_font(20, bold=True)
    f_small = get_font(15, bold=False)
    
    # En-tête
    draw.rectangle([80, 80, W - 80, 210], outline=(30, 30, 30), width=3)
    draw.text((110, 100), "DÉPARTEMENT TECHNIQUE - SYSTÈMES D'IMPRESSION PRO", fill=(10, 10, 10), font=f_title)
    draw.text((110, 150), "RAPPORT D'ATELIER : RÉVISION TÊTE D'IMPRESSION & BOÎTIER MAINTENANCE", fill=(60, 60, 60), font=f_header)
    
    # Métadonnées
    draw.rectangle([80, 230, W - 80, 440], outline=(80, 80, 80), width=2)
    draw.line([80, 300, W - 80, 300], fill=(120, 120, 120), width=1)
    draw.line([80, 370, W - 80, 370], fill=(120, 120, 120), width=1)
    draw.line([850, 230, 850, 440], fill=(120, 120, 120), width=1)
    
    draw.text((100, 255), "Machine :", font=f_header, fill=(30, 30, 30))
    draw.text((240, 255), "Epson SureColor SC-P700 (A3+ 17 pouces)", font=f_hand, fill=(120, 10, 20))
    
    draw.text((870, 255), "N° Série :", font=f_header, fill=(30, 30, 30))
    draw.text((1000, 255), "SN-SCP700-993821-FR", font=f_hand, fill=(120, 10, 20))
    
    draw.text((100, 325), "Date visite :", font=f_header, fill=(30, 30, 30))
    draw.text((270, 325), "22 Février 2026", font=f_hand, fill=(120, 10, 20))
    
    draw.text((870, 325), "Total tirages :", font=f_header, fill=(30, 30, 30))
    draw.text((1050, 325), "3 842 feuilles A3+ / FineArt", font=f_hand, fill=(120, 10, 20))
    
    draw.text((100, 395), "Intervenant :", font=f_header, fill=(30, 30, 30))
    draw.text((270, 395), "Thierry VASSEUR (Ingénieur Support Imagerie)", font=f_hand, fill=(120, 10, 20))
    
    draw.text((870, 395), "État initial :", font=f_header, fill=(30, 30, 30))
    draw.text((1030, 395), "Code erreur bloquant 1485", font=f_hand, fill=(180, 20, 20))

    # Section 1 : Diagnostic & Analyse des anomalies
    draw.rectangle([80, 470, W - 80, 720], outline=(80, 80, 80), width=2)
    draw.text((100, 485), "1. DIAGNOSTIC PANNE & ÉTAT DES COMPTEURS INTERNES", font=f_header, fill=(20, 20, 20))
    draw.text((110, 530), "• Erreur 1485 : Capacité maximale du boîtier de maintenance atteinte (100% plein).", font=f_body, fill=(40, 40, 40))
    draw.text((110, 570), "• Blocage complet des opérations d'impression et des cycles de purge de sécurité.", font=f_body, fill=(40, 40, 40))
    draw.text((110, 610), "• Examen visuel tête d'impression : Dépôt d'encre séchée sur les canaux Cyan et Vivid Magenta.", font=f_hand, fill=(120, 10, 20))
    draw.text((110, 650), "• Motif Nozzle Check initial : 18 buses inactives sur le rang Cyan (banding prononcé).", font=f_hand, fill=(120, 10, 20))

    # Section 2 : Interventions effectuées
    draw.rectangle([80, 750, W - 80, 1300], outline=(80, 80, 80), width=2)
    draw.text((100, 765), "2. OPÉRATIONS TECHNIQUES RÉALISÉES", font=f_header, fill=(20, 20, 20))
    
    actions = [
        ("[X] Remplacement du boîtier de maintenance saturé par pièce d'origine Epson C12C935711", True),
        ("[X] Contrôle de non-altération de la puce IC et verrouillage du logement latéral", True),
        ("[X] Réinitialisation logicielle automatique du compteur de déchets d'encre (0% plein)", True),
        ("[X] Nettoyage de la station d'accueil de la tête (capping station & raclette wiper)", True),
        ("[X] Exécution d'un cycle de nettoyage standard (1 passe - buses 1 à 10 réactivées)", True),
        ("[X] Respect scrupuleux du temps de repos stabilisateur de 6 heures sous tension", True),
        ("[X] Test de tirage de mire d'alignement bidirectionnel sur papier Epson Proofing", True),
        ("[X] Vérification du bon cheminement papier manuel avant et chargeur automatique", True)
    ]
    
    y = 820
    for act, ok in actions:
        draw.text((120, y), act, font=f_body, fill=(10, 10, 10))
        y += 55

    # Section 3 : Recommandations Atelier
    draw.rectangle([80, 1330, W - 80, 1700], outline=(80, 80, 80), width=2)
    draw.text((100, 1345), "3. CONSIGNES OPÉRATIONNELLES POUR L'ATELIER", font=f_header, fill=(20, 20, 20))
    draw.text((110, 1395), "1. Toujours conserver un boîtier de secours C12C935711 en stock d'avance en salle d'impression.", font=f_body, fill=(40, 40, 40))
    draw.text((110, 1445), "2. Ne JAMAIS tenter de vider ou laver les mousses absorbantes d'un boîtier usagé (risque de fuite).", font=f_body, fill=(180, 20, 20))
    draw.text((110, 1495), "3. Ne pas enchaîner plus de 2 nettoyages consécutifs : laisser décanter les microbulles 6 heures.", font=f_body, fill=(40, 40, 40))
    draw.text((110, 1545), "4. Machine déclarée 100% opérationnelle. Recommandation étalonnage spectro tous les 3 mois.", font=f_hand, fill=(120, 10, 20))

    # Section 4 : Signatures
    draw.rectangle([80, 1730, W - 80, 2180], outline=(80, 80, 80), width=2)
    draw.text((120, 1760), "Contrôleur Qualité Impression :", font=f_header, fill=(30, 30, 30))
    draw.text((120, 1810), "T. Vasseur - Certifié EPSON PRO GRAPHICS", font=f_hand, fill=(120, 10, 20))
    
    draw.text((1000, 1760), "Validation Laboratoire Tirage :", font=f_header, fill=(30, 30, 30))
    draw.text((1000, 1810), "Conformité colorimétrique Delta E < 1.2 validée", font=f_small, fill=(70, 70, 70))
    
    # Tampon circulaire bleu/vert
    draw_rubber_stamp(draw, 500, 1980, ["EPSON CERTIFIED LAB", "MAINTENANCE VALIDÉE", "CONFORME NORME ISO", "22 FÉV 2026"], color=(20, 80, 150, 200))

    # Rotation légère
    tilted = img.rotate(-0.6, resample=Image.BICUBIC, expand=False, fillcolor=(235, 230, 222))
    
    tmp_path = os.path.join(DIR_FAMILLE_2, "tmp_scan_epson.png")
    pdf_path = os.path.join(DIR_FAMILLE_2, "DOC_EPSON_09_Rapport_Maintenance_Atelier_Scan.pdf")
    tilted.save(tmp_path, "PNG")
    
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.drawImage(tmp_path, 0, 0, width=A4[0], height=A4[1])
    c.save()
    os.remove(tmp_path)
    print("PDF scanné Epson généré :", pdf_path)

if __name__ == "__main__":
    print("Génération des 2 documents scannés simulés pour le test OCR...")
    generate_canon_scan()
    generate_epson_scan()
    print("Documents scannés générés avec succès.")
