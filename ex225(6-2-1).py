phone={}

i=1
while i <=5:    
    id=int(input("{}번째 학생 학번 입력 : ".format(i)))
    num=input("{}번째 학생 번호 입력 : ".format(i))
    phone[id]=num
    i +=1

print("학생 전화번호부가 완성됨")
id=int(input("학번 입력 : "))
if id in phone:
    print("입력한 학생 번호 :",phone[id])
else:
    print("없는 학번")