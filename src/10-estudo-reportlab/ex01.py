from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import blue, red

# Criando o arquivo PDF
pdf_file = "src/10-estudo-reportlab/example.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

# Definindo a string "Hello World"
text = "Hello World!"

# Definindo o tamanho da página
width, height = letter

# Escrevendo a string "Hello World" no centro da página
c.setFont("Helvetica", 12)
text_width = c.stringWidth(text, "Helvetica", 12)
text_height = 12
c.drawString((width - text_width) / 2, (height - text_height) / 2, text)

# Desenhando algumas formas geométricas
c.setStrokeColor(blue)
c.setFillColor(red)

# Retângulo
c.rect(2 * inch, 2 * inch, 3 * inch, 2 * inch, fill=True)

# Círculo
c.ellipse(5 * inch, 3 * inch, 6 * inch, 4 * inch, fill=True)

# Linha diagonal
c.setStrokeColor(blue)
c.setLineWidth(2)
c.line(1 * inch, 1 * inch, 7 * inch, 5 * inch)

# Salvando o arquivo PDF
c.showPage()
c.save()

print(f"PDF criado com sucesso: {pdf_file}")