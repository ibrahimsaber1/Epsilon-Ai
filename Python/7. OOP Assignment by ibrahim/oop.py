# > # Dear Epsilon Students, 
# > # The More you practice The better You'll Be.
# ### Instructions: 
# - Make sure that you understand this topics before you start.
# - If you found something hard to do, try and try then google it and finally ask someone. 
# - You can divide this work into daily tasks so that you do not feel pressure.
# - After you finish, go to model answer and rate yourself. 
# - If you find something ambiguous, Try to make a hypothesis to solve a problem. 
# ### Question classification: 
# - Green is level 1 
# - Orange is level 2 
# - Red is level 3 
# <center> Let's start 💪 </center> 
## <p style="color:green;">Q.01 Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.</p>

# Answer here 
import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)
    
l1 = Line((1, 2), (4, 6))
l2 = Line((2, 2), (5, 4))
l1.coor1
## <p style="color:green;">Q.02 Fill in the class to get the volume and surface area of Cylinder</p>
# Answer here 
# A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r²
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.h = height
        self.r = radius
        pass
        
    def volume(self):
        return 3.14 * (self.r **2) * self.h
    
    def surface_area(self):
        return  (2*3.14 * self.r * self.h) + (2*3.14 * (self.r **2) )
    
    
c1 = Cylinder(5, 3)
c1.surface_area()
## <p style="color:green;">Q.03 Create a child class Bus that will inherit all of the variables and methods of the Vehicle class</p>
# > Given:

# Answer here 
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, color):
        Vehicle.__init__(self, name, max_speed, mileage)
        self.color = color
b1 = Bus("B770", 170, 80, "blue")
b1.color

# <center> Thank's for your effort ❤️ </center> 