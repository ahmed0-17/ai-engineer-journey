from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod   
    def turn_on(self):
        pass

class Fan(Appliance):

    def turn_on(self):
        print("Fan is spinning")    



class WashingMachine(Appliance):

    def turn_on(self):
        print("Washing machine is starting")            




fan=Fan()
fan.turn_on()        
washing_machine=WashingMachine()
washing_machine.turn_on()