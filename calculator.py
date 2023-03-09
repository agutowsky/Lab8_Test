class four_function_calc:
    def __init__(self):
        self.total = 0
    
    def add(self, arg1, arg2):
        self.total = arg1 + arg2
        return self.total
    
    def sub(self, arg1, arg2):
        self.total = arg1 - arg2
        return self.total
    
    def mult(self, arg1, arg2):
        self.total = arg1 * arg2
        return self.total
    
    def div(self, arg1, arg2):
        self.total = arg1 / arg2
        return self.total