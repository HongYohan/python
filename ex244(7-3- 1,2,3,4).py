source=input("source파일 입력 :")
target=input("target파일 입력 :")

with open (source,"r") as f:
    txts=f.read()
with open (target,"w") as f:
    f.write(txts) #타겟 경로에 txts를 그대로 적는다


f=open("C:/Users/82106/Documents/stu.txt","w")
i=1
while i <=5:
    score=input("%d번째 학생 이름과 3과목 성적입력(예: 홍길동 80 90 70) : "%i)
    f.write(score+"\n")
    i=i+1
f.close()
    

with open("C:/Users/82106/Documents/stu.txt","r") as f :
    lines=f.readlines()
    a=0
    while a <= len(lines)-1 :
        scorelist=lines[a].split() # 공백 기준으로 리스트 객체로 변환
        name=scorelist[0]
        a=a+1
        sum=0
        i=1
        while i <=3 :
            sum=sum+int(scorelist[i])
            i=i+1
        print(name+"의 평균 성적은 :",sum/3)


enter=[]
while True:
    text=input("저장할 문장 입력(끝-엔터키) : ")
    if text == '':
        break;
    enter.append(text+"\n")
print("입력될 리스트 :",enter)

with open ("C:/Users/82106/Documents/out.txt","w") as f :
    f.writelines(enter)
print("out.txt 파일이 생성되었습니다.")