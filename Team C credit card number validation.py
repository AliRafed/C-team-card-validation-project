
import getsize

import prefixMatched

import getDigit

import getPrefix

import sumOfDoubleEvenPlace

import sumOfOddPlace

import isvalid

 




while True:
   number = input("enter the card number ")
   
   if number.startswith('-') and number[1:].isnumeric():
      
      print("invalid invalid input, card number cannot be a negative value")
   
   elif number.isnumeric():
      
      d = getsize.getsize(number)
      
      
      
      if  13 <= d and d <= 16:
         
         Prefix_match = prefixMatched.prefixMatched(number)
         
         if Prefix_match == True:
            number_digits = getDigit.getDigit(number)
            
            sum_of_even = sumOfDoubleEvenPlace.sumOfDoubleEvenPlace(number_digits)
            
            sum_of_odd = sumOfOddPlace.sum_odd_place_digits(number)


            Card_validation_value = sum_of_odd + sum_of_even

            Card_validation = isvalid.isvalid(Card_validation_value)
            
            if Card_validation == True:
               if number.startswith('4'):
                  k= 1
                  card_type = "Visa card"
               elif number.startswith('5'):
                  k= 1
                  card_type = "MasterCard"
               elif number.startswith('37'):
                  k= 2
                  card_type = "American Express"
               elif number.startswith('6'):
                  k= 1
                  card_type = "Discover card"
               prefix = getPrefix.getPrefix(number, k)
               
               print(f"The credit card number is {number}\n and the prefix {prefix}\n it is a valid {card_type}.")
               
               
               break
            else:
            
               print("card is invalid")
               break
            

         else:
            print("Card type is invalid please enter a card number with a valid prefix")
      
      
      
      
            
      elif d < 13 or d > 16:
         print("input must be between 13 and 16 digits ") 
   else:
      print("invalid input please enter Numeric valuse ")


