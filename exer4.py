from abc import ABC, abstractmethod

class Laptop(ABC):
    
    # A general method that will use the effects of this class
    
    def state(self):
        print('New')
        
    # abstract methods that will need to be redefined for each subclass
    
    @abstractmethod
    def screen(self):
        print('Some screen')
        
    @abstractmethod
    def keyboard(self):
        print('Some keyboard')

    @abstractmethod
    def touchpad(self):
        print('Some touchpad')
        
    @abstractmethod
    def webcam(self):
        print('Some webcam')
        
    @abstractmethod
    def ports(self):
        print('Some ports')
    
    @abstractmethod
    def dynamics(self):
        print('Some dynamics')


class HPLaptop(Laptop):
    
    def screen(self):
        print('HP integrated screen')
        
    def keyboard(self):
        print('HP keyboard')

    def touchpad(self):
        print('Synaptics touchpad')
        
    def webcam(self):
        print('HP webcam 2.0')
        
    def ports(self):
        print('HP reserved ports')
    
    def dynamics(self):
        print('HP cdax dynamics')