month=int(input('현재 입력받은 월 : '))

if (month >12 or month <1) :
    print('잘못 입력했습니다')

elif (month >=3 and month <=5) :
    print('봄')

elif (month >=6 and month <=8) :
    print('여름')
    
elif (month >=9 and month <=11) :
    print('가을')
    
else :
    print('겨울')