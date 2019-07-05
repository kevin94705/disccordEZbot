import time 

def whichboss(w,h,m): 
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
            return '15:00 貝爾 \n 14.30漁村出發逾時不候'
        elif 15<=h<19:
            return '19:00 卡嵐達、庫屯'
        elif 19<=h<=23:            
            if h==23 and m>30:
                return '00:15 肯恩特、木拉卡'
            else:
                return '23:30 奧平'
if __name__ == "__main__":
    print(whichboss('Sun',14,38))