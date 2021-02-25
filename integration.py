class AddOrMult():
    
    def __init__(self, add_func, mult_func):
        super().__init__()
        self.add = add_func
        self.mult = mult_func

    def do(self, a, b, c):
        if c == 'add':
            return self.add(a, b)
        if c == 'mult':
            return self.mult(a, b)
        return None
