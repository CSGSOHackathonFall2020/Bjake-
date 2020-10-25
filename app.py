from tkinter import *
import random

# Two dimensional grid

gameGrid = [
    ['','',''],
    ['','',''],
    ['','','']
]

turns = 0 # when turns = 9, we need to check for a winner

# functions

def checkWinner():
    global gameGrid, winColor
    
	#top horizontal
    if gameGrid[0][0] == gameGrid[0][1] and gameGrid[0][0] == gameGrid[0][2]:
        if gameGrid[0][0] == '' or gameGrid[0][1] == '' or gameGrid[0][2] == '':
            print('pass1')
            pass
        else:
            winColor = gameGrid[0][0]
            restartGame()
            print('winner1')
            return
            
    #mid horizontal
    if gameGrid[1][0] == gameGrid[1][1] and gameGrid[1][0] == gameGrid[1][2]:
        if gameGrid[1][0] == '' or gameGrid[1][1] == '' or gameGrid[1][2] == '':
            print('pass2')
            pass
        else:
            winColor = gameGrid[1][0]
            restartGame()
            print('winner2')
            return
            
    #bottom horizontal
    if gameGrid[2][0] == gameGrid[2][1] and gameGrid[2][0] == gameGrid[2][2]:
        if gameGrid[2][0] == '' or gameGrid[2][1] == '' or gameGrid[2][2] == '':
            print('pass3')
            pass
        else:
            winColor = gameGrid[2][0]
            restartGame()
            print('winner3')
            return
            
    #left vertical
    if gameGrid[0][0] == gameGrid[1][0] and gameGrid[0][0] == gameGrid[2][0]:
        if gameGrid[0][0] == '' or gameGrid[1][0] == '' or gameGrid[2][0] == '':
            print('pass4')
            pass
        else:
            winColor = gameGrid[0][0]
            restartGame()
            print('winner4')
            return
            
    #mid vertical
    if gameGrid[0][1] == gameGrid[1][1] and gameGrid[0][1] == gameGrid[2][1]:
        if gameGrid[0][1] == '' or gameGrid[1][1] == '' or gameGrid[2][1] == '':
            print('pass5')
            pass
        else:
            winColor = gameGrid[0][1]
            restartGame()
            print('winner5')
            return
            
    #right vertical
    if gameGrid[0][2] == gameGrid[1][2] and gameGrid[0][2] == gameGrid[2][2]:
        if gameGrid[0][2] == '' or gameGrid[1][2] == '' or gameGrid[2][2] == '':
            print('pass6')
            pass
        else:
            winColor = gameGrid[0][2]
            restartGame()
            print('winner6')
            return
            
     #vert start top left
    if gameGrid[0][0] == gameGrid[1][1] and gameGrid[0][0] == gameGrid[2][2]:
        if gameGrid[0][0] == '' or gameGrid[1][1] == '' or gameGrid[2][2] == '':
            print('pass7')
            pass
        else:
            winColor = gameGrid[0][0]
            restartGame()
            print('winner7')
            return
            
    #vert bottom left
    if gameGrid[2][0] == gameGrid[1][1] and gameGrid[2][0] == gameGrid[0][2]:
        if gameGrid[2][0] == '' or gameGrid[1][1] == '' or gameGrid[0][2] == '':
            print('pass8')
            pass
        else:
            restartGame()
            print('winner8')
            return
            
def action(button):
    global turn, turns, players
    if turn == players[0] and button['bg'] == 'white': # check whos turn and if button is empty
        button.config(bg='red')

        row = int(button.grid_info()['row'])
        column = int(button.grid_info()['column'])
        gameGrid[row-1][column] = "red"

        checkWinner()

        turn = players[1]
        turnLabel.config(text=players[1] + "'s turn")
        turns += 1
    elif turn == players[1] and button['bg'] == 'white': # check whos turn and if button is empty
        button.config(bg='blue')

        row = int(button.grid_info()['row'])
        column = int(button.grid_info()['column'])
        gameGrid[row-1][column] = "blue"

        checkWinner()

        turn = players[0]
        turnLabel.config(text=players[0] + "'s turn")
        turns += 1
    else:
        pass # don't do anything until a blank button is clicked
        

# INITIAL 
app = Tk()

# ----- APP WIDGETS -----

def setup():
    global turn, players

    playerOneLabel.destroy()
    playerOneEntry.destroy()
    playerTwoEntry.destroy()
    playerTwoLabel.destroy()
    setupLabel.destroy()
    playButton.destroy()

    players = [] # plan to allow players to insert names before turns. Hard code player 1 and 2 for now

    players.append(playerOneName.get())
    players.append(playerTwoName.get())
    turn = random.choice(players) # chooses a random first turn


