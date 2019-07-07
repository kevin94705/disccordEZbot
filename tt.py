import discord
import time
import os
import bosslist
import armod
import random

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
async def roll(ctx):
    await ctx.send(random.randint(0,6))

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
    standtime=ans.find(':')
    hourtime=int(ans[0:standtime])
    minstime=int(ans[standtime+1:standtime+3])   
    tttt=abs(hourtime-dayOfhour)
    ttttt=abs(dayOfmin-minstime)
    print(hourtime)
    print(minstime)
    await ctx.send(f'{ans} 還有{tttt}小時{ttttt}分')

    
@client.command()
async def ar(ctx,*,lear=None):
    if lear!=None:        
        #學習
        await ctx.send(armod.learning(lear))
    else:
        text=armod.says()  
        await ctx.send(text)

@client.command(aliases=['OK還錢','夢夢還錢','告娃娃還錢','AR還錢','ar還錢'])
async def _i(ctx):    
    await ctx.send(file=discord.File('C:\disbot\Vedlve0.jpg'))#傳圖片


client.run('NTc2NzY4NzMzNzU0ODE4NTcw.XRUBMA.C0ockwxUlZbRQj8z2oI562nzp5c')