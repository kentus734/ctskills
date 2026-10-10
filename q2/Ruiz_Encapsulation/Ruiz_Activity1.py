class GameCharacter:
    def __init__(self, username):
        self.username = username

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

class Vehicle:
    def __init__(self, engineCode):
        self._engineCode = engineCode

class Student:
    def __init__(self, schoolName):
        self.schoolName = schoolName

class VotingSystem:
    def __init__ (self, voterID):
        self.__voterId = voterID

# Testing

'''
game = GameCharacter("Kentus123")
bank = BankAccount(5000)
vehicle = Vehicle("ENG-2026")
student = Student("PSHS")
voting = VotingSystem("VOTER-001")
'''

# 1. Public attribute
# print(game.username)

# 2. Private attribute
# print(bank.__balance)  #  Gives error because its private*

# 3. Protected attribute
#print(vehicle._engineCode)

# 4. Public attribute
#print(student.schoolName)

# 5. Private attribute
# print(voting.__voterId)  # Gives error because its private*

