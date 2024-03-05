#Return sum of odd place digits in number

def sum_odd_place_digits(number):
    
    number = [int(digit) for digit in number]
  
    
    odd = 0
    if len(number) % 2 == 0:
     for n in number[1::2]:
      odd += n
    else:
      for n in number[::2]:
        odd += n
    return odd

