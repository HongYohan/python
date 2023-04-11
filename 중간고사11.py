age=int(input('나이를 입력하시오 : '))

if (age >= 20):
    print('어른')
    
elif (age < 20 and age >= 10):
    print('청소년')
    
elif (age < 10) :
    print('아동')