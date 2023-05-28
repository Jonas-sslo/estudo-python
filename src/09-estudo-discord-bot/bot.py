import os
from decouple import config
from discord.ext import commands
from discord import app_commands
import discord

MY_GUILD = discord.Object(id = 1111398730822844478)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)

bot = commands.Bot(intents = intents, command_prefix = "!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    await load_cogs(bot)
    synced = await bot.tree.sync(guild = MY_GUILD)
    print(f"Synced {len(synced)} command(s)")
    await bot.get_cog("Dates").current_time.start()

async def load_cogs(bot):
    await bot.load_extension("manager")
    await bot.load_extension("tasks.dates")
    for file in os.listdir("src/09-estudo-discord-bot/commands"):
        if file.endswith(".py"): 
            await bot.load_extension(f"commands.{file[:-3]}")

TOKEN = config("TOKEN")
bot.run(TOKEN)
