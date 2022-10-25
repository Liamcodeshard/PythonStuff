from room import Room
from characterTest import jacque

# Name rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining = Room("Dining room")

# Describe the named rooms
kitchen.SetDescription("A nice clean room with grandious facilities to cook up some nutritious goodness.")
ballroom.SetDescription("A huge, beautifully painted room with a smooth floor and tall ceilings.")
dining.SetDescription("An elegant, long room with a round table in the middle of it.")

# Link the rooms with cardinal directions
kitchen.LinkRoom(dining, "south")
ballroom.LinkRoom(dining, "east")
dining.LinkRoom(kitchen, "north")
dining.LinkRoom(ballroom, "west")

# # print all those deets
# kitchen.GetFullDetails()
# ballroom.GetFullDetails()
# dining.GetFullDetails()

currentRoom = kitchen

while True:
    print("\n")
    currentRoom.GetFullDetails()
    directionCommand = input("Please request a cardinal direction >>> ").lower()
    currentRoom = currentRoom.Move(directionCommand)
    fightWithWhat = input("What will you fight with?>>> ")
    jacque.Fight(fightWithWhat)