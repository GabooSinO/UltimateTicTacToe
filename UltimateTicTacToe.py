from tkinter import *

window = Tk()
window.geometry("400x270")
window.title("UltimateTicTacToe")

turn = True

def player1(button):
    global turn
    if turn == True:
        button.config(text="X")
    else:
        button.config(text="O")
    turn = not turn

button1 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button1))
button1.grid(row = 2, column = 0)
button2 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button2))
button2.grid(row = 2, column = 1)
button3 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button3))
button3.grid(row = 2, column = 2)
button4 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button4))
button4.grid(row = 3, column = 0)
button5 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button5))
button5.grid(row = 3, column = 1)
button6 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button6))
button6.grid(row = 3, column = 2)
button7 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button7))
button7.grid(row = 4, column = 0)
button8 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button8))
button8.grid(row = 4, column = 1)
button9 = Button(window, text = " ", width = 10, height = 5, command = lambda: player1(button9))
button9.grid(row = 4, column = 2)
buttonNewGame = Button(window, text = "New Game", width = 20, height = 5)
buttonNewGame.grid(row = 2, column = 4)
buttonExit = Button(window, text = "Exit The Game", width = 20, height = 5)
buttonExit.grid(row = 3, column = 4)

if button1.cget() == "X":
    print("Si")

window.mainloop()