def play():
    global turnLabel, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9

    setup()

    app.geometry('600x700')
    # label indicates who's turn it is
    turnLabel = Label(app, text=turn + "'s Turn")
    turnLabel.config(font=('Helvetica, 24'))
    turnLabel.grid(column=1, row=0, pady=30)

    # GRID
    #  [1,2,3]
    #  [4,5,6]
    #  [7,8,9]

    # ROW 1
    btn1 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn1.configure(command=lambda: action(btn1))
    btn2 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn2.configure(command=lambda: action(btn2))
    btn3 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn3.configure(command=lambda: action(btn3))

    # ROW 2
    btn4 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn4.configure(command=lambda: action(btn4))
    btn5 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn5.configure(command=lambda: action(btn5))
    btn6 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn6.configure(command=lambda: action(btn6))

    # ROW 3
    btn7 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn7.configure(command=lambda: action(btn7))
    btn8 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn8.configure(command=lambda: action(btn8))
    btn9 = Button(app, font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
    btn9.configure(command=lambda: action(btn9))

    # add buttons to app
    btn1.grid(column=0, row=1, padx=12)
    btn2.grid(column=1, row=1)
    btn3.grid(column=2, row=1)
    btn4.grid(column=0, row=2)
    btn5.grid(column=1, row=2)
    btn6.grid(column=2, row=2)
    btn7.grid(column=0, row=3)
    btn8.grid(column=1, row=3)
    btn9.grid(column=2, row=3)

def startScreen():
    global setupLabel, playerOneLabel, playerOneEntry, playerTwoLabel, playerTwoEntry, playerOneName, playerTwoName, playButton

    app.geometry('300x400')

    setupLabel = Label(app, text="TIC-TAC-TOE")
    setupLabel.config(font=('Helvetica, 24'))
    setupLabel.grid(column=1, row=0, pady=30)

    playerOneName = StringVar()
    playerOneLabel = Label(app, text="Player One Name", font=('Helvetica', 20))
    playerOneLabel.grid(column=1, row=1)
    playerOneEntry = Entry(app, textvariable=playerOneName, font=('Helvetica', 16), fg='red', borderwidth=4, relief="groove")
    playerOneEntry.grid(column=1, row=2, padx=20)

    playerTwoName = StringVar()
    playerTwoLabel = Label(app, text="Player Two Name", font=('Helvetica', 20))
    playerTwoLabel.grid(column=1, row=3)
    playerTwoEntry = Entry(app, textvariable=playerTwoName, font=('Helvetica', 16), fg='blue', borderwidth=4, relief="groove")
    playerTwoEntry.grid(column=1, row=4, padx=20)

    playButton = Button(app, text="PLAY", font=('Helvetica, 20'), fg="white", bg='green', borderwidth=4, relief="groove", width=15)
    playButton.configure(command=lambda: play())
    playButton.grid(column=1, row=5, pady=20)
    
def restartGame():
    global setupLabelrestart, resetLabel,playerTwoLabel, resetButton

    clearGrid()
    
    app.geometry('275x275')

    setupLabelrestart = Label(app, text= winColor + " won the game")
    setupLabelrestart.config(font=('Helvetica, 24'))
    setupLabelrestart.grid(column=1, row=0, pady=30)

    resetLabel = StringVar()
    resetLabel = Label(app, text="Reset game?", font=('Helvetica', 20))
    resetLabel.grid(column=1, row=1)

    resetButton = Button(app, text="Restart", font=('Helvetica, 20'), fg="white", bg='green', borderwidth=4, relief="groove", width=15)
    resetButton.configure(command=lambda: play())
    resetButton.grid(column=1, row=5, pady=20)

def clearGrid():
	btn1.destroy()
	btn2.destroy()
	btn3.destroy()
	btn4.destroy()
	btn5.destroy()
	btn6.destroy()
	btn7.destroy()
	btn8.destroy()
	btn9.destroy()

	turnLabel = ''
	gameGrid[0][0] = ''
	gameGrid[0][1] = ''
	gameGrid[0][2] = ''
	gameGrid[1][0] = ''
	gameGrid[1][1] = ''
	gameGrid[1][2] = ''
	gameGrid[2][0] = ''
	gameGrid[2][1] = ''
	gameGrid[2][2] = ''



# APP DETAILS
app.title('TIC-TAC-TOE')

startScreen()


app.mainloop()
