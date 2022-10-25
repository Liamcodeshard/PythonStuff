class Item:
    def __init__(self):
        self.name = None
        self.description = None

    def SetName(self, itemName):
        self.name = itemName

    def GetName(self):
        return self.name

    def SetDescription(self, itemDescription):
        self.description = itemDescription

    def GetDescription(self):
        return self.description

    def GetFullDetails(self):
        print(f"The {self.name}:")
        print(f"Is {self.description}")



