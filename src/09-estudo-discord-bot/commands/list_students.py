from discord.ext import commands
import discord

class List(commands.Cog):
    """ List students"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "listar-alunos")
    async def list_students(self, ctx, ):
        embed = discord.Embed(
            title = "Resultado da busca de alunos cadastrados",
            description = "Apenas alunos cadastrados",
            color=0x0000FF
        )

        embed.add_field(name = "Alunos", value = "")

        with open("src/09-estudo-discord-bot/commands/alunos.txt", "r", encoding = "UTF-8") as arquivo:
            for linha in arquivo.readlines():
                dado = linha.strip().split(",")
                embed.add_field(name = f"{dado[1]}", value = f"Prontuário: {dado[0]} e Email: {dado[2]}")

        embed.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar)
        embed.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar)

        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(List(bot))
            