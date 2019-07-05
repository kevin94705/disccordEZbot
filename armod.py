import random

data=[]
nowseek=0
def says():    
    with open('ar.txt','r') as r:
        line = r.read().split(",")
        for i in  line:
            data.append(i)
    temp=random.choice(data)
    r.close()
    return temp

def learning(learn_what):
    with open('ar.txt','a') as w:        
        w.write(f',{learn_what}')
        w.close()
    return "succsess"

if __name__ == "__main__":
    pass