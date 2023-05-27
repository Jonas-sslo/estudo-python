from discord.ext import commands
import discord


class Images(commands.Cog):
    """ Work with Images """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "foto", help= "Envia uma foto no privado. Não requer argumento")
    async def get_random_image(self, ctx):
        url_image = "https://picsum.photos/200/300"

        embed_image = discord.Embed(
            title = "Resultado da busca de imagem",
            description = "PS: A busca é totalmente aleatória",
            color=0x0000FF
        )

        embed_image.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar)
        embed_image.set_footer(text = "Feito por " + self.bot.user.name, icon_url = self.bot.user.avatar)

        embed_image.add_field(name = "API", value="Usamos a API do https://picsum.photos")
        embed_image.add_field(name = "Parâmetros", value = "{largura}/{altura}")

        embed_image.add_field(name = "Exemplo", value = url_image, inline = False)

        embed_image.set_image(url = url_image)

        await ctx.send(embed = embed_image)


async def setup(bot):
    await bot.add_cog(Images(bot))
