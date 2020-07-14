class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.las = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

class Manager(Employee):
    raise_amt = 1.20
    

dev_1 = Developer('Kevin', 'Frankhouser', 50000)
dev_2 = Manager('Bradley', 'Bach', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.email)
