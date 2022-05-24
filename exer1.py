# Exercise 1

class Animals:
    """
    Parent class, should have eat, sleep
    """
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour
    def eat(self):
        print('I am well fed')
    def sleep(self):
        print('I am allowed to sleep')
        
class Snake(Animals):
    def __init__(self, type, colour):
        super().__init__(type, colour) 
    def slithering(self):
        print('I can crawl anywhere')
        
class Monkey(Animals):
    def __init__(self, type, colour):
        super().__init__(type, colour) 
    def climb(self):
        print('I can climb trees')
        
class Hippopotamus(Animals):
    def __init__(self, type, colour):
        super().__init__(type, colour) 
    def swim(self):
        print('I can swim well')
        
class Cheetah(Animals):
    def __init__(self, type, colour):
        super().__init__(type, colour) 
    def run(self):
        print('I am running the fastest')
        
class Elephant(Animals):
    def __init__(self, type, colour):
        super().__init__(type, colour) 
    def power(self):
        print('I am the strongest')
        
        
snake = Snake('reptile', 'green')
print(snake.colour, snake.type)
snake.slithering()
print(isinstance(snake, Animals))

monkey = Monkey('mammal', 'brown')
print(monkey.colour, monkey.type)
monkey.climb()
print(isinstance(monkey, Animals))

hippopotamus = Hippopotamus('mammal', 'grey')
print(hippopotamus.colour, hippopotamus.type)
hippopotamus.swim()
print(isinstance(hippopotamus, Animals))

cheetah = Cheetah('mammal', 'yellow')
print(cheetah.colour, cheetah.type)
cheetah.run()
print(isinstance(cheetah, Animals))

elephant = Elephant('mammal', 'white')
print(elephant.colour, elephant.type)
elephant.power()
print(isinstance(elephant, Animals))

        
        