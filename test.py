#-*-conding='utf-8'-*-
import os
import csv
csv_file_addr=os.path.join(os.getcwd(),'data','stand.csv')
item_num=0
cook_title=['品名', '材料', '數量', '材料', '數量', '材料', '數量', '材料', '數量', '材料', '數量']
cook_map=[]
#def cook_format():
#    return pass

with open(csv_file_addr,'r',encoding='utf-8') as cookmaps:
    rows = csv.reader(cookmaps)#,讀取
    for row in rows:        
        if item_num==0:
            #抓抬頭
            pass
        else:
            #去空白            
            for i in range(row.count('')):                
                row.remove('')
            cook_map.append(row)        
        item_num+=1
     
cookmaps.close()
##tile 0 title 1 need_num 2
print(cook_map)

