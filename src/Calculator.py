def addition(a,b):
    return a+b
def subtract(a,b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self,a,b):
        self.result=addition(a,b)
        return self.result

    def subtract(self,a,b):
        self.result = subtract(a, b)
        return self.result