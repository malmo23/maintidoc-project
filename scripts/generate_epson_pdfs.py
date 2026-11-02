"""
Génération des 8 documents PDF pour la Famille 2 : Epson SureColor P700.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from pdf_builder_utils import NumberedCanvas, get_doc_styles, make_callout

OUTPUT_DIR = os.path.join("L1_MaintiDoc_TeamName_Corpus", "documents", "famille_2")
os.makedirs(OUTPUT_DIR, exist_ok=True)
styles = get_doc_styles()

def build_pdf(filename, title, ref, story_func):
    path = os.path.join(OUTPUT_DIR, filename)
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=50
    )
    
    class DocNumberedCanvas(NumberedCanvas):
        doc_title = f"Epson SC-P700 - {title}"
        doc_ref = ref

    story = []
    story.append(Paragraph(title, styles['title']))
    story.append(Paragraph(f"<b>Référence :</b> {ref} | <b>Appareil :</b> Epson SureColor SC-P700 | <b>Statut :</b> Documentation Technique Officielle", styles['subtitle']))
    story.append(Spacer(1, 10))
    
    story_func(story)
    doc.build(story, canvasmaker=DocNumberedCanvas)
    print(f"PDF généré : {path}")

# -------------------------------------------------------------
# 1. DOC_EPSON_01_Guide_Utilisateur_General.pdf
# -------------------------------------------------------------
def epson_01_story(s):
    s.append(Paragraph("1. Présentation de l'Imprimante Epson SureColor SC-P700", styles['h1']))
    s.append(Paragraph("L'Epson SureColor SC-P700 est une imprimante photo professionnelle de format A3+ (13 pouces / 330 mm de largeur) dotée de la technologie de tête d'impression piézo-électrique PrecisionCore Micro TFP à 10 canaux d'encre indépendants. Elle intègre le jeu d'encres pigmentaires UltraChrome PRO10, avec des canaux dédiés pour le Noir Photo et le Noir Mat ne nécessitant aucune purge lors du basculement de support.", styles['body']))

    s.append(Paragraph("2. Description des Composants et Commandes", styles['h1']))
    s.append(Paragraph("• <b>Écran tactile couleur de 4.3 pouces :</b> Interface graphique permettant la visualisation des niveaux d'encre en temps réel, l'exécution des routines de maintenance autonome et le paramétrage réseau.<br/>"
                       "• <b>Alimentation feuille à feuille supérieure arrière :</b> Pour papiers photo brillants, lustrés, mats et papiers bureautiques (jusqu'à 30 feuilles selon grammage).<br/>"
                       "• <b>Alimentation manuelle avant Fine Art :</b> Trajet rectiligne dédié aux papiers d'art épais et cartons rigides jusqu'à 1.5 mm d'épaisseur.<br/>"
                       "• <b>Unité rouleau intégrée :</b> Supporte les rouleaux sans mandrin (bobines de 2 pouces et 3 pouces) avec coupe automatique motorisée.", styles['body']))

    s.append(PageBreak())
    s.append(Paragraph("3. Spécifications Techniques Principales", styles['h1']))
    data = [
        [Paragraph("<b>Caractéristique</b>", styles['header']), Paragraph("<b>Spécification Constructeur</b>", styles['header'])],
        [Paragraph("Technologie de tête", styles['cell']), Paragraph("Tête d'impression PrecisionCore Micro TFP 10 canaux", styles['cell'])],
        [Paragraph("Résolution maximale", styles['cell']), Paragraph("5760 x 1440 ppp (points par pouce)", styles['cell'])],
        [Paragraph("Taille minimale de goutte", styles['cell']), Paragraph("1.5 picolitre (technologie à taille de point variable VSDT)", styles['cell'])],
        [Paragraph("Type d'encre", styles['cell']), Paragraph("Encre pigmentaire UltraChrome PRO10 (10 couleurs T46S)", styles['cell'])],
        [Paragraph("Format papier maximal", styles['cell']), Paragraph("Largeur 330 mm (A3+), longueur jusqu'à 2 mètres", styles['cell'])],
        [Paragraph("Boîtier de maintenance", styles['cell']), Paragraph("Réf. C12C935711 (remplaçable par l'utilisateur)", styles['cell'])],
        [Paragraph("Connectivité", styles['cell']), Paragraph("USB 3.0 SuperSpeed, Ethernet Gigabit 1000Base-T, Wi-Fi 5 GHz", styles['cell'])],
    ]
    t = Table(data, colWidths=[180, A4[0] - 80 - 180])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0055aa")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f4f9ff")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    s.append(t)

# -------------------------------------------------------------
# 2. DOC_EPSON_02_Remplacement_Boitier_Maintenance_C12C935711.pdf
# -------------------------------------------------------------
def epson_02_story(s):
    s.append(Paragraph("1. Fonction et Rôle du Boîtier de Maintenance", styles['h1']))
    s.append(Paragraph("Le boîtier de maintenance (part number constructeur : <b>C12C935711</b>) recueille le surplus d'encre évacué lors des cycles de nettoyage des buses, des purges d'amorçage, de l'impression sans marge et des changements de configuration. Il contient un feutre multicouche ultra-absorbant haute densité.", styles['body']))

    s.append(Paragraph("2. Messages d'Alerte et Comportement de la Machine", styles['h1']))
    s.append(Paragraph("• <b>'Le boîtier de maintenance approche de la fin de sa durée de service' :</b> Avertissement préventif. L'impression reste possible temporairement, mais un boîtier C12C935711 de rechange doit être approvisionné sans délai.<br/>"
                       "• <b>'Remplacer le boîtier de maintenance' (Code Erreur 1485) :</b> Le boîtier est saturé. Par sécurité absolue pour éviter tout débordement d'encre toxique à l'intérieur du châssis, l'imprimante <b>verrouille intégralement toutes les impressions et cycles de nettoyage</b> tant que la pièce n'est pas remplacée.", styles['body']))

    s.append(Paragraph("3. Procédure Pas à Pas de Remplacement", styles['h1']))
    s.append(Paragraph("1. Assurez-vous que l'imprimante n'est pas en train d'imprimer.<br/>"
                       "2. Ouvrez le couvercle d'accès au boîtier de maintenance situé sur le flanc inférieur droit de l'appareil.<br/>"
                       "3. Tirez fermement le boîtier usagé vers l'extérieur en le maintenant parfaitement à plat.<br/>"
                       "4. Placez immédiatement le boîtier usagé dans le sac plastique étanche hermétique fourni avec la pièce neuve et refermez hermétiquement la fermeture zippée.<br/>"
                       "5. Déballez le nouveau boîtier <b>C12C935711</b>. Insérez-le dans son logement jusqu'à ce qu'il s'enclenche dans la butée mécanique.<br/>"
                       "6. Refermez le couvercle latéral. L'imprimante détecte la nouvelle puce et réinitialise automatiquement son compteur interne à 100% de capacité libre.", styles['body']))

    s.append(PageBreak())
    s.append(Paragraph("4. Précautions Indispensables de Manipulation", styles['h1']))
    s.append(make_callout("PROTECTION DE LA PUCE ÉLECTRONIQUE VERTE :<br/>"
                          "Ne touchez en aucun cas les contacts métalliques de la puce IC verte située sur le côté du boîtier de maintenance.<br/>"
                          "La sueur cutanée, le sébum ou une décharge électrostatique peuvent endommager la puce, empêchant la reconnaissance du boîtier neuf par l'imprimante.", "warning", styles))
    s.append(Spacer(1, 12))
    s.append(make_callout("INTERDICTION DE RÉUTILISATION : Ne tentez jamais de laver, rincer ou vider un boîtier de maintenance saturé. Les feutres absorbants détériorés ne retiennent plus les pigments et provoqueront des fuites destructrices sur la platine électronique principale.", "danger", styles))

# -------------------------------------------------------------
# 3. DOC_EPSON_03_Table_Codes_Erreurs_Solutions.pdf
# -------------------------------------------------------------
def epson_03_story(s):
    s.append(Paragraph("1. Tableau Exhaustif des Codes d'Erreurs Epson SC-P700", styles['h1']))
    s.append(Paragraph("Ce tableau répertorie les codes d'erreurs hexadécimaux et numériques retournés par l'interface logicielle et l'écran tactile du SC-P700, avec leurs actions correctives d'atelier.", styles['body']))

    data = [
        [Paragraph("<b>Code</b>", styles['header']), Paragraph("<b>Description Erreur</b>", styles['header']), Paragraph("<b>Cause Matérielle</b>", styles['header']), Paragraph("<b>Action de Dépannage Immédiate</b>", styles['header'])],
        [
            Paragraph("<b>1485</b>", styles['cell']),
            Paragraph("Boîtier maintenance plein", styles['cell']),
            Paragraph("Feutres saturés à 100%, puce IC verrouillée.", styles['cell']),
            Paragraph("Remplacer immédiatement le boîtier de maintenance usagé par la réf. C12C935711.", styles['cell'])
        ],
        [
            Paragraph("<b>1404</b>", styles['cell']),
            Paragraph("Cartouche non reconnue", styles['cell']),
            Paragraph("Puce de cartouche encrassée ou mal clipsée.", styles['cell']),
            Paragraph("Ouvrir le capot de la baie, réenclencher fermement la cartouche T46S ou essuyer la puce.", styles['cell'])
        ],
        [
            Paragraph("<b>000100</b>", styles['cell']),
            Paragraph("Erreur chargement papier", styles['cell']),
            Paragraph("Bourrage ou galets d'entraînement encrassés.", styles['cell']),
            Paragraph("Retirer le papier froissé, vérifier les guides latéraux et nettoyer les rouleaux d'alimentation.", styles['cell'])
        ],
        [
            Paragraph("<b>000185</b>", styles['cell']),
            Paragraph("Format de papier non concordant", styles['cell']),
            Paragraph("Le papier inséré ne correspond pas au pilote.", styles['cell']),
            Paragraph("Vérifier les dimensions dans le pilote Epson Print Layout et recharger le format adéquat.", styles['cell'])
        ],
        [
            Paragraph("<b>031008</b>", styles['cell']),
            Paragraph("Erreur capteur tête d'impression", styles['cell']),
            Paragraph("Surchauffe transitoire de la tête Micro TFP.", styles['cell']),
            Paragraph("Éteindre l'appareil, laisser refroidir 30 minutes. Rallumer. Si persistance, atelier SAV.", styles['cell'])
        ],
        [
            Paragraph("<b>038001</b>", styles['cell']),
            Paragraph("Erreur moteur chariot (CR)", styles['cell']),
            Paragraph("Obstacle physique sur la course du chariot.", styles['cell']),
            Paragraph("Couper le secteur, vérifier qu'aucun morceau de papier ne bloque la bande encodeuse CR.", styles['cell'])
        ],
        [
            Paragraph("<b>000031</b>", styles['cell']),
            Paragraph("Erreur détection bord papier", styles['cell']),
            Paragraph("Capteur optique PW encrassé par des poussières.", styles['cell']),
            Paragraph("Dépoussiérer le capteur inférieur avec une poire soufflante propre.", styles['cell'])
        ],
    ]
    t = Table(data, colWidths=[55, 105, 130, A4[0] - 80 - 290])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0055aa")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f0f7ff")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    s.append(t)

# -------------------------------------------------------------
# 4. DOC_EPSON_04_Guide_Maintenance_Tete_Standard.pdf (CONTRADICTION 2)
# -------------------------------------------------------------
def epson_04_story(s):
    s.append(Paragraph("1. Importance du Test des Buses (Nozzle Check)", styles['h1']))
    s.append(Paragraph("La tête PrecisionCore Micro TFP dispose de buses microscopiques expulsant des gouttes de 1.5 picolitre. La présence de pigments secs ou d'air dans les canaux engendre des lignes blanches transversales (banding). Avant tout nettoyage, un test des buses doit impérativement être imprimé pour cartographier les canaux défaillants.", styles['body']))

    s.append(Paragraph("2. Protocole Officiel de Nettoyage de la Tête (Méthode Standard)", styles['h1']))
    s.append(Paragraph("1. Chargez une feuille de papier ordinaire au format A4 dans le bac arrière.<br/>"
                       "2. Sur l'écran tactile, appuyez sur l'icône <b>[Maintenance]</b> -> <b>[Vérification des buses]</b> -> <b>[Imprimer]</b>.<br/>"
                       "3. Examinez le motif imprimé. Si un seul canal présente des segments manquants, sélectionnez <b>[Nettoyer la tête]</b>.<br/>"
                       "4. À la fin du cycle de nettoyage, réimprimez un test de vérification des buses.<br/>"
                       "5. Si le motif n'est pas encore parfait, effectuez un <b>deuxième cycle de nettoyage standard</b>.", styles['body']))

    s.append(PageBreak())
    s.append(Paragraph("3. Règle d'Or Constructeur : La Règle des 12 Heures de Repos", styles['h1']))
    
    s.append(make_callout("LIMITE DES CYCLES CONSECUTIFS ET TEMPS DE DÉCANTATION :<br/>"
                          "Epson prescrit de ne JAMAIS lancer plus de 2 à 3 nettoyages consécutifs.<br/>"
                          "Chaque nettoyage injecte de l'encre sous pression qui génère de microbulles d'air par cavitation. Enchaîner les nettoyages aggrave l'obstruction des buses et gaspille massivement l'encre tout en saturant inutilement le boîtier C12C935711.<br/>"
                          "<b>Règle obligatoire :</b> Si le problème persiste après 2 nettoyages, éteignez l'imprimante et <b>laissez reposer l'appareil pendant au minimum 6 à 12 heures</b> sans sollicitation. L'encre fraîche dissout naturellement les dépôts solides pendant cette période.", "contradiction", styles))
    s.append(Spacer(1, 12))

    s.append(Paragraph("4. Nettoyage Puissant (Power Cleaning) : Conditions Strictes", styles['h1']))
    s.append(Paragraph("Le Power Cleaning est une procédure lourde d'aspiration réservée aux colmatages persistants :<br/>"
                       "• <b>Prérequis de niveau d'encre :</b> Chaque cartouche T46S doit afficher au moins <b>33% (un tiers) de niveau restant</b>.<br/>"
                       "• <b>Fréquence maximale :</b> 1 seule fois. Si les buses ne sont pas rétablies après 1 Power Cleaning, patientez 12 heures supplémentaires avant tout nouvel essai.", styles['body']))

# -------------------------------------------------------------
# 5. DOC_EPSON_06_Gestion_Cartouches_Encre_UltraChrome_PRO10.pdf
# -------------------------------------------------------------
def epson_06_story(s):
    s.append(Paragraph("1. Système d'Encres UltraChrome PRO10 (Série T46S)", styles['h1']))
    s.append(Paragraph("Le système d'encres UltraChrome PRO10 comprend 10 cartouches indépendantes scellées sous vide de 25 ml chacune. Cette technologie garantit une gamme chromatique étendue et une stabilité d'archivage exceptionnelle (jusqu'à 200 ans en conditions de conservation muséale).", styles['body']))

    s.append(Paragraph("2. Remplacement d'une Cartouche Épuisée", styles['h1']))
    s.append(Paragraph("1. Ouvrez le volet rabattable de la baie de cartouches située en partie supérieure de l'imprimante.<br/>"
                       "2. Poussez doucement sur la cartouche indiquée par l'écran tactile pour déverrouiller son loquet de maintien.<br/>"
                       "3. Extrayez la cartouche verticalement.<br/>"
                       "4. <b>Secouage préparatoire :</b> Secouez la cartouche neuve horizontalement environ <b>15 fois en 5 secondes</b> dans son emballage avant ouverture pour homogénéiser les pigments colloïdaux.<br/>"
                       "5. Retirez le ruban adhésif jaune de mise à l'air libre scellant la cartouche. Ne touchez pas la puce latérale dorée.<br/>"
                       "6. Insérez fermement la cartouche dans son logement jusqu'au clic mécanique, puis refermez le couvercle.", styles['body']))

    s.append(make_callout("N'installez jamais une cartouche sans avoir préalablement retiré la bande jaune de protection. Si la mise à l'air libre reste obturée, la pompe d'aspiration crée une dépression dans le circuit d'encre, provoquant le désamorçage complet de la tête.", "warning", styles))

# -------------------------------------------------------------
# 6. DOC_EPSON_07_Procedure_Alignement_Tete_Impression.pdf
# -------------------------------------------------------------
def epson_07_story(s):
    s.append(Paragraph("1. Objectif de l'Alignement de la Tête d'Impression", styles['h1']))
    s.append(Paragraph("L'alignement optimise la précision géométrique de projection des microgouttes lors des allers-retours du chariot (impression bidirectionnelle). Un mauvais alignement provoque un flou de bougé, des dédoublements de contours ou un lignage régulier.", styles['body']))

    s.append(Paragraph("2. Procédure d'Alignement Automatique", styles['h1']))
    s.append(Paragraph("1. Chargez 2 feuilles de papier photo glacé ou de papier couché de haute qualité dans le bac arrière.<br/>"
                       "2. Sur l'écran tactile, naviguez vers <b>[Maintenance]</b> -> <b>[Alignement de la tête d'impression]</b> -> <b>[Automatique]</b>.<br/>"
                       "3. L'appareil imprime des séries de motifs denses et lit automatiquement les densités optiques grâce à son capteur de bord et de couleur embarqué.<br/>"
                       "4. Les coefficients de compensation bidirectionnels sont recalculés et inscrits directement dans la mémoire de l'imprimante.", styles['body']))

    s.append(Paragraph("3. Alignement Manuel d'Atelier", styles['h1']))
    s.append(Paragraph("Pour une fidélité d'exposition maximale sur des tirages d'art, privilégiez le mode <b>Manuel</b> :<br/>"
                       "• Examinez les blocs numérotés imprimés sous une source d'éclairage normalisée 5000K (D50).<br/>"
                       "• Pour chaque rangée, identifiez le motif présentant le moins de rayures, le grain le plus uniforme et saisissez son numéro sur le pavé tactile.", styles['body']))

# -------------------------------------------------------------
# 7. DOC_EPSON_08_Resolution_Bourrages_Papier.pdf
# -------------------------------------------------------------
def epson_08_story(s):
    s.append(Paragraph("1. Zones Fréquentes d'Engorgement Papier", styles['h1']))
    s.append(Paragraph("En cas d'arrêt machine avec le code d'erreur <b>000100</b>, le support papier est immobilisé dans l'un des trois points critiques suivants :", styles['body']))
    s.append(Paragraph("• <b>Zone A : Bac arrière supérieur :</b> Feuille engagée de travers ou coincée par les patins de retenue.<br/>"
                       "• <b>Zone B : Platine d'impression sous le chariot :</b> Froissement de la tête de page lors de l'aspiration à vide.<br/>"
                       "• <b>Zone C : Fente Fine Art manuelle avant :</b> Bourrage sur média rigide non dégagé.", styles['body']))

    s.append(Paragraph("2. Procédure de Retrait Sécurisé sans Détériorer la Tête", styles['h1']))
    s.append(Paragraph("1. Mettez l'imprimante hors tension et ouvrez le capot supérieur transparent.<br/>"
                       "2. Si le papier est coincé sous le chariot, ne forcez jamais sur le chariot d'impression manuellement s'il est verrouillé dans la station de repos.<br/>"
                       "3. Saisissez délicatement la feuille bloquée des deux mains par les bords latéraux et tirez lentement vers vous dans le sens naturel d'avance du papier.<br/>"
                       "4. Inspectez minutieusement la platine à la lampe torche pour vérifier qu'aucun débris ou fragment de fibre de papier ne subsiste près des galets d'entraînement.<br/>"
                       "5. Refermez tous les capots et remettez sous tension.", styles['body']))

    s.append(make_callout("N'utilisez jamais d'outils métalliques (brucelles, tournevis, cutter) à l'intérieur du mécanisme pour extraire un morceau de papier déchiré. Une rayure superficielle sur la surface de la tête ou la bande d'encodage transparente rend l'imprimante irréparable.", "danger", styles))

# -------------------------------------------------------------
# 8. DOC_EPSON_12_Calibration_Profils_Colorimetriques.pdf
# -------------------------------------------------------------
def epson_12_story(s):
    s.append(Paragraph("1. Gestion des Profils Colorimétriques ICC", styles['h1']))
    s.append(Paragraph("L'Epson SureColor SC-P700 requiert des profils de couleur ICC (International Color Consortium) adaptés à chaque couple 'Encre UltraChrome PRO10 / Type de Papier' pour garantir une restitution conforme et une neutralité des gris parfaite.", styles['body']))

    s.append(Paragraph("2. Installation et Affectation dans le Logiciel Epson Print Layout", styles['h1']))
    s.append(Paragraph("1. Téléchargez le profil ICC spécifique fourni par le fabricant du papier (Canson Infinity, Hahnemühle, Ilford, Epson Signature Worthy).<br/>"
                       "2. Sous Windows, effectuez un clic droit sur le fichier <b>.icc / .icm</b> et sélectionnez <b>Installer le profil</b> (chemin système : <code>C:\\Windows\\System32\\spool\\drivers\\color</code>).<br/>"
                       "3. Ouvrez l'application <b>Epson Print Layout</b>.<br/>"
                       "4. Dans le panneau de droite, sélectionnez le support papier approprié (ex: <i>Velvet Fine Art Paper</i>), choisissez le mode de rendu (Perceptif ou Colorimétrie relative) et activez la compensation du point noir.<br/>"
                       "5. Pour les tirages noir et blanc d'art, activez le mode <b>ABW (Advanced Black and White)</b> pour désactiver la gestion des couleurs par le système d'exploitation et piloter directement les 4 noirs et gris.", styles['body']))

    s.append(Paragraph("3. Mode Black Enhance Overcoat", styles['h1']))
    s.append(Paragraph("L'option Black Enhance Overcoat applique une couche microscopique d'encre Light Gray sur les zones sombres des tirages brillants et lustrés afin de lisser l'état de surface, éliminer le phénomène de bronzing et accroître la densité maximale de noir optique (Dmax supérieure à 2.85).", styles['body']))

def generate_all_epson_pdfs():
    print("Génération des 8 PDF Epson SureColor P700...")
    build_pdf("DOC_EPSON_01_Guide_Utilisateur_General.pdf", "Guide Utilisateur Général", "DOC-EPS-001", epson_01_story)
    build_pdf("DOC_EPSON_02_Remplacement_Boitier_Maintenance_C12C935711.pdf", "Procédure Remplacement Boîtier Maintenance C12C935711", "DOC-EPS-002", epson_02_story)
    build_pdf("DOC_EPSON_03_Table_Codes_Erreurs_Solutions.pdf", "Tableau Exhaustif des Codes d'Erreurs SC-P700", "DOC-EPS-003", epson_03_story)
    build_pdf("DOC_EPSON_04_Guide_Maintenance_Tete_Standard.pdf", "Protocole Officiel Entretien Tête d'Impression", "DOC-EPS-004", epson_04_story)
    build_pdf("DOC_EPSON_06_Gestion_Cartouches_Encre_UltraChrome_PRO10.pdf", "Gestion des Cartouches d'Encre T46S UltraChrome PRO10", "DOC-EPS-006", epson_06_story)
    build_pdf("DOC_EPSON_07_Procedure_Alignement_Tete_Impression.pdf", "Procédure d'Alignement Tête d'Impression", "DOC-EPS-007", epson_07_story)
    build_pdf("DOC_EPSON_08_Resolution_Bourrages_Papier.pdf", "Résolution des Bourrages Papier", "DOC-EPS-008", epson_08_story)
    build_pdf("DOC_EPSON_12_Calibration_Profils_Colorimetriques.pdf", "Calibration & Profils Colorimétriques ICC", "DOC-EPS-012", epson_12_story)
    print("8 PDF Epson générés avec succès.")

if __name__ == "__main__":
    generate_all_epson_pdfs()
