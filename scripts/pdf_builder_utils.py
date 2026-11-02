"""
Utilitaires de mise en page ReportLab pour les documents MaintiDoc.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        
        # En-tête (à partir de la page 1)
        self.setStrokeColor(colors.HexColor("#dddddd"))
        self.setLineWidth(0.5)
        self.line(40, A4[1] - 40, A4[0] - 40, A4[1] - 40)
        self.drawString(42, A4[1] - 35, getattr(self, 'doc_title', 'MaintiDoc - Corpus Technique'))
        self.drawRightString(A4[0] - 42, A4[1] - 35, getattr(self, 'doc_ref', 'RÉF-TECH-2026'))
        
        # Pied de page
        self.line(40, 45, A4[0] - 40, 45)
        page_str = f"Page {self._pageNumber} sur {total_pages}"
        self.drawRightString(A4[0] - 42, 32, page_str)
        self.drawString(42, 32, "MaintiDoc Assistant Multimodal - Usage Technique & Maintenance Agréée")
        self.restoreState()

def get_doc_styles():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0d233a"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#555555"),
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#004080"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#222222"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#222222"),
        spaceAfter=6
    )
    
    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#2b2b2b")
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#111111")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'h1': h1_style,
        'h2': h2_style,
        'body': body_style,
        'callout': callout_style,
        'cell': table_cell,
        'header': table_header
    }

def make_callout(text, kind="note", styles=None):
    if styles is None:
        styles = get_doc_styles()
    
    bg = colors.HexColor("#f0f7ff")
    border = colors.HexColor("#0066cc")
    prefix = "<b>NOTE TECHNIQUE :</b> "
    
    if kind == "warning":
        bg = colors.HexColor("#fff8e1")
        border = colors.HexColor("#f57f17")
        prefix = "<b>ATTENTION :</b> "
    elif kind == "danger":
        bg = colors.HexColor("#ffebee")
        border = colors.HexColor("#c62828")
        prefix = "<b>AVERTISSEMENT DE SÉCURITÉ :</b> "
    elif kind == "contradiction":
        bg = colors.HexColor("#fbe9e7")
        border = colors.HexColor("#d84315")
        prefix = "<b>NORME CONSTRUCTEUR OFFICIELLE :</b> "
        
    p = Paragraph(f"{prefix}{text}", styles['callout'])
    t = Table([[p]], colWidths=[A4[0] - 80])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('BOX', (0,0), (-1,-1), 1.2, border),
        ('PADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
    ]))
    return t
