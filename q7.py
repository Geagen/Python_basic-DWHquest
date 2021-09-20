class Animal:
        __my_voice=''
        def voice(self):
                pass


def get_child_val():
                print(len(Animal.__subclasses__()))    

class Dog(Animal):
        
        def __init__(self):
                Animal.__my_voice='woof, woof'

        def voice(self):
                print(Animal.__my_voice)

class Cow(Animal):
        cow_voice=' '
        def __init__(self):
                self.cow_voice='moo, moo'
        def voice(self):
                print(self.cow_voice)

class Customer(Animal):
        
        def __init__(self):
                Animal.__my_voice='Хорошо, но надо переделать'
        def voice(self):
                print (Animal.__my_voice)


hDog= Dog()
hDog.voice()
hCow= Cow()
hCow.voice()
hCust= Customer()
hCust.voice()

get_child_val()
