from tkinter import *
import os
import sys

#-----------------------WINDOW--------------------------------------------------

window = Tk()
window.geometry("400x270")
window.title("UltimateTicTacToe")
window.resizable(False, False)

turn = True

#-----------------------CLOSE PROGRAM-------------------------------------------

def exit():
    window.destroy()

#-----------------------REFRESH PROGRAM-----------------------------------------

def new():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#-----------------------BLOCK BUTTONS-------------------------------------------

def changeState(button):
    if (button['state'] == NORMAL):
        button['state'] = DISABLED
    else:
        button['state'] = DISABLED

def stateWin():
    button1["state"] = DISABLED
    button2["state"] = DISABLED
    button3["state"] = DISABLED
    button4["state"] = DISABLED
    button5["state"] = DISABLED
    button6["state"] = DISABLED
    button7["state"] = DISABLED
    button8["state"] = DISABLED
    button9["state"] = DISABLED

#-----------------------PLAYERS TURN--------------------------------------------

def player(button):
    global turn
    if turn == True:
        button.config(text="X")
    else:
        button.config(text="O")
    turn = not turn
    win()

#-----------------------BUTTONS-------------------------------------------------

button1 = Button(window, text = " ", state=NORMAL , width = 10, height = 5, command = lambda: [player(button1), changeState(button1)])
button1.grid(row = 2, column = 0)
button2 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button2), changeState(button2)])
button2.grid(row = 2, column = 1)
button3 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button3), changeState(button3)])
button3.grid(row = 2, column = 2)
button4 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button4), changeState(button4)])
button4.grid(row = 3, column = 0)
button5 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button5), changeState(button5)])
button5.grid(row = 3, column = 1)
button6 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button6), changeState(button6)])
button6.grid(row = 3, column = 2)
button7 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button7), changeState(button7)])
button7.grid(row = 4, column = 0)
button8 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button8), changeState(button8)])
button8.grid(row = 4, column = 1)
button9 = Button(window, text = " ", state=NORMAL, width = 10, height = 5, command = lambda: [player(button9), changeState(button9)])
button9.grid(row = 4, column = 2)
buttonNewGame = Button(window, text = "New Game", width = 20, height = 5, command = new)
buttonNewGame.grid(row = 2, column = 4)
buttonExit = Button(window, text = "Exit The Game", width = 20, height = 5, command = exit)
buttonExit.grid(row = 3, column = 4)
text = Label(window, text = " ")
text.grid(row = 4, column = 4)

#-----------------------WIN-----------------------------------------------------

def win():
    global newwindow
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        text["text"] = "Player One Wins!"
        stateWin()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          text["text"] = "Player Two Wins!"
          stateWin()
    elif (button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
         button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
         button7["text"] != " " and button8["text"] != " " and button9["text"] != " "):
         text["text"] = "Tie!"
         stateWin()

#-----------------------EXIT BUTTON---------------------------------------------

def exit():
    newwindow.destroy()

window.mainloop()
