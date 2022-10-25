class Character:

    # Create character
    def __init__(self, charName, charDescription):
        self.name = charName
        self.description = charDescription
        self.conversation = None

    # Describe character
    def Describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what they will say when spoken to
    def SetConvo(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def Talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(self.name + " doesn't want to talk to you.")

    # Fight with this character
    def Fight(self, combatItem):
        print(self.name + " doesn't want to fight with you.")
        return True
class Enemy(Character):

    def __init__(self, charName, charDescription):
        super().__init__(charName, charDescription)
        self.weakness = None
        self.attack = None

    def SetWeakness(self, weakness):
        self.weakness = weakness

    def GetWeakness(self):
        return self.weakness

    def SetAttack(self, attackWeapon):
        self.attack = attackWeapon

    def GetAttack(self):
        return self.attack

    def Fight(self, attackWeapon):
        if attackWeapon == self.weakness:
            print(f"You DESTROY {self.name} with the {attackWeapon}")
            return True
        else:
            print(f"{self.name} crushes you. PUSSYYY")
            return False

class Companion(Enemy):
    def __init__(self, charName, charDescription):
        super().__init__(charName, charDescription)
        self.animalType = None

    def SetAnimalType(self, animal):
        self.animalType = animal

    def GetAnimalType(self):
        return self.animalType

    def Describe(self):
        print(f"{self.name} the {self.GetAnimalType()} is here!")
        print(self.description)