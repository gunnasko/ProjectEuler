
basic_numbers = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

double_digit = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def underHoundredToString(number):
    if number < 20:
        return basic_numbers[number]
    if number < 100:
        stringToRet = double_digit[number/10]
        if number%10 != 0:
            stringToRet = stringToRet + '-' + basic_numbers[number%10]
        return stringToRet

def underThousandToString(number):
    if number < 100:
        return underHoundredToString(number)
    if number < 1000:
        stringToRet = basic_numbers[number/100] + ' hundred'
        if number%100 != 0:
            stringToRet = stringToRet + ' and ' + underHoundredToString(number%100)
        return stringToRet

def numberToString(number):
    if number < 1000:
        return underThousandToString(number)
    if number == 1000:
        return 'one ' + double_digit[1000]

def stringTotal(string_number):
    return len(string_number) - string_number.count(' ') - string_number.count('-')

print stringTotal(numberToString(342))
sum_num = 0
for i in range (1, 1001):
    number_string = numberToString(i)
    sum_num = sum_num + stringTotal(number_string)
    print number_string

print sum_num
