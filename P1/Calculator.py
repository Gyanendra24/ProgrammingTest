#Program1: Calculator

class Calculator:
    def __init__(self, a, b, op):
        self.a = float(a)
        self.b = float(b)
        self.op = op
        
    def operation(self):
        try:
            if self.op == '+':
                return self.a + self.b
            elif self.op == '-':
                return self.a - self.b
            elif self.op == '*':
                return self.a * self.b
            elif self.op == '/':
                return self.a / self.b
            else: 
                return 'Unknown operation'
        except ArithmeticError:
            return 'Divide by Zero'