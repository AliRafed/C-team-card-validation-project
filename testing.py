from tkinter import *
import Card_validation



window = Tk()
window.title('Card validator')
window.geometry('500x500')


card_number = Entry(window, width=60)
card_number.pack(pady = 10)


Main_button = Button(window,text='validate Card',command= Card_validation.Card_validation(card_number))
Main_button.pack()


v = Card_validation.Card_validation(card_number)

answar = Label(window, textvariable= Main_button)
Pack()

window.mainloop()