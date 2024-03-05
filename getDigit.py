

def getDigit(number):
    number = [int(digit) for digit in number]

    for i in range(len(number) - 1, -1, -1):  # Loop in reverse order
        if i % 2 == 0:
            number[i] *= 2

            if number[i] >= 10:
                first_digit = number[i] // 10
                second_digit = number[i] % 10
                number[i] = first_digit + second_digit

    return number[::2] 
print()
