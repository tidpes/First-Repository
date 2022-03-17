def leapYear(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    else:
        return False

def maxDay(m,y):
    if m==2:
        if leapYear(y)==False:
            return 28
        elif leapYear(y)==True:
            return 29
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31