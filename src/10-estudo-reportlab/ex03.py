from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

# Criação do arquivo PDF
pdf_file = "src/10-estudo-reportlab/example3.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Caminho da imagem
image_path = "src/10-estudo-reportlab/logo_reportlab.png"

# Obtendo os estilos de amostra
styles = getSampleStyleSheet()

# Conteúdo do documento
conteudo = []

# Imagem
image = Image(image_path)
conteudo.append(image)

# Título
titulo = "Título do Relatório"
titulo_texto = Paragraph(titulo, styles["Heading1"])
conteudo.append(titulo_texto)
conteudo.append(Spacer(1, 20))  # Espaçamento de 20pt

# Parágrafo
paragrafo = "Este é um parágrafo de exemplo."
paragrafo_texto = Paragraph(paragrafo, styles["BodyText"])
conteudo.append(paragrafo_texto)
conteudo.append(Spacer(1, 15))  # Espaçamento de 15pt

# Tabela
dados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    ["Dado 1", "Dado 2", "Dado 3", "Dado 4"]
]
tabela = Table(dados)
conteudo.append(tabela)

# Construção do PDF
doc.build(conteudo)