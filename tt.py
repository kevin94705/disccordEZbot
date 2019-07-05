import discord
import time
import os
import bosslist
import armod

from discord.ext import commands

client = commands.Bot(command_prefix = ".")


master = 100

@client.event
async def on_ready():
    print('bot is ready')
'''
@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return    
'''
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command(aliases=['等下甚麼王','nextboss','boss'])
async def _boss(ctx):
    dayOfhour=int(time.strftime("%H", time.localtime()))
    dayOfWeek=time.strftime("%a", time.localtime())
    dayOfmin=int(time.strftime("%M",time.localtime()))
    ans=bosslist.whichboss(dayOfWeek,dayOfhour,dayOfmin)
    print(dayOfWeek,dayOfhour,dayOfmin)
    await ctx.send(f'{ans}  ')
    
@client.command()
async def ar(ctx,*,lear=None):
    if lear!=None:
        armod.learning(lear)
            
    else:
        text=armod.says()  
        await ctx.send(text)

@client.command(aliases=['OK還錢','夢夢還錢','告娃娃還錢','AR還錢','ar還錢'])
async def _i(ctx):
    
    await ctx.send(file=discord.File('C:\disbot\Vedlve0.jpg'))


client.run('NTc2NzY4NzMzNzU0ODE4NTcw.XRUBMA.C0ockwxUlZbRQj8z2oI562nzp5c')