#coding=utf-8
import time 
import datetime
import discord
import os
import csv
from discord.ext import commands

class cook(commands.Cog):
    def __init__(self,bot:commands.Bot):        
        self.bot = bot

    @commands.command(aliases=["s"])
    async def search(self,ctx,*,all=None):
        spt1 = all.split(' ')[0]
        spt2 = all.split(' ')[1]        
        if spt1=="料理":            
            if spt2 != None:                
                await ctx.send(self.cookmap(spt2))
            else :
                await ctx.send("沒按照格式0")
        else:            
            await ctx.send("沒按照格式 .serch ")
    def ans_format(self,b):
        material_num=(len(b)-1)/2 
        if material_num == 1:#一種材料:
            return b[0]+'\n  '+str(b[1])+' '+str(b[2])
        if material_num == 2:#兩種材料:
            return b[0]+'\n  '+str(b[1])+' '+str(b[2])+'\n  '+str(b[3])+' '+str(b[4])
        if material_num == 3:#兩種材料:
            return b[0]+'\n  '+str(b[1])+' '+str(b[2])+'\n  '+str(b[3])+' '+str(b[4])+'\n  '+str(b[5])+' '+str(b[6])
        if material_num == 4:#兩種材料:
            return b[0]+'\n  '+str(b[1])+' '+str(b[2])+'\n  '+str(b[3])+' '+str(b[4])+'\n  '+str(b[5])+' '+str(b[6])+'\n  '+str(b[7])+' '+str(b[8])
        if material_num == 5:#兩種材料:
            return b[0]+'\n  '+str(b[1])+' '+str(b[2])+'\n  '+str(b[3])+' '+str(b[4])+'\n  '+str(b[5])+' '+str(b[6])+'\n  '+str(b[7])+' '+str(b[8])+'\n  '+str(b[9])+' '+str(b[10])

    def cookmap(self,cookname):
        cook_map=[['起司','牛奶','1'],['鮮奶油','牛奶','1','砂糖','1'],['奶油','鮮奶油','1','鹽','1'],['剁碎的鳥肉','白肉','3'],['醋','穀物','1','水果','1','砂糖','1','發酵劑','1'],['酒的精髓','水果','1','麵粉','1','發酵劑','1'],['醬料','雞蛋','1','鹽','2','橄欖油','1','料理用飲用水','1'],['紅醬','紅肉','1','砂糖','2','基本醬料','1','料理用飲用水','2'],['白醬','水果','1','牛奶','1','基本醬料','1','料理用紅酒','2'],['高級紅蘿蔔汁','高級紅蘿蔔','1','麵粉','3','砂糖','3','料理用飲用水','4'],['特等紅蘿蔔汁','特產紅蘿蔔','1','麵粉','3','麵粉','3','料理用飲用水','4'],['好的飼料','紅肉','6','魚乾','2','麵粉','4','料理用飲用水','3'],['有機飼料','燕麥片','2','紅肉','5','白肉','4','魚乾','2'],['啤酒','穀物','5','砂糖','1','發酵劑','2','料理用飲用水','6'],['烤鳥肉','雞肉','2','油炸用油','6','料理用紅酒','2','鹽','1'],['燕麥片','牛奶','3','食用蜂蜜','2','洋蔥','3','麵粉','9'],['魚片','麵粉','7','魚乾','2','鹽','2','白醬','3'],['普里卡燉蛇肉','普里卡','6','八角','2','蛇肉','3','料理用飲用水','5'],['起司派','雞蛋','3','麵糰','4','起司','7','奶油','3'],['清蒸雞肉','白肉','5','蔬菜','3','鹽','2','醋','2','酒的精髓','2'],['肉丸子','紅肉','8','雞蛋','2','麵粉','5','起司','2','油炸用油','4'],['奶茶','香味很好的茶','2','牛奶','3','食用蜂蜜','3','麵粉','2'],['各色小菜','炸雞','1','水果','5','海鮮乾','4','起司','3'],['蘇特茶','香味很好的茶','2','牛奶','3','奶油','2','鹽','1'],['鯨魚肉沙拉','大王鯨魚肉','1','蔬菜','6','雞蛋','3','胡椒','4','醬料','2'],['清蒸魚','魚乾','2','蒜頭','2','鹽','2','料理用飲用水','3'],['蘆薈餅乾','蘆薈','5','食用蜂蜜','3','麵糰','7','砂糖','4'],['清蒸海鮮','海鮮乾','2','辣椒','3','鹽','2','料理用飲用水','6'],['烤香腸','紅肉','6','洋蔥','1','胡椒','2','鹽','2'],['水煮蛋','雞蛋','3','鹽','1','料理用紅酒','1','料理用飲用水','6'],['炒肉','紅肉','7','洋蔥','2','辣椒','3','基本醬料','2'],['暗黑布丁','燕麥片','1','醃製蔬菜','1','白肉','5','二類血','7'],['火腿三明治','柔軟的麵包','2','烤香腸','2','蔬菜','5','雞蛋','4'],['柯爾克的泡酒','蜂蜜酒','5','柯爾克的角','1','椰棗','6','砂糖','6','發酵劑','6'],['烤奶油海鮮','海鮮乾','2','奶油','3','鹽','2','橄欖油','1'],['煙燻魚排','魚乾','2','鹽','2','橄欖油','3'],['起司焗烤','烤香腸','1','蔬菜','4','麵糰','5','起司','3','紅醬','3'],['牡蠣煎餅','牡蠣','3','雞蛋','2','麵粉','5','橄欖油','3','醋','2'],['炒海鮮','蔬菜','4','辣椒','2','海鮮乾','2','白醬','2'],['海鮮義大利麵','蒜頭','3','海鮮乾','2','麵糰','5','料理用紅酒','3'],['水果派','水果','6','麵糰','6','鮮奶油','3','砂糖','4'],['肉湯','紅肉','5','胡椒','1','鮮奶油','2','料理用飲用水','4'],['魚湯','魚乾','2','麵粉','3','鮮奶油','2','料理用飲用水','6'],['椰子酥脆炸魚','椰子果','3','雞蛋','2','魚乾','2','麵糰','3','油炸用油','4'],['奶油焗龍蝦','龍蝦','1','蒜頭','3','奶油','4','鹽','5','橄欖油','5'],['烤起司彩虹蘑菇','彩虹蘑菇','1','紅肉','2','起司','2','鹽','3','橄欖油','4'],['胡樂米','牦牛肉','5','穀物','2','牛奶','1','蒜頭','5','鹽','2'],['炸蔬菜','蔬菜','4','雞蛋','2','麵糰','3','油炸用油','6'],['炸雞','白肉','7','雞蛋','2','胡椒','3','麵粉','4'],['水果布丁','水果','5','牛奶','3','鮮奶油','1','砂糖','2'],['蔬菜水果沙拉','水果','4','蔬菜','4','料理用紅酒','2','醋','1'],['椰子義大利麵','椰子果','2','洋蔥','2','蒜頭','4','麵糰','5','白醬','1'],['森林之王漢堡','苔麩麵包','4','醃製蔬菜','2','獅子肉','4','肉豆蔻','3'],['烤蠍子','蠍子肉','3','肉豆蔻','3','辣椒','3','奶油','2'],['歐姆蛋','穀物','5','雞蛋','5','鹽','2','橄欖油','2'],['蜂蜜酒','食用蜂蜜','3','砂糖','2','料理用飲用水','6','酒的精髓','2'],['清蒸鯨魚肉','蜂蜜酒','1','大王鯨魚肉','1','蒜頭','4','鹽','2','料理用飲用水','6'],['瘦肉沙拉','紅肉','8','胡椒','3','醬料','4','醋','2'],['燉肉','紅肉','5','麵粉','2','料理用紅酒','2','料理用飲用水','3'],['肉排','紅肉','8','蒜頭','2','鹽','2','紅醬','2'],['果汁','水果','4','砂糖','3','鹽','1','料理用飲用水','5'],['香味很好的茶','花','4','水果','4','食用蜂蜜','3','料理用飲用水','7'],['椰棗酒','椰棗','5','砂糖','1','發酵劑','4','酒的精髓','2'],['鬆軟的麵包','牛奶','3','雞蛋','2','麵糰','6','發酵劑','2'],['烤蜥蜴肉串','爬蟲類的肉','6','穀物','7','洋蔥','3','紅醬','2'],['肉餡餅','紅肉','4','麵糰','6','砂糖','2','橄欖油','2'],['沙漠餃子','爬蟲類的肉','6','肉桂','1','麵糰','6','橄欖油','2'],['彩虹蘑菇三明治','彩虹蘑菇','1','鬆軟的麵包','1','鮮奶油','2','洋蔥','2','橄欖油','4'],['炸魚','魚乾','2','麵粉','3','油炸用油','2'],['魚肉沙拉','洋蔥','3','魚乾','2','起司','2','醬料','2'],['肉醬三明治','柔軟的麵包','1','紅肉','7','蔬菜','6','起司','3'],['清蒸明蝦','蝦子','4','甜椒','3','辣椒','2','料理用紅酒','3','料理用飲用水','4'],['海鮮蘑菇沙拉','蘑菇','1','海鮮乾','2','醬料','2'],['肉醬義大利麵','紅肉','5','蒜頭','2','胡椒','3','麵糰','4'],['明蝦沙拉','蔬菜水果沙拉','2','蝦子','2','雞蛋','3','鹽','2','橄欖油','3'],['蜂巢餅乾','牛奶','4','雞蛋','2','食用蜂蜜','6','麵糰','4'],['羊駝串起司燒烤','羊駝肉','5','起司','4','辣椒','3','胡椒','1','白醬','1'],['開心果炒飯','開心果','4','苔麩','6','肉桂','2','鹽','2'],['庫斯庫斯','普里卡燉蛇肉','1','蔬菜','4','肉豆蔻','3','苔麩麵糰','6'],['無花果派','無花果','5','麵糰','3','砂糖','3','橄欖油','2'],['穀物湯','穀物','6','鹽','1','料理用紅酒','3','料理用飲用水','3'],['醃製蔬菜','蔬菜','8','砂糖','2','發酵劑','2','醋','4'],['醬燒蛤蜊','蒜頭','5','辣椒','5','珍珠蛤肉乾','2','橄欖油','5','酒的精髓','5'],['苔麩麵包','苔麩粉','5','鹽','2','發酵劑','2','料理用飲用水','3'],['苔麩三明治','烤蠍子','1','苔麩麵包','1','普里卡燉蛇肉','1','紅醬','3'],['獵人的沙拉','柔軟的鯨魚肉','1','蒜頭','5','醋','2','醬料','2'],['椰子雞尾酒','異國的穀物酒','1','椰子果','2','水果','1','料理用飲用水','5','酒的精髓','2'],['異國的穀物酒','麵糰','3','發酵劑','2','料理用飲用水','5','酒的精髓','1'],['蘆薈優格','蘆薈','5','牛奶','2','砂糖','3','發酵劑','3'],['水果酒','異國的穀物酒','1','水果','5','料理用飲用水','2','酒的精髓','3'],['炒青菜','蔬菜','5','辣椒','2','鹽','1','橄欖油','2'],['醃魚','魚乾','2','鹽','4','發酵劑','2','醋','2'],['五穀雞肉粥','剁碎的鳥肉','2','料理用飲用水','2','穀物','3'],['羅宋湯','肉桂','1','牛奶','3','氣味濃烈的肉乾','7','料理用飲用水','2'],['炒蕨菜','蕨菜','8','蒜頭','5','鹽','2','料理用飲用水','5','橄欖油','2'],['土撥鼠燒烤','土撥鼠肉','5','辣椒','3','鹽','2','紅醬','1','料理用紅酒','3'],['巴雷諾斯套餐','起司焗烤','1','煙燻魚排','1','肉丸子','1','炒青菜','2','啤酒','2'],['賽林迪亞套餐','火腿三明治','1','蜂巢餅乾','1','肉餡餅','1','水煮蛋','2','水果酒','2'],['卡爾佩恩套餐','肉醬義大利麵','1','魚肉沙拉','1','起司派','1','奶茶','1','柔軟的麵包','2'],['梅迪亞套餐','暗黑布丁','1','瘦肉沙拉','1','燕麥片','1','異國的穀物酒','2','烤香腸','2'],['騎士團的戰鬥糧食','火腿三明治','1','暗黑布丁','1','肉丸子','1','水果酒','1'],['瓦倫西亞套餐','森林之王漢堡','1','苔麩三明治','1','庫斯庫斯','1','無花果派','2','椰棗酒','2'],['阿利赫恣特餐','椰子義大利麵','1','椰子酥脆炸魚','1','肉排','1','燉肉','1','椰子雞尾酒','2'],['瑪戈利雅海鮮特餐','奶油焗龍蝦','1','明蝦沙拉','1','清蒸明蝦','1','牡蠣煎餅','1','水果酒','2'],['卡瑪希爾比亞套餐','彩虹蘑菇三明治','1','烤起司彩虹蘑菇','1','椰子義大利麵','1','無花果派','1','水果酒','2'],['德利勘特餐','炒蕨菜','1','土撥鼠燒烤','1','胡樂米','1','羊駝串起司燒烤','1','蜂蜜酒','2'],['海鮮拼盤克羅恩套餐','巴雷諾斯套餐','3','卡爾佩恩套餐','3','瑪戈利雅海鮮特餐','1','古代克羅恩香料','1'],['簡單製作的克羅恩套餐','騎士團的戰鬥糧食','1','梅迪亞套餐','3','瓦倫西亞套餐','3','古代克羅恩香料','1'],['風味獨特的克羅恩套餐','賽琳迪亞套餐','3','阿利赫恣特餐','1','卡瑪希爾比亞套餐','3','古代克羅恩香料','1'],['充滿活力的克羅恩套餐','德利勘特餐','1','賽林迪亞套餐','3','梅迪亞套餐','3','古代克羅恩香料','1']]
        a=list
        for i in cook_map:                    
            if cookname in i:
                if i[0]==cookname :                    
                    a=i
                    return self.ans_format(a)
                else:
                    return "沒找到"
    
        