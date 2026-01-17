def sum_list(l):
    if not  l :
        return 0
    else:
        return l[0] + sum_list(l[1:])
    
def fibonachicci(n):
    if n<=0:
        return "invalid input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonachicci(n-1) + fibonachicci(n-2)