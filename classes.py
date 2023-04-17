class Car:
    
    def __init__(self, carname, year):
        self.carname = carname
        self.year = year
        
    def calc(self, mileage):
        return 10 * mileage
    
    def __str__(self):
        return f"{self.carname} - {self.year}"
    
    
c1 = Car("Audi", 2022)
print(c1)

print(c1.calc(200))