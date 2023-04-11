# 주소 바꿔서 확인

f=open("C:/Users/82106/Desktop/Python/txt/stu.txt","w")
i=1
while i <=5:
    score=input("%d번째 학생 이름과 3과목 성적입력(예: 홍길동 80 90 70) : "%i)
    f.write(score+"\n")
    i=i+1
f.close()



with open("C:/Users/82106/Desktop/Python/txt/stu.txt","r") as f :
    lines=f.readlines()
    korean=0
    math=0
    english=0
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
        korean=korean+int(scorelist[1])
        math=math+int(scorelist[2])
        english=english+int(scorelist[3])
    print("국어전체평균 :",korean/len(lines))
    print("수학전체평균 :",math/len(lines))
    print("영어전체평균 :",english/len(lines))