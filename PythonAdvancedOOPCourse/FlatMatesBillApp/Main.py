from OOPLearning.PythonAdvancedOOPCourse.FlatMatesBillApp.flat import Bill, Flatmate, House
from OOPLearning.PythonAdvancedOOPCourse.FlatMatesBillApp.pdf_printout import PDFPrintout, FileSharer

house_name = input("What is the name or address of the house? \n>> ")
bill_amount = float(input("How much is the total bill? \n>>£"))
bill_period = input("What is the bill period? I.E. December 2020 \n>> ")
number_of_housemates = int(input("How many Housemates are there to share the bill?\n>> "))

# flatmate_1_name = input(f"What is the name of the first housemate? \n>> ")
# flatmate_1_days_in_house = float(input(f"How many days did {flatmate_1_name} stay in the house? \n>> "))
#
# flatmate_2_name = input("What is the name of the next housemate? \n>> ")
# flatmate_2_days_in_house = float(input(f"How many days did {flatmate_2_name} stay in the house? \n>> "))
flatmate_list = []
bill_object = Bill(bill_amount, bill_period)

for i in range(0,number_of_housemates):
    name = input(f"What is the name of housemate #{i+1}? \n>> ")
    days_in_house = float(input(f"How many days did {name} stay in the house? \n>> "))
    flatmate_list.append(Flatmate(name, days_in_house))

house1 = House(house_name, flatmate_list, bill_object)

for house_mates in flatmate_list:
    print(house_mates.name, house_mates.pays(bill_object, house1))


bill_printout: PDFPrintout = PDFPrintout(fileName=bill_period + " bill.pdf")
bill_printout.generate(bill_object,house1)

file_sharer = FileSharer(filepath=bill_printout.fileName)
print(file_sharer.share())

# flatmate1 = Flatmate(flatmate_1_name, flatmate_1_days_in_house)
# flatmate2 = Flatmate(flatmate_2_name, flatmate_2_days_in_house)



# print(flatmate1.name, flatmate1.pays(bill_object, house1))
# print(flatmate2.name, flatmate2.pays(bill_object, house1))
