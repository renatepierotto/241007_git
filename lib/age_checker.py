from datetime import datetime
import math


class AgeChecker():

    def __init__(self, birthdate) -> None:
        self.birthdate = birthdate

    def return_age(self):
        try:
            age = datetime.now() - datetime.strptime(self.birthdate, '%Y-%m-%d')
            return math.floor(age.days/365)
        except:
            raise Exception("Date is the incorrect format")
        

    def check_age(self):
        age = self.return_age()
        if age < 16:
            return f"Access Denied, you are {age} years old, wait another {16 - age} years"
        else:
            return "Access granted"
        