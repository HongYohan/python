f=open("C:/Users/82106/Documents/test.txt","w")
for i in range(1,11):
    f.write("%d번째 줄입니다\n"%i)
f.close()

f=open("C:/Users/82106/Documents/test.txt","a")
f.write("마지막줄 : 홍요한")
f.close()

f=open("C:/Users/82106/Documents/test.txt","r")
txts=f.read()#read(n)에서 n개의 문자를 읽어 출력
print(txts)

# with open("text.txt","w") as f :  close 함수가 필요없음