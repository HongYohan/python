# from fileinput import close


# f=open("C:/Users/82106/Desktop/Python/txt/members.txt","w")
# f=close()

with open("C:/Users/82106/Desktop/Python/txt/members.txt","r") as f:
    txts=f.read()
    txts=txts.splitlines()
    print(txts)
    
with open("C:/Users/82106/Desktop/Python/txt/report2.txt","w") as f:
    a=''
    b=''
    i=0
    while True:
        for i in range(0,len(txts)):
            a=txts[i].split(',')
            b=a[1]
            name=a[0]
            if b == "학생":
                c=15000*int(a[2])
            elif b == "일반":
                c=50000 * int(a[2])
            else:
                c=30000* int(a[2])
            print(name,": 등록금액",c, file=f)
            
        if i == len(txts)-1:
            break;