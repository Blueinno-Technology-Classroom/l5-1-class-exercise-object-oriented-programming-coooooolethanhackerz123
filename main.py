##################################################
'''
Q1a: 
'''
p1 = Point(9,2)
##################################################
'''
Q1b: 
'''
p1 = Point(27,2)
##################################################
'''
Q2:
'''
class Name:
    def _init_(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

##################################################
'''
Q3:
'''
class Name:
    def _init_(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def normal_order():
        return self.first_name+' '+self.last_name

    
    def revers_order():
        return self.last_name+' '+self.first_name
    
person = Name('a','b')
person.normal_order()

person.reverse_order()

##################################################
'''
Q4:
'''

class Name:
    def _init_(self,name,balance):
        self.name = name
        self.balance = balance


##################################################
'''
Q5:
'''
class BankAccount:
    def _init_(self,name,balance):
        self.name = name
        self.balance = 0

    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit: ${amount}, \tLatest balance: ${self.balance}")

    def withdraw(self,amount):
        slef.balance -= amount
        print(f"Wthdraw: ${amount}, \tLatest balance: $ {self.balance}")
##################################################
'''
Q6:
'''
class BankAccount:
    def _init_(self,name,balance):
        self.name = name
        self.balance = 0
        slef.transaction_fee = 2.0
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit: ${amount}, \tLatest balance: ${self.balance}")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"Wthdraw: ${amount}, \tLatest balance: $ {self.balance}")
        if (self.blance < amount + self.transaction_fee):
                print("YOU ARE POOR")
        else:
            self.balance -= amount + self.transaction_fee
            print(f"withdraw: ${amount},|tlatest balance: ${self.balance}")

##################################################
'''
Q7:
'''
class BankAccount:
    def _init_(self,name,balance):
        self.name = name
        self.balance = 0
        slef.transaction_fee = 2.0
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit: ${amount}, \tLatest balance: ${self.balance}")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"Wthdraw: ${amount}, \tLatest balance: $ {self.balance}")
        if (self.blance < amount + self.transaction_fee):
                print("YOU ARE POOR")
        else:
            self.balance -= amount + self.transaction_fee
            print(f"withdraw: ${amount},|tlatest balance: ${self.balance}")
ben = BankAccount('ben')
ben.deposit(80.00)

hal = BankAccount('hal')
hal.deposit(hal,20.00)
##################################################
