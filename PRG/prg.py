import sys

class PRG:
    def __init__(self, seed):
        self.seed = seed
        self.n = len(seed)
        self.g = 7781
        self.p = 40529
    
    def l_func(self, x):
        return pow((x-1),2)
        
    def h_func(self, s1, s2):
        x = int(s1, 2)
        mod_exp = bin(pow(self.g, x, self.p))
        mod_exp = mod_exp.replace('0b', '').zfill(self.n)
        hard_bit = 0
        for i in range(len(s1)):
            temp = int(s1[i]) & int(s2[i])
            hard_bit = (hard_bit ^ temp)%2
        result_tup = (mod_exp, s2, str(hard_bit))
        return "".join(result_tup)
    
    def g_func(self):
        string = self.seed
        result = ""
        for i in range(self.l_func(self.n)):
            if len(string) == 1:
                s1 = string
                s2 = string
            else:
                s1 = string[:len(string)//2]
                s2 = string[len(string)//2:]
            string = self.h_func(s1, s2)
            result += string[-1]
            string = string[:-1]
        return result
    
    def print(self):
        print(self.g_func())

prg = PRG(sys.argv[1])
prg.print()