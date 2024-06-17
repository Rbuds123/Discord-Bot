import discord
from discord.ext import commands
import bot

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def echo(self, ctx, *, content: str):
        await ctx.send(content)

def setup(bot):
    bot.add_cog(General(bot))
