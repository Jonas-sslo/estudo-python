from discord.ext import commands
from discord import app_commands
import discord
import requests
MY_GUILD = discord.Object(id=1111398730822844478)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class Crypto(commands.Cog):
    """ Work with CryptoCurrency """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Verifica o preço de um par na binance. Argumentos: moeda, base")
    async def binance(self, interaction: discord.Interaction, coin: str, base: str):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")

            if price:
                await interaction.response.send_message(f"O valor do par {coin}/{base} é {price}")
            else:
                await interaction.response.send_message(f"O valor do par {coin}/{base} é inválido")
        except Exception as error:
            await interaction.response.send_message("Ops... Deu algum erro!")
            print(error)


async def setup(bot):
    await bot.add_cog(Crypto(bot), guilds=[MY_GUILD])
