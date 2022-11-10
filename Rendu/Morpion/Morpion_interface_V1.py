#---Import librairies----
from tkinter import Tk, Canvas
import random
from tkinter.messagebox import askyesno, showerror, showinfo, showwarning

#Create grid board
game = [[0,1,2],[0,1,2],[0,1,2]]


#Create graphic interface
def gril(c="black"):
    '''
    Create configuration line size in black color 
    '''
    canvas.create_line((100,0),(100,300), width=3, fill=c)
    canvas.create_line((200,0),(200,300), width=3, fill=c)
    canvas.create_line((0,100),(300,100), width=3, fill=c)
    canvas.create_line((0,200),(300,200), width=3, fill=c)

"""Function that defines the coordinates of points"""
def pions():

	"""	Iteration of the loop, which must be executed with the same results"""
	for x in range(3):
		for y in range(3):
			xx = x * 100
			yy = y * 100

			"""Define the length of the shapes"""
			A = (xx+20,yy+20)
			B = (xx+80,yy+80)
			C = (xx+20,yy+80)
			D = (xx+80,yy+20)

			""" Creation of oval , define color 'blue' """
			if game[x][y] == 1:
				canvas.create_oval(A,B,fill="blue")

				""" Creation of the cross, define color 'red', configuration pf the dimension"""
			if game[x][y] == 2:
				canvas.create_line(A,B,fill="red",width=10)
				canvas.create_line(C,D,fill="red",width=10)

"""Function who detect win """
def DetectWin():
	for i in [1,2]:
		for x in range(3):
			if game[x][0] == game[x][1] == game[x][2] == i : return i
		for y in range(3):
			if game[0][y] == game[1][y] == game[2][y] == i : return i
		if game[0][0] == game[1][1] == game[2][2] == i : return i
		if game[0][2] == game[1][1] == game[2][0] == i : return i
	return 0

"""Function who searches if the boxes are empty"""
def SearchEmptyCases():
	L = []
	for x in range(3):
		for y in range(3):

			if game[x][y] == 0:
				L.append((x,y))   #adds items to the list L 

	if len(L) == 0 : return False 
	
	else :
		i = random.randint(0,len(L)-1) #returns the number of elements L
		return L[i]


#program

"""Function prog, wich refers to the gril function"""
def prog():
	gril()

"""Function affiche that remove all forms"""
def affiche():
	canvas.delete("all")
	 #Refers to the functions gril and pion"""
	gril()
	pions()
	
'''Function callback who displays the windows , to play again or leave'''
def callback():
	if askyesno('Fin du jeu', 'Voulez-vous rejouer ?'):
		print("")

	else :
		showerror('Fin du jeu', 'Au revoir !')
		window.destroy()

"""Function click whi creates the click through the argument event"""
def click(event):
	global game
	affiche()
	x = event.x // 100
	y = event.y // 100

	if DetectWin() != 0:
		game = [[0,0,0],[0,0,0],[0,0,0]]
		affiche()
		return

	if game[x][y] != 0 : return

#human player 
	game[x][y] = 1 
	pions()
	if DetectWin() == 1:
		gril("blue")
		callback()
		

#computer player 
	calcul = SearchEmptyCases()
	if calcul != False:
		x,y = calcul
		game[x][y] = 2
		pions()
		if DetectWin() == 2:
			gril("red")
			callback()
			return

#Initiation of the interface 
"launching interface"
window = Tk()
window.title("Morpion")
"""Configuration window size"""
window_size = 300
window.geometry(str(window_size) + "x" + str(window_size))
canvas = Canvas(window, width=window_size, height=window_size, borderwidth=0, highlightthickness=0, bg="lightgray")
"""launch of the librairie canvas"""
canvas.pack()
window.after(100, prog)
window.bind("<Button-1>", click)
window.mainloop()  