# from re import sub


# subject=1
# total=0


# for i in range(10):
#     score=int(input(str(subject)+"번째 성적 입력 : "))

#     if(score>=0 and score<=100):
#         total=total+score
#         print(subject,"번째 성적 :",score)
#         subject+=1
#         if subject == 6:
#             break;
#     else:
#         print(" 유효한 성적이 아닙니다")
        



# print("총점 :",total)
# print("평군 :",total/5)

count=int(input("과목수 : "))
subject=1
total=0

for i in range(1,count+1): #무한루프가 안됨
    while True:
        score=int(input(str(subject)+"번째 성적 입력 : "))
        if(score>=0 and score<=100):
            total=total+score
            print(subject,'번째 성적 :', score)
            subject+=1
            break;
        else:
            print("유효하지 않은 값")
        
print("총점 :",total)
print("평균 :",total/count)