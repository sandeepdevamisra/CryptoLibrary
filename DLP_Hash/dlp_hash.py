import sys
class DLP_HASH:
    def __init__(self, x1, x2):
        self.p = 130367
        self.q = 65183
        self.g = 2
        self.h = pow(self.g, 42, self.p)
        self.x1 = int(x1)
        self.x2 = int(x2)
    
    def generate(self):
        res = pow(self.h, self.x1, self.p) * pow(self.g, self.x2, self.p) % self.p
        return bin(res).replace('0b', '')

if __name__=="__main__": 
    dlp_hash = DLP_HASH(sys.argv[1], sys.argv[2])
    print(dlp_hash.generate())
    
