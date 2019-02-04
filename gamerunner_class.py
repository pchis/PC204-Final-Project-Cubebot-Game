import time
import Tkinter as Tk
import creature_and_character_classes as CC
class Gamerunner(object):
    def __init__(self, Width=800, Height=800):
        
        #import gamedrawer_class as GD
        self.creatures = [] #array of creatures
        self.terrain = [] #all the individual terrain objects. Everytime the character looks to move it checks all the spaces occupied by terrain
        self.gamespace = {} #the pixels in the gamespace and what their qualities are
        #self.game = GD.Gamedrawer()
        self.root = Tk.Tk()
        self.canvaswidth=Width
        self.canvasheight=Height
        self.gamewidth=0
        self.gameheight=0
        self.can = Tk.Canvas(self.root, width=self.canvaswidth, height=self.canvasheight)
        self.level=1

        self.loadlevel()
        self.x=10
        self.y=10
    def loadlevel(self):
        #first remove the last level
        self.creatures = []
        self.terrain = []
        self.gamespace = {}
        #self.can.destroy(
        if self.level==1:
            self.gamewidth=800
            self.gameheight=800
            self.terrain.append(CC.Terrain(0,self.gameheight-40,self.gamewidth,40,"rectangle","unpassable","black")) #last three variables are unnecessary
            self.terrain.append(CC.Terrain(0,0,20,self.gameheight))
            self.terrain.append(CC.Terrain(self.gamewidth-40,self.gameheight-60,40,60))
            for ter in self.terrain:
                self.drawterrain(ter)
                self.updategamespace(ter)
            self.can.pack()
        if self.level==2:
            return

    def drawterrain(self,PoT): #creates the terrain in the level for the first time. PoT stands for piece of terrain
        if PoT.shape=="rectangle":
            self.can.create_rectangle(PoT.x,PoT.y,PoT.x+PoT.width,PoT.y+PoT.height,fill=PoT.color)
            self.can.pack()

    def updategamespace(self,terrain): #receives a terrain and updates the master gamespace        
        for pixel in terrain.space.keys():
            self.gamespace[pixel] = terrain.space[pixel]
                              
    def updateterrain(self): #goes through the list of terrain and updates their location
        return

    def updatecreatures(self): #calculates where the creatures will go and puts them there
        return
                                
    def rungame(self):
        print("blah")
        self.can.create_oval(self.x,self.y,self.x+10,self.y+10)
        self.x+=10
        self.y+=10
        self.updatecreatures()
        self.root.after(1000,self.rungame)
        
    def go(self):
        #print ("blah7")
        self.rungame()
        #print ("blah5")
        self.root.mainloop()
        #print ("blah6")
