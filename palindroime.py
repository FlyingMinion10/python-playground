# SOLUCION PITERA DE PEPE

class Solution(object):
    def isPalindrome(self, x):
        self.numero = str(x)
        self.numero_invertido = self.numero[::-1]
        if self.numero == self.numero_invertido:
            return True
        else:
            return False  
        
# SOLUCION GOD JF
class Solution(object):
    def isPalindrome(self, x):
        self.rw = []
        self.rs = ""
        self.w = str(x)
        for l in self.w:
            self.rw.append(l)
        self.rw.reverse()
        for i in self.rw:
            self.rs += i
        if self.rs == self.w: 
            return True 
        else: 
            return False
        