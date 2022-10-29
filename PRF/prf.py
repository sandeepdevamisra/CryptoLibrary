import sys

class PRF:
    def __init__(self, seed, inp_bit):
        self.seed = seed
        self.inp_bit = inp_bit
        self.n = len(seed)
        self.g = 7781
        self.p = 40529
    
    def l_func(self, x):
        return 2*x

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
    
    def generate(self):
        for i in self.inp_bit:
            output = self.g_func()
            if int(i) == 0:
                output = output[:len(output)//2]
            else:
                output = output[len(output)//2:]
            self.seed = output
        return output
    
    def print(self):
        print(self.generate())

if __name__=="__main__":       
    prf = PRF(sys.argv[1], sys.argv[2])
    prf.print()
