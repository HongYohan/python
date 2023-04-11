sub1=int(input('첫 번째 과목의 점수 입력 : '))
sub2=int(input('두 번째 과목의 점수 입력 : '))
total=sub1+sub2

# if (sub1 >= 75 and sub2 >= 75):
    
#     if total >= 180 :
#         print('최우수 학생')
        
#     elif total >= 160 :
#         print('우수 학생')

#     else :
#         print('보통 학생')

# else :
#     print('분발합시다')

if sub1 >=75 and sub2>= 75 and total >= 180 :
    print('최우수 학생')
    
elif sub1 >=75 and sub2>= 75 and total >= 160 :
    print('우수 학생')
    
elif sub1 >=75 and sub2>= 75 and total >= 150 :
    print('보통 학생')
    
else :
    print('분발합시다')