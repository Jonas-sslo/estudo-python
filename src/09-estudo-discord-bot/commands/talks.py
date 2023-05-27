from discord.ext import commands
import discord


class Talks(commands.Cog):
    """ Talks with user """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="oi", help="Envia um Oi(Não requer argumento)")
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = "Olá, " + name
        await ctx.channel.send(response)

    @commands.command(name="segredo", help="Envia um segredo no privado.Não requer argumento")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Banana!")
        except discord.errors.Forbidden:
            await ctx.send("Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)")


async def setup(bot):
    await bot.add_cog(Talks(bot))
