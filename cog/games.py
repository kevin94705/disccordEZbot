import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self,bot:commands.Bot):        
        self.bot = bot

    def ex_card(self,cards, num):
        labels = [0]    
        for card in cards:
            print(labels[-1]),card[1]
            labels.append(labels[-1] + card[1])
    

        rands = [random.randint(1, labels[-1]) for _ in range(num)]
        print(rands,labels)
        for rand_i, rand in enumerate(rands):
            for label_i, label in enumerate(labels):
                if label >= rand:
                    rands[rand_i] = cards[label_i - 1]
                    break
        
        return rands

    @commands.command()
    async def roll(slef,ctx):
        await ctx.send(random.randint(0,6))

    @commands.command(aliases=["今天適合點裝嗎"])
    async def hope(slef,ctx):
        random.seed()
        cards = [['就是今天',1], ['點爆!',5], ['BANG! BANG! BANG!', 94]]
        exs = slef.ex_card(cards, 1)
        print(exs[0][0])
        await ctx.send(exs[0][0])