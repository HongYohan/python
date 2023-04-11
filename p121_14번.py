sub1=float(input('과목1 성적 : '))
sub2=float(input('과목2 성적 : '))
sub3=float(input('과목3 성적 : '))
sub4=float(input('과목4 성적 : '))
sub5=float(input('과목5 성적 : '))

total=sub1+sub2+sub3+sub4+sub5
avg=total/5

print("5과목의 총점은 : {}, 5과목의 평균은 : {}".format(int(total),avg))
