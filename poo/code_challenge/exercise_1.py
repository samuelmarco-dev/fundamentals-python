class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def power(self):
        return self.a ** self.b

num_a, num_b = int(input()), int(input())
calc = Calculator(num_a, num_b)
print(calc.add())
