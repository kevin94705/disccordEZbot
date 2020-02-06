import time 
import datetime
import discord
import os
from discord.ext import commands

class boss(commands.Cog):
    def __init__(self,bot:commands.Bot):        
        self.bot = bot

    @commands.command(aliases=['等下甚麼王','nextboss','boss','BOSS'])
    async def _boss(self,ctx,*,all=None):
        work_path = os.getcwd()
        boss_png= os.path.join(work_path,'allbosslist.png')
        dayOfhour=int(time.strftime("%H", time.localtime()))
        dayOfWeek=time.strftime("%a", time.localtime())
        dayOfmin=int(time.strftime("%M",time.localtime()))
        ans=self.whichboss(dayOfWeek,dayOfhour,dayOfmin)
        print(dayOfWeek,dayOfhour,dayOfmin)    
        standtime=ans.find(':')
        hourtime=int(ans[0:standtime])
        minstime=int(ans[standtime+1:standtime+3]) 
        
        h1=self.distance(dayOfhour,dayOfmin,hourtime,minstime)[0]
        m1=self.distance(dayOfhour,dayOfmin,hourtime,minstime)[1]
        if all==None:            
            await ctx.send('下一隻 {ans}\n還有{h1}小時{m1}分'.format(ans=ans,h1=h1,m1=m1))
        else:
            await ctx.send('下一隻 {ans}\n還有{h1}小時{m1}分'.format(ans=ans,h1=h1,m1=m1))
            await ctx.send(file=discord.File(boss_png))
    def whichboss(self,w,h,m):
        if w=='Mon':        
            if (h==0)and(m<=15):
                return '00:15 肯恩特、木拉卡'
            elif 0<=h<2:
                return '2:00 克價卡、庫屯'
            elif 2<=h<11:
                return '11:00 卡蘭達'
            elif 11<=h<15:
                return '15:00 克價卡、庫屯'
            elif 15<=h<19:
                return '19:00 卡莫斯'
            elif 19<=h<=23:
                if h==23 and m>30:
                    return '2:00 羅裴勒'
                else:
                    return '23:30 克價卡、庫屯'
        elif w=='Tue':
            if 0<=h<2:
                return '2:00 羅裴勒'
            elif 2<=h<11:
                return '11:00 克價卡、庫屯'
            elif 11<=h<15:
                return '15:00 卡蘭達、羅裴勒'
            elif 15<=h<19:
                return '19:00 庫屯'
            elif 19<=h<=23:
                if h==23 and m>30:
                    return '2:00 卡蘭達'
                else:
                    return '23:30 克價卡、羅裴勒'
        elif w=='Wed':
            if 0<=h<2:
                return '2:00 卡蘭達'
            elif 2<=h<11:
                return '11:00 克價卡、羅裴勒'
            elif 11<=h<15:
                return '15:00 卡莫斯'
            elif 15<=h<19:
                return '19:00 克價卡、庫屯'
            elif 19<=h<=23:
                if h==23 and m>30:
                    return '2:00 庫屯'
                else:
                    return '23:30 羅裴勒、卡蘭達'
        elif w=='Thu':
            if 0<=h<2:
                return '2:00 庫屯'
            elif 2<=h<11:
                return '11:00 卡蘭達、庫屯'
            elif 11<=h<15:
                return '15:00 克價卡、羅裴勒'
            elif 15<=h<19:
                return '19:00 羅裴勒'
            elif 19<=h<=23:
                if h==23 and m>30:
                    return '2:00 克價卡、羅裴勒'
                else:
                    return '23:30 卡蘭達、庫屯'
        elif w=='Fri':
            if 0<=h<2:
                return '2:00 克價卡、羅裴勒'
            elif 2<=h<11:
                return '11:00 奧平'
            elif 11<=h<15:
                return '15:00 羅裴勒、卡蘭達'
            elif 15<=h<19:
                return '19:00 克價卡、庫屯'
            elif 19<=h<=23:
                if h==23 and m>30:
                    return '00:15 卡莫斯'
                else:
                    return '23:30 肯恩特、木拉卡'
        elif w=='Sat':
            if (h==0)and(m<=15):
                return '00:15 卡莫斯'
            elif 0<=h<2:
                return '2:00 克價卡、庫屯'
            elif 2<=h<11:
                return '11:00 卡蘭達、庫屯'
            elif 11<=h<15:
                return '15:00 奧平'
            elif 15<=h<19:
                return '19:00 克價卡、羅裴勒'
            elif 19<=h<24:
                return '2:00 卡嵐達、羅裴勒'
        elif w=='Sun':
            if 0<=h<2:
                return '2:00 卡嵐達、羅裴勒'
            elif 2<=h<11:
                return '11:00 克價卡、羅裴勒'
            elif 11<=h<15:
                return '15:00 貝爾 \n14.30漁村出發逾時不候'
            elif 15<=h<19:
                return '19:00 卡嵐達、庫屯'
            elif 19<=h<=23:            
                if h==23 and m>30:
                    return '00:15 肯恩特、木拉卡'
                else:
                    return '23:30 奧平'
    def distance(self,h,m,h1,m1):
        if h1-h<0:
            if h==0:
                h=24            
            if h1==0:
                h1=24
            if h1<h:
                h1+=24        
            if m1-m<0:
                h1-=1
                m1+=60        
            dh=abs(h1-h)
            dm=abs(m1-m)
            return dh,dm
        else:
            if m1-m<0 and h1-h>=0:
                h1-=1
                m1+=60
            dh=abs(h1-h)
            dm=abs(m1-m)
            return dh,dm
