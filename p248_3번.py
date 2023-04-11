# f=open ("C:/Users/82106/Desktop/Python/txt/score.txt","w")
# f.close()
    
    
with open ("C:/Users/82106/Desktop/Python/txt/score.txt","r") as f:
    txts=f.read()
    txts= txts.split()
    
    

with open ("C:/Users/82106/Desktop/Python/txt/report1.txt","w") as f:
    i=1
    num=0
    while True:
        if i%2==0:
            num=int(txts[i-1])
            if num >=90:
                print(txts[i-2],": A", file=f)
            elif num >= 80:
                print(txts[i-2],": B", file=f)
            elif num >= 70:
                print(txts[i-2],": C", file=f)
            elif num >=60:
                print(txts[i-2],": D", file=f)
            else:
                print(txts[i-2],": E", file=f)
        if i == len(txts):
            break;
        i=i+1