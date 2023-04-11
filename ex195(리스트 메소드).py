lis1=list(range(1,21)) #범위가 1~20까지의 숫자를 리스트화
lis1[4]=('홍','요','한') # 4번째 인덱스에 튜플()로 대체 삽입
print(lis1)


del lis1[4] #4번째 인덱스 삭제
print(lis1)
print(sum(lis1)) # 리스트 요소의 합


lis1.append(5) # 리스트 마지막에 요소 추가
print(lis1)


lis2=list(range(0,11,2)) # 0~10까지 2씩 증가
print(lis2)


lis1.append(lis2)
print(lis1)
print(sum(lis2))


lis1.extend("python") # 리스트와 리스트 연결 확장
lis1.insert(2,"뭘보냐") # 리스트 특정 위치에 요소 삽입
print(lis1)

lis1.pop() # 리스트의 마지막 요소 삭제
print(lis1)

print(lis1.count(3)) # 리스트에서 3이라는 숫자의 개수

list9=['dragon','busan','fucx']
list9.sort() # 리스트 오름차순 정렬
list9.reverse() # 리스트 역순 정렬
print(list9)