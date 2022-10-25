import array
import random


class Room:
    def __init__(self, roomName):
        self.name = roomName
        self.description = None
        self.linkedRooms = {}
        self.windows = 0

    def SetDescription(self, roomDescription):
        self.description = roomDescription

    def GetDescription(self):
        return self.description

    def Describe(self):
        print(self.description)

    def SetName(self,roomName):
        self.name = roomName

    def GetName(self):
        return self.name

    def PrintName(self):
        print(self.name)

    def GetFullDetails(self):
        print("------------------------------")
        print("The " + self.name + ":")
        print(self.description)
        for direction in self.linkedRooms:
            room = self.linkedRooms[direction]
            print("The " + room.GetName() + " is " + direction + " from here")

    def LinkRoom(self, roomToLink, direction):
        self.linkedRooms[direction] = roomToLink

    def Move(self, direction):
        if direction in self.linkedRooms:
            return self.linkedRooms[direction]
        else:
            print("You can't go that way.")
            return self

    def GiveWindow(self, numberOfWindows):
        self.windows = numberOfWindows

    def CheckWindow(self):
        return self.windows

    def CheckWeather(self):
        weather = ["sunny", "cloudy", "raining", "thundering"]
        return weather[random.randint(0,5)]

    def LookOutWindow(self):
        print(f"You look out of the window and see it is {self.CheckWeather()}")
