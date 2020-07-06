import random
import time
from tkinter import Tk , Button , DISABLED

def show_symbol(x,y):
    # Declared again so the symbol wont go after first try
    global first
    global previousx , previousy
    #button[x,y]['text'] is accessing all buttons at same time along with its text in it
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        # store x and y in previous as we need them to match with same value
        previousx = x
        previousy = y
        first = False # if true it will take a new symbol as first value and wont work
    elif previousx != x or previousy != y:   # to prevent user from pressing same card  
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']: # if card is not same.
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else: 
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

win = Tk()
win.title('Match The Cards!')
win.resizable(width=False , height=False)
first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }

#Inbuilt images Of Python
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        # Used Lambda to prevent KeyError! x,y will store loop range to prevent 0,0 looping
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8)
        button.grid(column = x , row = y)
        buttons[x,y] = button  # store all button created in variable
        button_symbols[x,y] = symbols.pop()

win.mainloop()
