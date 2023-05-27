from discord.ext import commands, tasks
import datetime

class Dates(commands.Cog):
    """ Work with dates """

    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(hours = 1)
    async def current_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%d/%m/%Y as %H:%M:%S")

        channel = self.bot.get_channel(1111398732102123562)

        await channel.send("Data atual: " + now)


async def setup(bot):
    await bot.add_cog(Dates(bot))
