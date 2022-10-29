import sys
sys.path.insert(0, '../PRF')
import prf

class CPA:

    def __init__(self, msg, seed, counter):
        self.n_chunk = 16
        self.seed = seed.zfill(self.n_chunk)
        self.msg = msg 
        self.counter = counter 

    def generate(self):
        result = ""
        i=0
        while i<len(self.msg):
            self.counter = int(self.counter,2)
            self.counter = self.counter+1
            self.counter = bin(self.counter).replace('0b', '')
            temp_msg = self.msg[i:i+self.n_chunk]
            temp_result = ""
            prf_obj = prf.PRF(self.seed, self.counter) 
            prf_out = prf_obj.generate() 
            for j in range(len(temp_msg)):
                temp_result += str(int(temp_msg[j]) ^ int(prf_out[j]))
            result += temp_result
            i+=self.n_chunk
        return result
    
if __name__=="__main__":      
    cpa = CPA(sys.argv[1], sys.argv[2], sys.argv[3])
    print(cpa.generate())


