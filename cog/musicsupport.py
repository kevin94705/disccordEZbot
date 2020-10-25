#coding=utf-8
import os
import random
import discord
from discord.ext import commands


class support(commands.Cog):
    def __init__(self,bot:commands.Bot):        
        self.bot = bot

    @commands.command()
    async def play(self,ctx):
        user_id = ctx.message.author.id
        #channel = ctx.message.author.voice.channel
        #voice= await channel.connect()
        tmp = self.getlist(user_id)
        print(tmp)
        for i in tmp:
            if len(tmp)>1:            
                await ctx.send(f'!play {i}')
    

    def getlist(self,id):
        data=[]  
        with open('data/'+str(id)+'.txt','r',encoding='utf-8') as r:
            line = r.read().split(",,")            
            for i in  line:
                if i!="":
                    data.append(i)        
        return data