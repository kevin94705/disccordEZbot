import discord
import time
import os
import json
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
    
    print(message.author.id,message.content)   
    #防止bot回自己話
    if message.author.id == bot.user.id:
        return
    if message.content == "":
        return
    if '還錢' in message.content:        
        if len(message.content)>2:
            text=message.content
            t1=text.find('還')
            Subject=text[0:t1]
            if '垃圾馬' in Subject:
                await  channel.send("郭 我什麼都沒做")
            else: 
                await channel.send(str(Subject))
                await channel.send("還錢")
        else:            
            await channel.send("誰要還?")
    
    elif "打架" in message.content or "決鬥" in message.content:        
        await channel.send(file=discord.File('C:\disbot\dolo.jpg'))
        return 
    
    await bot.process_commands(message)#可以讓bot好好的接到commands指令工作

if __name__ == '__main__':
    bot.add_cog(games.Games(bot))        #加入discord bot的cog
    #bot.add_cog(armod.ARmod(bot))
    bot.add_cog(bosslist.boss(bot))
    with open('key.json','r') as reader:
        token = json.loads(reader.read())['token']
       
    bot.run(token)#啟動bot