import abc 
class PhysicalDevice:
    def __init__(self):
        self.node_name = self.get_node_name()
        self.share_list = set()
        
        self.begin()

    def begin(self):
        self.ask_node_state()
        self.ask_share_list()
        self.print_share_list_summary()

    def print_share_list_summary(self):
        print("Summary of shared list: \n\t{} could view content of {}\n".format(self.share_list, self.node_name))


    def remove_from_share_list(self, person):
        if person not in self.share_list:
            return 

        self.share_list.remove(person)

    @abc.abstractmethod
    def get_node_name(self):
        raise NotImplementedError

    def ask_share_list(self):
        person = input("who have access to {}? 'quit' to stop \n> ".format(self.node_name))
        while (person != "quit"):
            self.share_list.add(person)
            person = input("who have access to {}? 'quit' to stop \n> ".format(self.node_name))

        print("Summary: {} is able to access {}".format(self.share_list, self.node_name))


        