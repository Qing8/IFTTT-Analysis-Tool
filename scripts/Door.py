from enum import Enum
from PhysicalDevice import *

class DoorStateEnum(Enum):
    OPEN = 1
    CLOSE = 2
    
class Door(PhysicalDevice):
    def __init__(self):
        super().__init__()


    def get_node_name(self):
        print("================ Setting up Door ================")
        self.door_location = self.get_door_location() 
        node_name =  "[door at {}]".format(self.door_location)
        print("the node name is {}".format(node_name))
        return node_name

    def get_door_location(self):
        location = input("What is the location of the door?\n> ")
        return location


    def ask_node_state(self):
        print("================ Set the Slack node state ================")
        print("{} has the following state:".format(self.node_name))
        for s in DoorStateEnum:
            print(s.name)
        state = input("please choose one from above: \n> ")
        self.node_state = DoorStateEnum[state]
        print("Summary: You have set Node {} to state [{}].".format(self.node_name, self.node_state))