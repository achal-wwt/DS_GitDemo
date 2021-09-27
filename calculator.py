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
        # TODO:- Add your code in the below function
        # check for divide by zero error, using assert statements
        # implement the division operation
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("[ERROR] Can't divide by zero!")
