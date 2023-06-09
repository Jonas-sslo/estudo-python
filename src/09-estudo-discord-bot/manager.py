from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound


class Manager(commands.Cog):
    """ Manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "palavrão" in message.content:
            await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários!")
            await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Favor enviar todos os Argumentos. Digite !help para ver os parâmetros de cada comando")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe. Digite !help para ver todos os comandos")
        else:
            raise error


async def setup(bot):
    await bot.add_cog(Manager(bot))
