from tkinter import *
import random

# VARIABLES
turns = ["Player 1", "Player 2"] # plan to allow players to insert names before turns. Hard code player 1 and 2 for now
turn = random.choice(turns) # chooses a random first turn

# functions

def action():
    btn1.config(bg='red')
        

# INITIAL 
app = Tk()

# ----- APP WIDGETS -----

# label indicates who's turn it is
turnLabel = Label(app, text=turn + "'s Turn")
turnLabel.config(font=('Helvetica, 24'))
turnLabel.grid(column=1, row=0, pady=30)

# GRID
#  [1,2,3]
#  [4,5,6]
#  [7,8,9]

# ROW 1
btn1 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove", command=action)
btn2 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
btn3 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")

# ROW 2
btn4 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
btn5 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
btn6 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")

# ROW 3
btn7 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
btn8 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")
btn9 = Button(app, text=" ", font=('Helvetica, 20'), height=5, width=10, bg='white', borderwidth=4, relief="groove")

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




# APP DETAILS
app.title('TIC-TAC-Toe')
app.geometry('600x700')

app.mainloop()