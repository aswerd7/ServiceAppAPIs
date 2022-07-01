from datetime import time

# Функции для проверки времени -------------

def timecheck(a, b, c, d):
    c = time.strftime(c, '%H:%M:%S')
    d = time.strftime(d, '%H:%M:%S')
    if (a <= c < b) or (c <= a < d):
        return True
    else:
        return False
    
def timecheckPR(a, b, c, d):
    c = time.strftime(c, '%H:%M:%S')
    d = time.strftime(d, '%H:%M:%S')
    if (a <= c < b) or (c <= a < d):
        if a >= c and b <= d:
            return True
        else:
            return False    
    else:
        return False