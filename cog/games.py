import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self,bot:commands.Bot):        
        self.bot = bot 

    @commands.command()
    async def roll(slef,ctx):
        await ctx.send(random.randint(0,6))
    