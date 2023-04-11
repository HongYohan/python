print('당신의 나이는{}세 입니다'.format(19))
print('이름은 {}이고 나이는{}세'.format('홍길동', 19))
print('{0}에 {0}을 더하면 {0}이 되고, \
{1}에 {0}을 더하면 {1}가 됩니다'.format('정수','실수'))


print('이름은 {name}이고, 나이는 {age}세이고, \
주소지는 {addr}입니다'.format(age=24, addr='거제시', name='홍요한'))




#15칸지정
print('The best language is ({:15})'.format('Python'))  #문자열은 왼쪽정렬
print('The best language is ({:15})'.format(77777))     #숫자는 오른쪽정렬
print('The best language is ({:>15})'.format('Python')) #>는 오른쪽정렬
print('The best language is ({:<15})'.format(77777))    #<는 왼쪽정렬
print('The best language is ({:^15})'.format(77777))    #^는 중앙정렬