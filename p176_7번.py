while True:
    month=int(input("가장 좋아하는 월은?(종료:0)"))
    if month == 0:
        break;
    print("*** {}월 ***".format(month))
    
    
    if month >=3 and month <=5:
        print("{}월은 봄에 해당됩니다".format(month))
    elif month >=6 and month <=8:
        print("{}월은 여름에 해당됩니다".format(month))
    elif month >=9 and month <=11:
        print("{}월은 가을에 해당됩니다".format(month))
    elif month >= 12 or month <=2:
        print("{}월은 겨울에 해당됩니다".format(month))