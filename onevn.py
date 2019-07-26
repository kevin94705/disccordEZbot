import discord
import time
import os

from discord.ext import commands
from cog import bosslist,armod,games

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print('bot is ready')
    print('bot id:'+bot.user.name)
    print('bot id:'+str(bot.user.id))

@bot.event
async def on_message(message):

    channel = message.channel

    print(message.author.id,time.localtime())   

    if message.author.id == bot.user.id:
        return
    if message.content == "":
        return
    if str(message.author.id)=='194004173753155584':        
        await channel.send(B嘴 告娃娃)
    if '還錢' in message.content:
        
        if len(message.content)>2:
            text=message.content
            t1=text.find('還')
            Subject=text[0:t1]            
            await channel.send(str(Subject))
            await channel.send("還錢")
        else:            
            await channel.send("誰要還?")


    await bot.process_commands(message)#可以讓bot好好的接到commands指令並工作

if __name__ == '__main__':
    bot.add_cog(games.Games(bot))        #加入discord bot的cog
    bot.add_cog(armod.ARmod(bot))
    bot.add_cog(bosslist.boss(bot))

    bot.run('toekn')#啟動bot