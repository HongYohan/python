level=int(input('직급 입력 : '))
age=int(input('나이 입력 : '))


if (level > 5 or level < 8) and (age < 40 or age >60) :
    print('연금 대상자가 아닙니다')
    
elif (level >= 7 and level <=8) and (age <= 49 and age >= 40) :
    print('연금 80% 대상자입니다.')
    
elif (level == 5 or level ==6) and (age <= 59 and age >= 50) :
    print('연금 100% 대상자입니다.')