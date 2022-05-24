# 2a - Composition

class Person:
   
    def __init__(self):
        arm_left = Arm('left')
        arm_right = Arm('right')
        self.arms = [arm_left.location, arm_right.location]

class Arm:
    
    def __init__(self, location):
        self.location = location
        
person = Person()
print(person.arms)


# 2b - Aggregation

class CellPhone:
    
    def __init__(self, screens):
        self.screens = screens

class Screen:
    
    def __init__(self, resolution):
        self.resolution = resolution
        
screen_small = Screen('resolution 480x800')
screen_medium = Screen('resolution 720x1280')
screen_massive = Screen('resolution 1440x2560')
screens = [screen_small.resolution, screen_medium.resolution, screen_massive.resolution]

cellphone = CellPhone(screens)
print(cellphone.screens)