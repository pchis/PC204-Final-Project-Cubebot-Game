class Terrain(object):    
    """Terrain objects are things that take up space in the gamespace."""
    def __init__(self, x=10, y=10, width = 10, height = 10, shape = "rectangle", quality = "unpassable", color = 'black'):
        self.x = x #x and y are the object's top left corner
        self.y = y
        self.width = width
        self.height = height
        self.shape=shape
        self.color = color #the color of the terrain
        self.space = {} #the space the object takes up
        self.quality = quality #quality is whether the object is passable, unpassable, lethal, etc.
        if self.shape=="rectangle":
            for c1 in range(self.x, self.x+self.width):
                for c2 in range(self.y,self.y+self.height):
                    self.space[(c1,c2)] = self.quality  
#the creature class 
class Creature(Terrain):
    """a terrain that moves/updates itself"""
    def __init__(self, x=0, y=0, space=[], character=0,AI="basic"):
        self.x = x
        self.y = y
        self.space = space
        self.xvelocity = 0
        self.yvelocity = 0
        self.AI = AI
        self.falling = 0
    def nextturn(self):
        """updates any environmental effects on the creature and returns where it will be in the upcoming turn. The master runner will decide if there are any collisions"""
        return
    def fall(self): #checks to see if the creature should fall
        return

class Character(Creature):
    """A creature with different AI. Also if it dies you lose"""
    def nexturn(self,gamespace):
        if (self.falling==0):
            self.fall()
        else:
            self.yvelocity = 
        self.xvelocity=0
        
            
    
    

    
def blah():
    print "blah"
