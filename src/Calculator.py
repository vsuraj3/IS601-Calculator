def addition(a,b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtract(a,b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c

def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    d = round(c, 9)
    return d

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
    
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result
    
    def div(self, a, b):
        self.result = division(a, b)
        return self.result
    def div(self, a, b):
        self.result = division(a, b)
        return self.result
