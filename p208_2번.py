student=list(input("학생 : "))

for i in range(len(student)):
    if ',' in student:
        student.remove(',')

cnt=0
dap=[]
for j in range(0,10):
    answer=str(input("{}번 : ".format(j+1)))
    dap.append(answer)
    if dap[j] == student[j]:
        cnt=cnt+1


print("학생의 점수 : {}점".format(cnt))