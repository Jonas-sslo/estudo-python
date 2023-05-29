from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from discord.ext import commands
from discord import app_commands
import discord
MY_GUILD = discord.Object(id=1111398730822844478)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class List(commands.Cog):
    """ List students"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="listar-alunos")
    async def list_students_embed(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Resultado da busca de alunos cadastrados",
            description="Apenas alunos cadastrados",
            color=0x0000FF
        )

        embed.add_field(name="Alunos", value="")

        with open("src/09-estudo-discord-bot/commands/alunos.txt", "r", encoding="UTF-8") as arquivo:
            for linha in arquivo.readlines():
                dado = linha.strip().split(",")
                embed.add_field(name=f"{dado[1]}", value=f"Prontuário: {dado[0]} e Email: {dado[2]}")

        embed.set_author(name=self.bot.user.name,icon_url=self.bot.user.avatar)
        embed.set_footer(text="Feito por " + self.bot.user.name,icon_url=self.bot.user.avatar)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="listar-alunos-pdf")
    async def list_students_pdf(self, interaction: discord.Interaction):
        pdf_file = "src/09-estudo-discord-bot/alunos_cadastrados.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)

        styles = getSampleStyleSheet()

        conteudo = []

        titulo_texto = "Alunos Cadastrados"
        titulo = Paragraph(titulo_texto, styles["Heading1"])
        conteudo.append(titulo)
        conteudo.append(Spacer(1, 15))

        # Tabela
        dados = [["Prontuário", "Nome", "Email"]]
        with open("src/09-estudo-discord-bot/commands/alunos.txt", "r", encoding="UTF-8") as arquivo:
            for linha in arquivo.readlines():
                dado = linha.strip().split(",")
                dados.append([dado[0], dado[1], dado[2]])

        tabela = Table(dados)
        tabela_style = [
            ("BACKGROUND", (0, 0), (2, 0), colors.black),
            ("TEXTCOLOR", (0, 0), (2, 0), colors.white),
            ("FONTSIZE", (0, 0), (-1, -1), 12),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER")
        ]

        tabela.setStyle(tabela_style)

        conteudo.append(tabela)
        conteudo.append(Spacer(1, 15))

        paragrafo_texto = f"Total de alunos: {len(dados) - 1}"
        paragrafo = Paragraph(paragrafo_texto, styles["BodyText"])
        conteudo.append(paragrafo)

        doc.build(conteudo)
        await interaction.response.send_message(file=discord.File("src/09-estudo-discord-bot/alunos_cadastrados.pdf", "alunos_cadastrados.pdf"))

async def setup(bot):
    await bot.add_cog(List(bot), guilds=[MY_GUILD])
