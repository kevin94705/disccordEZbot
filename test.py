#-*-conding='utf-8'-*-
import os
import csv
csv_file_addr=os.path.join(os.getcwd(),'data','Alchemy.csv')
item_num=0
alchemy_list=[]
with open(csv_file_addr,'r',encoding='utf-8') as alchemymap:
    rows = csv.reader(alchemymap)#,讀取
    for row in rows:        
        if item_num==0:
            #print(row)
            #抓抬頭
            pass
        else:
            #去空白            
            for i in range(row.count('')):                
                row.remove('')
            alchemy_list.append(row)        
        item_num+=1
     
alchemymap.close()
##tile 0 title 1 need_num 2
print(alchemy_list)