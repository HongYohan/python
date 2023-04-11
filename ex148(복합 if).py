while True :
    num1=int(input('1번째 숫자 : '))
    op=input('연산자 : ')
    num2=int(input('2번째 숫자 : '))

    if (op == '+') :
        hap=num1+num2
        print('{} + {}는 {}'.format(num1, num2, hap))
        
    elif (op == '-') :
        minus=num1-num2
        print('{} - {}는 {}'.format(num1, num2, minus))
        
    elif (op == '*') :
        multiple=num1*num2
        print('{} * {}는 {}'.format(num1, num2, multiple))
        
    elif (op == '/') :
        division=num1/num2
        print('{} / {}는 {}'.format(num1, num2, round(division,2)))
        
    else :
        print('해당된 연산자는 없습니다.')
        break