import os
import random
from discord.ext import commands

data=[]
class ARmod(commands.Cog):
    def __init__(self,bot:commands.Bot):        
        self.bot = bot

    @commands.command()
    async def ar(self,ctx,*,lear=None):
        #學習
        if lear!=None:
            self.temp=self.learning(lear)
            await ctx.send(self.temp)
        else:
            arsays=self.says()            
            await ctx.send(arsays)   

    def says(self):    
        with open('ar.txt','r') as r:
            line = r.read().split(",")
            for i in  line:
                data.append(i)
        temp=random.choice(data)
        r.close()
        return temp

    def learning(self,learn_what):
        self.says() #讓data內有讀取TXT的資料
        with open('ar.txt','a') as w:
            if learn_what not in data:     
                w.write(',{learn_what}'.format(learn_what=learn_what))
                w.close()
            else:
                return "小看我?????早就會了"
        return "succsess"
    