s1={1,2,3,4,5}
s1.add(6) #추가
print(s1)

s1.discard(6) #제거
s1.remove(5) #제거

s2={1,2,3,4}
print(s1==s2)

s3={1,2,3,4,5}
s1.issubset(s3) #s1이 s3의 부분집합인가?
s3.issuperset(s1) #s3이 s1의 상위집합인가

print(s1|s3) #합집합
print(s1&s3) #교집합
print(s1-s3) #차집합