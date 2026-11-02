"""
Génération des 8 documents PDF pour la Famille 1 : Canon EOS R50.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from pdf_builder_utils import NumberedCanvas, get_doc_styles, make_callout

OUTPUT_DIR = os.path.join("L1_MaintiDoc_TeamName_Corpus", "documents", "famille_1")
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
    
    # Custom canvas wrapper pour injecter title et ref
    class DocNumberedCanvas(NumberedCanvas):
        doc_title = f"Canon EOS R50 - {title}"
        doc_ref = ref

    story = []
    # Titre & En-tête
    story.append(Paragraph(title, styles['title']))
    story.append(Paragraph(f"<b>Référence :</b> {ref} | <b>Appareil :</b> Canon EOS R50 | <b>Statut :</b> Documentation Officielle Fabricant", styles['subtitle']))
    story.append(Spacer(1, 10))
    
    story_func(story)
    doc.build(story, canvasmaker=DocNumberedCanvas)
    print(f"PDF généré : {path}")

# -------------------------------------------------------------
# 1. DOC_CANON_01_Manuel_Utilisateur_Base.pdf
# -------------------------------------------------------------
def canon_01_story(s):
    s.append(Paragraph("1. Présentation Générale et Prise en Main", styles['h1']))
    s.append(Paragraph("Le Canon EOS R50 est un boîtier hybride compact à objectifs interchangeables doté de la monture Canon RF. Il intègre un capteur CMOS APS-C haute définition de 24.2 mégapixels et le moteur de traitement d'image DIGIC X, optimisé pour les créateurs de contenu et les applications de prise de vue techniques.", styles['body']))
    
    s.append(Paragraph("2. Ergonomie et Commandes Opérateur", styles['h1']))
    s.append(Paragraph("La disposition des commandes a été pensée pour un accès intuitif et rapide à l'ensemble des réglages de prise de vue :", styles['body']))
    s.append(Paragraph("• <b>Sélecteur de mode de prise de vue :</b> Permet de commuter entre la Zone de Base (Scène Intelligente Auto, Filtres Créatifs, Scènes Spéciales SCN) et la Zone Créative (P : Programme d'exposition automatique, Tv : Priorité à la vitesse, Av : Priorité à l'ouverture, M : Exposition manuelle).", styles['body']))
    s.append(Paragraph("• <b>Molette principale :</b> Positionnée à proximité du déclencheur, elle contrôle directement l'ouverture, la vitesse ou la navigation dans les menus.", styles['body']))
    s.append(Paragraph("• <b>Écran LCD tactile Clear View II :</b> Moniteur de 3.0 pouces (7.5 cm) orientable sur rotule à environ 1.62 million de points.", styles['body']))
    s.append(Paragraph("• <b>Viseur électronique (EVF) :</b> Viseur OLED 0.39 pouce d'environ 2.36 millions de points avec capteur oculaire automatique.", styles['body']))
    
    s.append(make_callout("Pour préserver l'autonomie de la batterie LP-E17, l'affichage bascule automatiquement entre l'écran LCD et le viseur EVF grâce au capteur oculaire situé sous l'œilleton. Veillez à maintenir cette zone exempte de poussière.", "note", styles))
    s.append(Spacer(1, 12))

    s.append(Paragraph("3. Insertion de la Batterie et de la Carte Mémoire", styles['h1']))
    s.append(Paragraph("1. Assurez-vous que l'interrupteur d'alimentation est placé sur la position <b>OFF</b>.<br/>"
                       "2. Faites glisser le loquet d'ouverture du compartiment situé sur la semelle inférieure du boîtier.<br/>"
                       "3. Insérez la batterie rechargeable <b>Canon LP-E17</b> dans le sens indiqué par les flanches jusqu'au déclic du verrou plastique orange.<br/>"
                       "4. Insérez la carte mémoire <b>SD / SDHC / SDXC</b> (compatible bus UHS-I classe de vitesse U3 / V30 recommandée) contacts orientés vers l'écran LCD jusqu'au verrouillage.<br/>"
                       "5. Refermez le couvercle de la trappe et faites coulisser le verrou de sécurité.", styles['body']))
    
    s.append(PageBreak())
    s.append(Paragraph("4. Montage et Démontage des Objectifs RF / RF-S", styles['h1']))
    s.append(Paragraph("L'EOS R50 accepte nativement tous les objectifs Canon RF et RF-S. Les objectifs des gammes antérieures EF et EF-S peuvent être utilisés via la bague d'adaptation pour monture EF-EOS R optionnelle.", styles['body']))
    s.append(Paragraph("• <b>Repères de montage :</b> Alignez le repère blanc (objectifs RF-S) ou le repère rouge (objectifs RF) avec le repère correspondant sur le châssis de la monture.<br/>"
                       "• <b>Verrouillage :</b> Tournez l'objectif dans le sens des aiguilles d'une montre jusqu'au clic mécanique d'enclenchement.<br/>"
                       "• <b>Démontage :</b> Maintenez enfoncé le bouton de déverrouillage de l'objectif sur le boîtier et tournez l'optique dans le sens inverse des aiguilles d'une montre.", styles['body']))

    s.append(make_callout("Ne laissez jamais la chambre réflexe ouverte sans bouchon de boîtier ou objectif monté. Lors du changement d'optique en milieu poussiéreux, orientez l'appareil vers le bas pour minimiser l'intrusion de particules sur le capteur.", "warning", styles))
    s.append(Spacer(1, 12))

    s.append(Paragraph("5. Spécifications Synthétiques de Base", styles['h1']))
    data = [
        [Paragraph("<b>Composant / Fonction</b>", styles['header']), Paragraph("<b>Caractéristique Technique</b>", styles['header'])],
        [Paragraph("Monture d'objectif", styles['cell']), Paragraph("Canon RF (compatibilité RF et RF-S)", styles['cell'])],
        [Paragraph("Capteur d'image", styles['cell']), Paragraph("CMOS APS-C (22.3 x 14.9 mm) - 24.2 MP effectifs", styles['cell'])],
        [Paragraph("Moteur de traitement", styles['cell']), Paragraph("Canon DIGIC X", styles['cell'])],
        [Paragraph("Sensibilité ISO", styles['cell']), Paragraph("100 à 32 000 (extension possible à ISO 51 200)", styles['cell'])],
        [Paragraph("Vitesse d'obturation", styles['cell']), Paragraph("1/4000 s à 30 s (mécanique/EFCS), jusqu'à 1/8000 s (électronique)", styles['cell'])],
        [Paragraph("Support de stockage", styles['cell']), Paragraph("1 emplacement carte SD/SDHC/SDXC (UHS-I)", styles['cell'])],
        [Paragraph("Alimentation électrique", styles['cell']), Paragraph("Batterie Li-ion LP-E17 (Autonomie CIPA ~370 vues)", styles['cell'])],
        [Paragraph("Poids (boîtier seul)", styles['cell']), Paragraph("Environ 328 g (boîtier nu sans batterie ni carte)", styles['cell'])],
    ]
    t = Table(data, colWidths=[180, A4[0] - 80 - 180])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#004080")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8f9fa")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    s.append(t)

# -------------------------------------------------------------
# 2. DOC_CANON_02_Guide_Avance_Prise_Vue.pdf
# -------------------------------------------------------------
def canon_02_story(s):
    s.append(Paragraph("1. Système Autofocus Dual Pixel CMOS AF II", styles['h1']))
    s.append(Paragraph("L'EOS R50 bénéficie du système autofocus à corrélation de phase Dual Pixel CMOS AF II, couvrant jusqu'à 100% de la surface de cadrage en sélection automatique. L'appareil intègre des algorithmes d'apprentissage profond (Deep Learning) pour la détection et le suivi précis des sujets (personnes, animaux, véhicules).", styles['body']))
    
    s.append(Paragraph("2. Modes de Fonctionnement Autofocus", styles['h1']))
    s.append(Paragraph("• <b>One-Shot AF :</b> Conçu pour les sujets immobiles. La mise au point se verrouille dès que le déclencheur est enfoncé à mi-course. L'indicateur de confirmation AF vert s'allume fixement.<br/>"
                       "• <b>Servo AF :</b> Indispensable pour les sujets en mouvement. L'appareil ajuste en continu la distance de mise au point tant que le déclencheur est à mi-course.<br/>"
                       "• <b>AF avec suivi du sujet :</b> L'EOS R50 verrouille le collimateur sur le visage, l'œil ou le corps du sujet sélectionné et conserve le focus même lors de déplacements rapides dans le cadre.", styles['body']))

    s.append(Paragraph("3. Gestion de l'Obturation : EFCS vs Obturateur Électronique", styles['h1']))
    s.append(Paragraph("L'EOS R50 propose deux technologies d'obturation distinctes :", styles['body']))
    s.append(Paragraph("1. <b>Premier rideau électronique (EFCS) :</b> Combine un démarrage d'exposition électronique et une fin d'exposition mécanique. Réduit fortement les vibrations internes tout en garantissant une synchronisation flash au 1/250 s.<br/>"
                       "2. <b>Obturateur électronique silencieux :</b> L'exposition démarre et s'arrête intégralement par commutation électronique des photodiodes. Permet une cadence en rafale jusqu'à 15 images/seconde en silence absolu, mais peut engendrer des distorsions de type 'rolling shutter' sur des sujets en mouvement ultra-rapide.", styles['body']))

    s.append(PageBreak())
    s.append(Paragraph("4. Enregistrement Vidéo 4K et Profils de Couleur", styles['h1']))
    s.append(Paragraph("L'EOS R50 capture des flux vidéo 4K UHD à 29.97/25.00/23.98 images/s suréchantillonnés depuis un signal pleine largeur de 6K, garantissant une netteté remarquable sans recadrage. En Full HD, les cadences s'étendent jusqu'à 119.9/100 images/s pour des ralentis fluides.", styles['body']))
    
    s.append(make_callout("Pour enregistrer en 4K sans interruption de flux ou erreur d'écriture tampon (Buffer Full), utilisez exclusivement des cartes SDXC certifiées UHS-I Classe de vitesse vidéo V30 ou supérieure.", "warning", styles))
    s.append(Spacer(1, 12))

    s.append(Paragraph("5. Recommandations de Paramétrage pour Travaux Techniques", styles['h1']))
    s.append(Paragraph("Dans le cadre d'inspections de maintenance ou de captures macrographiques :<br/>"
                       "• Désactiver la réduction de bruit haute sensibilité pour préserver le micro-détail des textures mécaniques.<br/>"
                       "• Utiliser le mode d'accentuation des contours en mise au point manuelle (Focus Peaking) pour visualiser avec exactitude le plan de netteté.<br/>"
                       "• Sélectionner l'espace colorimétrique <b>sRGB</b> pour une compatibilité directe avec les protocoles d'imagerie documentaire.", styles['body']))

# -------------------------------------------------------------
# 3. DOC_CANON_03_Table_Codes_Erreurs_Depannage.pdf
# -------------------------------------------------------------
def canon_03_story(s):
    s.append(Paragraph("1. Diagnostic des Anomalies Système (Codes Err xx)", styles['h1']))
    s.append(Paragraph("Lorsqu'un dysfonctionnement matériel ou logique est détecté par le processeur DIGIC X, l'appareil interrompt les opérations de prise de vue et affiche un code d'erreur sur l'écran LCD de type <b>Err [XX]</b>. Le tableau ci-dessous détaille la cause probable et les actions correctives recommandées.", styles['body']))
    
    data = [
        [Paragraph("<b>Code</b>", styles['header']), Paragraph("<b>Désignation</b>", styles['header']), Paragraph("<b>Cause Probable</b>", styles['header']), Paragraph("<b>Procédure de Résolution Recommandée</b>", styles['header'])],
        [
            Paragraph("<b>Err 01</b>", styles['cell']),
            Paragraph("Communication objectif défaillante", styles['cell']),
            Paragraph("Oxydation ou salissure sur les 12 plots de contact de la monture RF.", styles['cell']),
            Paragraph("1. Éteindre l'appareil.<br/>2. Démonter l'objectif et nettoyer les contacts or au chiffon sec doux.<br/>3. Réinstaller l'objectif.", styles['cell'])
        ],
        [
            Paragraph("<b>Err 02</b>", styles['cell']),
            Paragraph("Accès carte mémoire impossible", styles['cell']),
            Paragraph("Corruption du système de fichiers ou secteur défectueux sur la carte SD.", styles['cell']),
            Paragraph("1. Éjecter et réinsérer la carte.<br/>2. Sauvegarder les images sur PC.<br/>3. Exécuter un formatage bas niveau dans l'appareil.", styles['cell'])
        ],
        [
            Paragraph("<b>Err 04</b>", styles['cell']),
            Paragraph("Capacité carte mémoire épuisée", styles['cell']),
            Paragraph("L'espace libre sur la carte SD est insuffisant pour enregistrer les données.", styles['cell']),
            Paragraph("Remplacer la carte mémoire par une carte vide ou supprimer des fichiers inutiles.", styles['cell'])
        ],
        [
            Paragraph("<b>Err 05</b>", styles['cell']),
            Paragraph("Obstruction flash intégré", styles['cell']),
            Paragraph("Le flash escamotable automatique a été retenu lors de son déploiement.", styles['cell']),
            Paragraph("Éteindre l'appareil, libérer l'espace au-dessus du flash et rallumer l'appareil.", styles['cell'])
        ],
        [
            Paragraph("<b>Err 06</b>", styles['cell']),
            Paragraph("Erreur unité de nettoyage capteur", styles['cell']),
            Paragraph("Blocage mécanique du mécanisme piézo-électrique auto-nettoyant.", styles['cell']),
            Paragraph("Couper l'alimentation, extraire la batterie pendant 1 minute, puis redémarrer.", styles['cell'])
        ],
        [
            Paragraph("<b>Err 70</b>", styles['cell']),
            Paragraph("Erreur de traitement des images", styles['cell']),
            Paragraph("Incohérence du tampon mémoire interne du processeur DIGIC X.", styles['cell']),
            Paragraph("Couper l'alimentation, retirer la batterie et reformater la carte mémoire.", styles['cell'])
        ],
        [
            Paragraph("<b>Err 99</b>", styles['cell']),
            Paragraph("Erreur système non spécifique", styles['cell']),
            Paragraph("Anomalie d'alimentation électrique ou court-circuit de commande d'obturateur.", styles['cell']),
            Paragraph("Retirer batterie et objectif. Remonter avec composants vérifiés. Si persistance, retour atelier SAV Canon agréé.", styles['cell'])
        ],
    ]
    t = Table(data, colWidths=[55, 95, 140, A4[0] - 80 - 290])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#c62828")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#fff9f9")]),
        ('PADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    s.append(t)
    s.append(Spacer(1, 12))
    s.append(make_callout("Si un code d'erreur persiste systématiquement malgré l'application des procédures ci-dessus, notez le numéro du code et transmettez le boîtier à un centre technique certifié Canon.", "warning", styles))

# -------------------------------------------------------------
# 4. DOC_CANON_04_Guide_Nettoyage_Capteur_Officiel.pdf (CONTRADICTION 1)
# -------------------------------------------------------------
def canon_04_story(s):
    s.append(Paragraph("1. Système d'Auto-Nettoyage par Vibrations Ultrasoniques", styles['h1']))
    s.append(Paragraph("L'EOS R50 est pourvu d'une unité de capteur autonettoyante (Self-Cleaning Sensor Unit). À chaque mise sous tension (ON) ou hors tension (OFF), le filtre passe-bas fixé devant le capteur CMOS vibre par excitation ultrasonique pour détacher les microparticules de poussière sèche en suspension.", styles['body']))
    
    s.append(Paragraph("2. Protocole Officiel de Nettoyage Manuel du Capteur", styles['h1']))
    s.append(Paragraph("Si des particules adhérentes demeurent visibles sur les prises de vue à petite ouverture (f/11 - f/22), l'opérateur doit procéder à un nettoyage manuel selon la méthode certifiée Canon :", styles['body']))
    s.append(Paragraph("1. Installez une batterie <b>LP-E17 pleinement chargée</b> (capacité supérieure à 75% requise pour éviter toute fermeture inopinée de l'obturateur).<br/>"
                       "2. Retirez l'objectif et placez le boîtier sur une surface plane et propre en atmosphère exempte de courants d'air.<br/>"
                       "3. Positionnez le commutateur d'alimentation sur <b>ON</b>.<br/>"
                       "4. Accédez au menu : <b>[Clé / Configuration]</b> -> onglet <b>[4]</b> -> sélectionnez <b>[Nettoyage du capteur]</b> -> <b>[Nettoyer manuellement]</b>.<br/>"
                       "5. Confirmez par <b>[OK]</b>. Le rideau mécanique d'obturateur se rétracte et découvre le capteur CMOS.<br/>"
                       "6. À l'aide d'une <b>poire soufflante manuelle en caoutchouc</b> (sans brosse ni poils synthétiques), insérez l'embout dans la cage reflex en maintenant une <b>distance minimale de sécurité de 15 mm</b> avec la surface du filtre.<br/>"
                       "7. Soufflez par pressions fermes et courtes tout en maintenant le boîtier orienté vers le bas pour faciliter l'évacuation des particules.<br/>"
                       "8. Positionnez l'interrupteur sur <b>OFF</b> pour terminer le cycle de nettoyage et refermer l'obturateur.", styles['body']))

    s.append(PageBreak())
    s.append(Paragraph("3. Interdictions Strictes et Consignes de Sécurité Constructeur", styles['h1']))
    
    s.append(make_callout("INTERDICTION ABSOLUE DE SOLVANTS LIQUIDES :<br/>"
                          "Canon interdit formellement l'utilisation de tout solvant chimique liquide (alcool isopropylique, méthanol, sprays pour optiques, nettoyants pour capteurs tiers) ainsi que l'usage de cotons-tiges ou de bâtonnets de contact.<br/>"
                          "La surface extérieure du capteur comporte un traitement de surface dichroïque et un filtre infrarouge ultra-mince qui subit une détérioration irréversible au contact de solvants ou sous l'effet de frottements mécaniques.<br/>"
                          "L'utilisation de gaz comprimé en bombe aérosol est également strictement prohibée en raison du risque de projection de gaz propulseur liquide cryogénique.", "danger", styles))
    s.append(Spacer(1, 12))

    s.append(Paragraph("4. Périodicité et Intervalles de Maintenance Officiels", styles['h1']))
    s.append(Paragraph("Selon le cahier des charges de maintenance préventive Canon :<br/>"
                       "• <b>Nettoyage manuel à l'air sec :</b> Uniquement à la demande, en cas de taches visibles constatées lors du contrôle technique.<br/>"
                       "• <b>Contrôle et révision en atelier agréé :</b> Recommandé tous les <b>12 mois</b> ou tous les <b>10 000 déclenchements</b>.<br/>"
                       "• Tout nettoyage humide en profondeur nécessitant l'application de solvants doit obligatoirement être confié aux laboratoires spécialisés du Service Après-Vente Canon sous atmosphère contrôlée (salle blanche classe 1000).", styles['body']))

# -------------------------------------------------------------
# 5. DOC_CANON_06_Maintenance_Batterie_Alimentation.pdf
# -------------------------------------------------------------
def canon_06_story(s):
    s.append(Paragraph("1. Spécifications de la Batterie Canon LP-E17", styles['h1']))
    s.append(Paragraph("L'EOS R50 est alimenté exclusivement par le bloc batterie rechargeable Lithium-Ion d'origine Canon <b>LP-E17</b>. Les caractéristiques nominales sont : Tension : 7.2 V CC | Capacité : 1040 mAh | Énergie : 7.5 Wh.", styles['body']))
    
    s.append(Paragraph("2. Modalités de Recharge et Chargeur USB-PD", styles['h1']))
    s.append(Paragraph("L'EOS R50 prend en charge la recharge directe de la batterie à l'intérieur du boîtier via son port USB Type-C, sous réserve d'utiliser une source d'alimentation conforme à la norme <b>USB Power Delivery (USB-PD)</b> de tension nominale 9V/3A ou l'adaptateur secteur d'origine <b>Canon PD-E1</b>.<br/>"
                       "• Les chargeurs USB conventionnels de téléphones portables délivrant 5V standard ne permettent pas la charge dans le boîtier.<br/>"
                       "• Le témoin LED de charge vert s'allume fixement pendant le cycle et s'éteint dès que l'accumulateur atteint 100% de charge.", styles['body']))

    s.append(Paragraph("3. Règles d'Entretien et Stockage Prolongé", styles['h1']))
    s.append(Paragraph("Pour maximiser la longévité chimique des cellules lithium-ion :<br/>"
                       "• En cas de stockage inactif supérieur à 30 jours, déchargez la batterie à environ <b>40-50% de sa capacité</b>.<br/>"
                       "• Stockez l'accumulateur dans un endroit sec, à l'abri de la lumière solaire directe, à une température comprise entre 10°C et 25°C.<br/>"
                       "• Ne conservez jamais une batterie insérée dans un boîtier inutilisé pendant plusieurs mois, au risque d'une décharge profonde irréversible des éléments.", styles['body']))
    
    s.append(make_callout("N'exposez jamais la batterie LP-E17 à des températures supérieures à 60°C ou à des flammes directes. Tout renflement ou déformation physique impose la mise au rebut immédiate de l'accumulateur dans un point de collecte agréé pour matières dangereuses.", "warning", styles))

# -------------------------------------------------------------
# 6. DOC_CANON_07_Procedure_Mise_A_Jour_Firmware.pdf
# -------------------------------------------------------------
def canon_07_story(s):
    s.append(Paragraph("1. Prérequis et Contrôles Préliminaires", styles['h1']))
    s.append(Paragraph("La mise à jour du micrologiciel (firmware) améliore la stabilité du système, résout les anomalies de communication d'objectifs (Err 01) et optimise la mise au point AF. Avant d'engager la procédure :<br/>"
                       "1. Vérifiez que la batterie LP-E17 est chargée à <b>100%</b> (l'appareil refuse d'initier la mise à jour si la charge est inférieure à 50%).<br/>"
                       "2. Munissez-vous d'une carte SD formatée au préalable dans le boîtier EOS R50.<br/>"
                       "3. Téléchargez le fichier de firmware certifié (extension <b>.FIR</b>) sur le portail d'assistance officiel Canon.", styles['body']))

    s.append(Paragraph("2. Procédure Pas à Pas de Flashage", styles['h1']))
    s.append(Paragraph("1. Copiez le fichier décompressé (ex: <i>EOSR50_120.FIR</i>) à la racine de la carte SD.<br/>"
                       "2. Insérez la carte mémoire dans le boîtier éteint.<br/>"
                       "3. Positionnez le commutateur d'alimentation sur <b>ON</b> et réglez la molette de mode sur <b>P</b>.<br/>"
                       "4. Appuyez sur la touche <b>MENU</b>, naviguez jusqu'à l'onglet de configuration <b>[Clé / 5]</b> et sélectionnez la ligne <b>[Version firmware]</b>.<br/>"
                       "5. L'écran affiche la version actuelle et la nouvelle version détectée. Validez en sélectionnant <b>[OK]</b>.<br/>"
                       "6. La barre de progression s'affiche. Le processus dure environ 4 à 6 minutes.", styles['body']))

    s.append(make_callout("CRITIQUE : Ne coupez JAMAIS l'alimentation, ne manipulez aucun bouton et n'ouvrez jamais la trappe de la batterie pendant l'écriture du firmware. Une coupure d'énergie corrompt la mémoire Flash EEPROM interne et rend le boîtier inopérant (briquage matériel irréversible nécessitant un retour SAV).", "danger", styles))

# -------------------------------------------------------------
# 7. DOC_CANON_08_Guide_Connectique_Ports_E_S.pdf
# -------------------------------------------------------------
def canon_08_story(s):
    s.append(Paragraph("1. Description des Interfaces Physiques de Communication", styles['h1']))
    s.append(Paragraph("Le flanc gauche de l'EOS R50 rassemble les connecteurs filaires protégés par des caches élastomères étanches à la poussière :", styles['body']))
    
    s.append(Paragraph("• <b>Port USB Type-C (Hi-Speed USB 2.0) :</b><br/>"
                       "- Vitesse de transfert théorique maximale : 480 Mbit/s.<br/>"
                       "- Prise en charge de la charge interne et de l'alimentation continue via protocole USB-PD.<br/>"
                       "- Support direct des protocoles UVC/UAC pour diffusion en webcam Full HD 1080p 30 fps sans pilote dédié.", styles['body']))
    
    s.append(Paragraph("• <b>Sortie vidéo Micro-HDMI (Connecteur Type D) :</b><br/>"
                       "- Délivre un signal vidéo numérique 4K ou FHD non compressé (Clean HDMI 4:2:2 8 bits / 10 bits).<br/>"
                       "- Permet le monitoring sur écran de contrôle externe ou l'enregistrement sur enregistreur externe (Atomos, Blackmagic).", styles['body']))

    s.append(Paragraph("• <b>Entrée Audio Microphone Externe (Prise Jack 3.5 mm stéréo) :</b><br/>"
                       "- Permet le raccordement de microphones électrets passifs ou auto-alimentés.<br/>"
                       "- Alimentation fantôme miniature (Plug-in Power 2.5V) fournie par l'appareil.<br/>"
                       "- <i>Note technique :</i> L'EOS R50 ne comporte pas de sortie casque jack 3.5 mm dédiée.", styles['body']))

    s.append(make_callout("Lors du raccordement des câbles USB-C ou Micro-HDMI, veillez à ne pas exercer de contrainte mécanique latérale sur les fiches afin d'éviter d'endommager les soudures de la carte mère principale.", "warning", styles))

# -------------------------------------------------------------
# 8. DOC_CANON_12_Fiche_Securite_Environnementale.pdf
# -------------------------------------------------------------
def canon_12_story(s):
    s.append(Paragraph("1. Plages de Fonctionnement et Tolérances Thermiques", styles['h1']))
    s.append(Paragraph("L'EOS R50 est conçu pour opérer dans les conditions environnementales suivantes :<br/>"
                       "• <b>Plage de température opérationnelle :</b> De <b>0°C à +40°C</b> (32°F à 104°F).<br/>"
                       "• <b>Taux d'humidité relative admissible :</b> <b>85% ou moins</b> (sans condensation).<br/>"
                       "• <b>Plage de température de stockage :</b> De -20°C à +60°C.", styles['body']))

    s.append(Paragraph("2. Prévention des Phénomènes de Condensation", styles['h1']))
    s.append(Paragraph("Lors du passage rapide d'un environnement froid extérieur vers un espace intérieur chaud et humide, des gouttelettes de condensation microscopiques se déposent sur les lentilles internes et sur les composants électroniques :", styles['body']))
    s.append(Paragraph("1. Placez systématiquement l'appareil et ses objectifs dans un sac hermétique zippé fermé avant de pénétrer dans le local chauffé.<br/>"
                       "2. Laissez le sac s'acclimater à la température ambiante pendant environ <b>1 à 2 heures</b> avant d'en extraire le matériel.<br/>"
                       "3. En cas de buée constatée à l'intérieur de l'œilleton ou du capteur, éteignez immédiatement l'appareil et laissez-le sécher dans une pièce ventilée sans appliquer d'air chaud pulsé (sèche-cheveux proscrit).", styles['body']))

    s.append(Paragraph("3. Règlementation Transport Aérien (Batteries Lithium-Ion UN 3481)", styles['h1']))
    s.append(Paragraph("Conformément aux instructions techniques de l'OACI et aux réglementations IATA pour le transport de batteries rechargeables au lithium :<br/>"
                       "• Les batteries LP-E17 de rechange doivent impérativement être transportées dans le <b>bagage en cabine</b> et protégées individuellement contre les courts-circuits.<br/>"
                       "• Il est strictement interdit d'expédier des batteries lithium-ion isolées non installées dans les bagages enregistrés en soute.", styles['body']))

def generate_all_canon_pdfs():
    print("Génération des 8 PDF Canon EOS R50...")
    build_pdf("DOC_CANON_01_Manuel_Utilisateur_Base.pdf", "Manuel Utilisateur de Base", "DOC-CAN-001", canon_01_story)
    build_pdf("DOC_CANON_02_Guide_Avance_Prise_Vue.pdf", "Guide Avancé Prise de Vue & AF", "DOC-CAN-002", canon_02_story)
    build_pdf("DOC_CANON_03_Table_Codes_Erreurs_Depannage.pdf", "Tableau Exhaustif des Codes d'Erreurs", "DOC-CAN-003", canon_03_story)
    build_pdf("DOC_CANON_04_Guide_Nettoyage_Capteur_Officiel.pdf", "Guide Officiel Nettoyage Capteur CMOS", "DOC-CAN-004", canon_04_story)
    build_pdf("DOC_CANON_06_Maintenance_Batterie_Alimentation.pdf", "Maintenance Batterie LP-E17 & Alimentation", "DOC-CAN-006", canon_06_story)
    build_pdf("DOC_CANON_07_Procedure_Mise_A_Jour_Firmware.pdf", "Procédure de Mise à Jour Firmware", "DOC-CAN-007", canon_07_story)
    build_pdf("DOC_CANON_08_Guide_Connectique_Ports_E_S.pdf", "Guide Technique Connectique & Ports E/S", "DOC-CAN-008", canon_08_story)
    build_pdf("DOC_CANON_12_Fiche_Securite_Environnementale.pdf", "Fiche de Sécurité et Conditions Environnementales", "DOC-CAN-012", canon_12_story)
    print("8 PDF Canon générés avec succès.")

if __name__ == "__main__":
    generate_all_canon_pdfs()
