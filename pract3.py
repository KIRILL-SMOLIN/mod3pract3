    # Самостоятельная работа по уроку "Рекурсия"
def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str_number[:1])
    if len(str_number) > 1:
        return first * int(get_multiplied_digits(int(str_number[1:])))
    else:
        return first


result = get_multiplied_digits(input('Введите любое целое число, а мы перемножим положительные цифры в нем!) '))
print('Перемножение цифр будет равно ', result)
