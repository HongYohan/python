import random

# num1=set()
# num2=set()
# while True:
#     if len(num1) <10:
#         num1.add(random.randint(1,100))
#     if len(num2) <10:
#         num2.add(random.randint(1,100))
#     if len(num1) == 10 and len(num2) == 10:
#         break;

# print("발생된 10개의 난수 1 :",num1)
# print("발생된 10개의 난수 2 :",num2)
# print("합집합",num1|num2)
# print("교집합",num1&num2)
# print("차집합",num1-num2)


lotto=set()
while True:
    if len(lotto) <6:
        lotto.add(random.randint(1,45))
    if len(lotto) == 6:
        break;



print("이번주 로또 넘버 :",sorted(lotto))