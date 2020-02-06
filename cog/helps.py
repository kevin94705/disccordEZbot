import time
import datetime
import discord
import os
from discord.ext import commands


class helps(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # .help
    @commands.command(aliases=["h"])
    async def _helps(self, ctx):
        
        await ctx.send(".boss        查詢下一隻王及距離時間 \n.boss l     查詢下一隻王及距離時間 再傳送一張圖片")
        await ctx.send(".roll        1~6隨機拿到一個數字")
        await ctx.send(".ar          隨機從AR字典裏面發出一句話\n.ar [anything] 可以教AR說話加入AR字典")
        await ctx.send(".serch or .s | .s 料理 <名稱>")