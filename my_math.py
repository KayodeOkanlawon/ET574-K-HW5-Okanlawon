# my_math.py
# Name: Kayode Okanlawon
# QCC ID: 24615461

def pow(x, y):
  
    if y == 0:
        return 1


    if y < 0:
        result = 1
        for _ in range(-y):
            result *= x
        return 1 / result

    result = 1
    for _ in range(y):
        result *= x
    return result
