#Program4: Mapping

class Mapping:
    def __init__(self):
        pass

    def operate(self, nums):
        res = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
        for num in nums:
            for i in range(1,10):
                if num % i == 0:
                    res[i] = res[i]+1 
        return res