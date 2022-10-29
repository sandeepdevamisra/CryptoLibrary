import sys
sys.path.insert(0, '../PRF')
import prf

class MAC:
    def __init__(self, msg, seed):
        self.msg = msg
        self.n_chunk = 8
        self.seed = seed
    
    def generate(self):
        if len(self.seed)<self.n_chunk:
            self.seed = self.seed.zfill(self.n_chunk)
        else:
            self.seed = self.seed[0:self.n_chunk]
        m_len = bin(len(self.msg)).replace('0b', '').zfill(self.n_chunk)
        prf_obj = prf.PRF(self.seed, m_len) 
        initial = prf_obj.generate()
        i=0
        while i<len(self.msg):
            temp_msg = self.msg[i:i+self.n_chunk].zfill(self.n_chunk)
            temp_result = ""
            for j in range(len(temp_msg)):
                temp_result += str(int(temp_msg[j]) ^ int(initial[j]))
            prf_obj = prf.PRF(self.seed, temp_result) 
            result = prf_obj.generate()
            initial = result
            i+=self.n_chunk
        return result

if __name__=="__main__":       
    mac = MAC(sys.argv[1], sys.argv[2])
    print(mac.generate())

