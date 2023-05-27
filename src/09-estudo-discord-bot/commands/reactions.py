from discord.ext import commands


class Reactions(commands.Cog):
    """ Work with Reactions """
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(1111485274967527464)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(1111485329766101003)
            await user.add_roles(role)

async def setup(bot):
    await bot.add_cog(Reactions(bot))