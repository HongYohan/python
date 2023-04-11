sex=input("당신의 성별은 'M or m' 또는 'F or f' : ")
height=float(input('키를 입력(cm) : '))/100
weight=float(input('몸무게 입력(kg) : '))

if (sex == 'm' or sex == 'M'):
    male=height*height*22
    if 110<= weight/male*100 and weight/male*100 <=119:
        print('과체중')
        
    elif 120 <= weight/male*100 :
        print('비만 체중')
        
    else :
        print('표준 체중')
        
elif (sex == 'f' or sex == 'F'):
    female=height*height*21
    if 110<= weight/female*100 and weight/female*100 <=119:
        print('과체중')
        
    elif 120 <= weight/female*100 :
        print('비만 체중')
        
    else :
        print('표준 체중')
        
else :
    print('성별 입력이 잘못 되었습니다')