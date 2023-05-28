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
    async def list_students(self, interaction: discord.Interaction):
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


async def setup(bot):
    await bot.add_cog(List(bot), guilds=[MY_GUILD])
