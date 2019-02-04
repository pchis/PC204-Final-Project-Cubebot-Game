import Tkinter as Tk
from operator import itemgetter

master = Tk.Tk()

turn = "black"
blackstonesplaced = []
whitestonesplaced = []


def taketurn(event):
    global turn
    global blackstonesplaced
    global whitestonesplaced
    #I couldn't figure out how to pass more variables with the event and I didn't want to turn this whole thing into a class for such a simple game.
    if(turn =="black"): #if it's black's turn do black turn
        clickedspace=((event.x-16)/20,(event.y-16)/20) #convert the clicked space to a place space. 16-25 should be 0. 26-34 should be 1. so subtract 16, divide by 10 always rounding down gives you the number you want.
        blackstonesplaced.append(clickedspace) #remember where all blackstones are placed
        w.create_oval(clickedspace[0]*20+16,clickedspace[1]*20+16,clickedspace[0]*20+24,clickedspace[1]*20+24,fill="black") #actuall draw the black stone
        #check if black wins
        sorted
        turn = "white"
        print "it's white's turn"
    else:                #if it's white's turn do white turn
        turn = "black"
        print "it's black's turn"

def callback(event):
    print "Clicked at:",event.x,event.y

def getem(event):
    print "blahblah"
#f = Tk.Frame(master, width=100, height=100)
w = Tk.Canvas(master, width=400, height=400)
w.pack()

def p():
    print "blahblah"
    
for x in range(20,381,20):
    w.create_line(x,20,x,380) #draw the horizontal lines
    w.create_line(20,x,380,x) #draw the vertical lines
w.create_line(20,380,381,380)
w.create_oval(16, 16, 24, 24, fill="black")
#w.create_line(0,100,200,0,fill="red",dash=(4,4))
#w.create_rectangle(50,25,150,75,fill="blue")

w.bind("<Button-1>",taketurn)
w.bind("<Button-2>",getem)
w.pack()

master.mainloop()
