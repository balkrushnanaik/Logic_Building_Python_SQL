class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
c1 = Calculator()
print(c1.add(10, 5))
print(c1.subtract(10, 5))
print(c1.multiply(10, 5))
print(c1.divide(10, 5))