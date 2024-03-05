
def prefixMatched(number):
    firstNumber = number[0]
    first_2_Numbers = number[:2]
    if firstNumber == "4" or firstNumber == '5' or firstNumber == '6' or first_2_Numbers == '37':
      return True
    else:
        return False


