def convertIntToStr(int):
    digits = '0123456789'
    result = ''

    if int == 0:
        return '0'
    
    while int > 0:
        result = digits[int%10] + result
        int = int // 10
    return result


print(convertIntToStr(145))