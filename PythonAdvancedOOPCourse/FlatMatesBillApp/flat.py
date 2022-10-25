class Bill:
    """
    Object that contains data about a bill - Period and Amount
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about the flatmates - name, days in house and how much they are to pay
    """

    def __init__(self, name, daysInHouse):
        self.name = name
        self.daysInHouse = daysInHouse

    def pays(self, bill, house):
        daily_charge = (bill.amount/house.totalDaysInHouse)
        individual_monthly_charge = daily_charge * self.daysInHouse
        self.the_maths = f"daily charge of (£{round(daily_charge,2)} x by the days in the house ({self.daysInHouse})"
        return individual_monthly_charge


class House:
    """
    contains data on the house object - how many housemates etc
    """
    def __init__(self, address, listOfFlatmates, bill):
        self.address = address
        self.listOfFlatmates = listOfFlatmates
        daysInHouse = 0
        for person in listOfFlatmates:
            daysInHouse += person.daysInHouse
        self.totalDaysInHouse = daysInHouse
        self.billAmount = bill.amount
