from abc import ABC, abstractmethod
class Animal(ABC): 
    @abstractmethod
    def move(self): 
        pass
class Human(Animal): 
    def move(self):
        print("I can talk in any lanuage, walk and run with 1 pair of legs")
class Cat(Animal): 
    def move(self): 
        print("I can hiss and run")
class Dog(Animal): 
    def move(self): 
        print("I can back, fetch and eat")
class Lion(Animal): 
    def move(self): 
        print("I can fight and hunt")
H = Human()
H.move()

C = Cat()
C.move()

D = Dog()
D.move()

L = Lion()
L.move()



