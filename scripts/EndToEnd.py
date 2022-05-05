from __future__ import annotations
import abc

EVERYONE = "everyone"

class EndToEnd:
    def __init__(self):
        super().__init__()
        self.send_to = set()
        self.receive_from = set()
        self.from_time = -1
        self.to_time = 25
        self.specify_send_to = False
        self.specify_receive_from = False 

    def add_sent_to(self, person):
        self.specify_send_to = True 
        self.send_to.add(person)
    
    def remove_send_to(self, person):
        if person not in self.send_to:
            return 
        self.send_to.remove(person)
        if len(self.send_to) == 0:
            self.specify_send_to = False 

    def add_receive_from(self, person):
        self.specify_receive_from = True 
        self.receive_from.add(person)

    def remove_receive_from(self, person):
        if person not in self.receive_from:
            return 
        self.receive_from.remove(person)
        if len(self.receive_from) == 0:
            self.specify_receive_from = False 

    def set_from_time(self, from_time):
        self.from_time = from_time 

    def set_to_time(self, to_time):
        self.to_time = to_time

    # @abc.abstractmethod
    def is_same_account(self, other:type[EndToEnd]):
        if not isinstance(other, EndToEnd):
            return False 
        return self.account_name == other.account_name
        
    def point_to(self, other):
        if self.specify_receive_from and self.specify_send_to:
            return self.point_to_time(other) and (self.point_to_receive_from(other) or self.point_to_send_to(other))
        if self.specify_receive_from:
            return self.point_to_time(other) and self.point_to_receive_from(other)
        elif self.specify_send_to:
            return  self.point_to_time(other) and self.point_to_send_to(other)
        else:
            return  self.point_to_time(other)

    def point_to_send_to(self, other: type[EndToEnd]):
        if not isinstance(other, EndToEnd) or not self.is_same_account(other):
            return False
        if EVERYONE in other.send_to or len(self.send_to.intersection(other.send_to)) != 0:
            return True 
        return False 
    
    def point_to_receive_from(self, other:type[EndToEnd]):
        if not isinstance(other, EndToEnd) or not self.is_same_account(other):
            return False
        if EVERYONE in other.receive_from or len(self.receive_from.intersection(other.receive_from)) != 0:
            return True 
        return False 

    def point_to_time(self, other:type[EndToEnd]):
        if not isinstance(other, EndToEnd) or not self.is_same_account(other):
            return False
        return (max(self.from_time, other.from_time) <= min(self.to_time, other.to_time))
