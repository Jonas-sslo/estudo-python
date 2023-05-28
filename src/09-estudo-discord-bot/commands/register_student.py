from discord.ext import commands
from discord import app_commands
import discord
MY_GUILD = discord.Object(id = 1111398730822844478)

intents = discord.Intents.default()
client = discord.Client(intents = intents)
tree = app_commands.CommandTree(client)


class Register(commands.Cog):
    """ Register students """

    def __init__(self, bot): 
        self.bot = bot

    @app_commands.command(name = "cadastrar-aluno", description = "Cadastra um aluno. Argumento: prontuario, nome e email")
    async def register_student(self, interaction: discord.Interaction, prontuario:str, nome:str, email:str):
        with open("src/09-estudo-discord-bot/commands/alunos.txt", "r", encoding = "UTF-8") as arquivo:
            arquivo = arquivo.read()

            if prontuario in arquivo:
                await interaction.response.send("Já existe um aluno com esse prontuário. Reinsira!")
            elif email in arquivo:
                await interaction.response.send_message("Já existe um aluno com esse email. Reinsira!")
            else:
                with open("src/09-estudo-discord-bot/commands/alunos.txt", "a", encoding = "UTF-8") as arquivo:
                    aluno = f"{prontuario}, {nome}, {email} \n"
                    arquivo.write(aluno)
                await interaction.response.send_message(f"O aluno {nome} foi cadastrado.")

async def setup(bot):
    await bot.add_cog(Register(bot), guilds = [MY_GUILD])