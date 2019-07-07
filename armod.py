import random

data=[]

def says():    
    with open('ar.txt','r') as r:
        line = r.read().split(",")
        for i in  line:
            data.append(i)
    temp=random.choice(data)
    r.close()
    return temp

def learning(learn_what):
    says()
    with open('ar.txt','a') as w:
        if learn_what not in data:     
            w.write(f',{learn_what}')
            w.close()
        else:
            return "小看我?????"
    return "succsess"

if __name__ == "__main__":
    pass