#Program3 Odd Series2

class OddSeries2:
    def __init__(self):
        pass
    
    def generate_odd_series(self, a):
        if a % 2 == 0:
            a = a - 1
        return [2*i + 1 for i in range(a)]