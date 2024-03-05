







def Card_validation(number):

 import getsize

 import prefixMatched

 import getDigit

 import getPrefix

 import sumOfDoubleEvenPlace

 import sumOfOddPlace

 import isvalid

 
 number = card_number.get()
 

      
      
 if number.startswith('-') and number[1:].isnumeric():
      
       return "invalid invalid input, card number cannot be a negative value"
     
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
                  k=1
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
               
               return f"The credit card number is {number}\n and the prefix {prefix}\n it is a valid {card_type}."
               
               
               
            else:
            
               return "card is invalid"
               
            

         else:
            return "Card type is invalid please enter a card number with a valid prefix"
            
      
      
            
      elif d < 13 or d > 16:
         
         return "input must be between 13 and 16 digits"
         
 else:
      return "invalid input please enter Numeric valuse "
   









from tkinter import *
import Card_validation






window = Tk()
window.title('Card validator')
window.geometry('500x500')


card_number = Entry(window, width=60)
card_number.pack(pady = 10)



Main_button = Button(window,text='validate Card',command= Card_validation)
Main_button.pack()

#answar =Label(window,textvariable= v)
#answar.pack()



window.mainloop()


