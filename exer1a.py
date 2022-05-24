from exer1 import Animals

class Human:
    """
    Human class, should have eat, sleep, study, work
    """
    def __init__(self, name):
        self.name = name
    def eat(self):
        print('Bread is the head of everything')
    def sleep(self):
        print('It is time to sleep when no one is waiting')
    def study(self):
        print('Knowledge is power')
    def work(self):
        print('There is no fruit without work')

class Centaur(Animals, Human):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
    def __init__(self, name, type, colour):
        Human.__init__(self, name)
        Animals.__init__(self, type, colour)
        
    def unbridled_rage(self):
        print('just come to me!')
        
        
centaur = Centaur('Bucentaurus', 'mythical creature', 'brown')
print(centaur.name, centaur.colour, centaur.type)
centaur.unbridled_rage()
