"""Write a Python class to implement pow(x, n)."""
class PowerCalculator:
    def power(self, x, n):
        return x ** n

x = int(input("Enter x: "))
n = int(input("Enter n: "))
obj = PowerCalculator()
print(obj.power(x, n))