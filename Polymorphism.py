class animal():
    def __init__(self, name= 'yeezy'):
        self.name = name
        
 #must do self instead of name otherwise returns just memory location       
 #self allows you to pass parameters from animal class so do not need to declare name again  
    def introduceMyself(self): 
        print(f'hello my name is {self.name}')

class Cat(animal):
    def sound(self):
        print('meooow')
        
class Dog(animal):
    def sound(self):
        print('woooof')

class Snake(animal):
    def sound(self):
        print('hissss')

def animalSound(animal):
    aimal.sound()

animal = Cat()    
print(animal.introduceMyself())
