from discord.ext import commands
from discord import app_commands
import discord
MY_GUILD = discord.Object(id = 1111398730822844478)

intents = discord.Intents.default()
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)


class Smarts(commands.Cog):
    """ A lot of Smart commands """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="calcular", description="Calcula uma expressão. Argumentos: Expressão")
    async def calculate_expression(self, interaction: discord.Interaction, expression:str):
        expression = "".join(expression)
        # print(expression)
        response = eval(expression)
        await interaction.response.send_message("A resposta é: " + str(response))


async def setup(bot):
    await bot.add_cog(Smarts(bot), guilds = [MY_GUILD])
