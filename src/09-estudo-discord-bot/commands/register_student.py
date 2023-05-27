from discord.ext import commands


class Register(commands.Cog):
    """ Register students """

    def __init__(self, bot): 
        self.bot = bot

    @commands.command(name = "cadastrar-aluno", help = "Cadastra um aluno. Argumento: prontuario, nome e email")
    async def register_student(self, ctx, prontuario, nome, email):
        with open("src/09-estudo-discord-bot/commands/alunos.txt", "r", encoding = "UTF-8") as arquivo:
            arquivo = arquivo.read()

            if prontuario in arquivo:
                await ctx.send("Já existe um aluno com esse prontuário. Reinsira!")
            elif email in arquivo:
                await ctx.send("Já existe um aluno com esse email. Reinsira!")
            else:
                with open("src/09-estudo-discord-bot/commands/alunos.txt", "a", encoding = "UTF-8") as arquivo:
                    aluno = f"{prontuario}, {nome}, {email} \n"
                    arquivo.write(aluno)
                await ctx.send(f"O aluno {nome} foi cadastrado.")

async def setup(bot):
    await bot.add_cog(Register(bot))