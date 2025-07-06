
class brej:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    
    def calc(self):
        assert brej.add(10,2) == 12, "Addition yes"
        assert brej.add(22,3) == 2, "Addition no"
        

f = brej(10,2)
f.calc()
