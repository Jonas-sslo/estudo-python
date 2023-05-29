from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Criando o arquivo PDF
pdf_file = "src/10-estudo-reportlab/example2.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Obtendo estilos de exemplo
styles = getSampleStyleSheet()

# Definindo estilos para os elementos
title_style = styles["Title"]
title_style.fontSize = 16

paragraph_style = styles["Normal"]
paragraph_style.fontSize = 12

# Criando uma lista de elementos do fluxo
flowables = []

# Adicionando o título
title_text = "Título do Documento"
title = Paragraph(title_text, title_style)
flowables.append(title)

# Adicionando espaçamento após o título
flowables.append(Spacer(1, 20))  # 1 inch = 72pt

# Adicionando o primeiro parágrafo
paragraph1_text = "Este é o primeiro parágrafo."
paragraph1 = Paragraph(paragraph1_text, paragraph_style)
flowables.append(paragraph1)

# Adicionando espaçamento entre os parágrafos
flowables.append(Spacer(1, 15))  # 1 inch = 72pt

# Adicionando o segundo parágrafo
paragraph2_text = "Este é o primeiro parágrafo."
paragraph2 = Paragraph(paragraph2_text, paragraph_style)
flowables.append(paragraph2)

# Adicionando espaçamento entre os parágrafos
flowables.append(Spacer(1, 15))  # 1 inch = 72pt

# Definindo o estilo do terceiro parágrafo
paragraph3_style = ParagraphStyle(
    name="paragraph3",
    fontSize=16,
    alignment=4,  # 4 para alinhar à esquerda
    leading=14,  # Espaçamento entre linhas
)

# Parágrafo com a classe ParagraphStyle
paragraph3_text = "Este é o terceiro parágrafo."
paragraph3 = Paragraph(paragraph3_text, paragraph3_style)
flowables.append(paragraph3)

# Construindo o documento PDF
doc.build(flowables)
