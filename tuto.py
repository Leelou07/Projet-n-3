from os import name
from tkinter import *
from turtle import position

class Mywindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.mylist = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.canvas = Canvas(self, width=500, height=500, background='white')
        ligne2 = self.canvas.create_line(166, 0, 166, 500)
        ligne2 = self.canvas.create_line(332, 0, 332, 500)
        ligne3 = self.canvas.create_line(0, 166, 500, 166)
        ligne3 = self.canvas.create_line(0, 342, 500, 342)
        self.canvas.pack()



        self.canvas.bind('<Button-1>', self.clic)
        

    def clic(self, event):
        X = event.x 
        Y = event.y
        self.position2(X, Y)

    def position(self, x, y):
        if(y <= 166 and x<= 166):
            self.mylist[0][0] = 1
            self.create_rond(2, 164)
        elif(y <= 166 and (x <= 332 and x > 166)):
            self.mylist[0][1] = 1
            self.create_rond(168, 330)
        elif(y <= 166 and (x <= 498 and x > 332)):
            self.mylist[0][1] = 1
            self.create_rond(334, 496)



    def position2(self, x, y):
        p = 166
        j = 0
        a = 0
        t = 166
        while(p <= 496):
            while(j <= 496):
                if((y <= p and y > a) and (x <= p and x > j)):
                #self.mylist[0][0] = 1
                    print(j)
                    print(p)
                    self.create_rond(j+2, p-2)
                    break
                j += 166
                t += 166
            j = 0; t = 0
            p += 166
            a += 166
            
            print(p)



    def create_rond(self, x, y):
        ligne = self.canvas.create_oval(x, 2, y, 160, width=2)

    def create_croix(self, x, y):
        ligne = self.canvas.create_line(0, 0, x, y)
        ligne = self.canvas.create_line(0, y, x, 0)
        self.canvas.pack()

window = Mywindow()

window.mainloop()