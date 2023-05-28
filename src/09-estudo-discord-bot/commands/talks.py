from discord.ext import commands
from discord import app_commands
import discord
MY_GUILD = discord.Object(id=1111398730822844478)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class Talks(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="oi", description="Envia um Oi(Não requer argumento)")
    async def send_hello(self, interaction: discord.Interaction):
        name = interaction.user.name
        response = "Olá, " + name
        await interaction.response.send_message(response)

    @commands.command(name="segredo", help="Envia um segredo no privado.Não requer argumento")
    async def secret(self, ctx):
        try:
            await interaction.user.dm_channel.send("Banana!")
        except discord.errors.Forbidden:
            await interaction.response.send_message("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")


async def setup(bot):
    await bot.add_cog(Talks(bot), guilds=[MY_GUILD])
