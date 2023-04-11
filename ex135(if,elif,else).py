score=int(input('점수 입력 :'))

if (score >= 90 and score <=100):
    print('A 학점')
    print('참 잘했어요!')

elif (score >= 80 and score < 90):
    print('B 학점')
    print('공부만 하시는군요!')
    
elif (score >= 70 and score < 80):
    print('C 학점')
    print('공부 반 놀이 반!')
    
elif (score >= 60 and score < 70):
    print('D 학점')
    print('공부에 시간을 좀더 투자하시오!')
    
elif (score < 60) :
    print('F 학점')
    print('낙제!')