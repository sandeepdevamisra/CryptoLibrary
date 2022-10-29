import sys
sys.path.insert(0, '../DLP_HASH')
import dlp_hash


class MERKLE_DAMGARD:
    def __init__(self, msg):
        self.msg = msg
        self.length = len(self.msg)
        self.n_chunk = 16

    def generate(self):
        output = 0
        i=0
        while i<len(self.msg):
            temp_msg = int(self.msg[i:i+self.n_chunk], 2)    
            dlp_hash_obj = dlp_hash.DLP_HASH(temp_msg, output)
            output = int(dlp_hash_obj.generate(), 2)
            i+=self.n_chunk
        dlp_hash_obj = dlp_hash.DLP_HASH(self.length, output)
        output = dlp_hash_obj.generate()
        return output
    
if __name__=="__main__": 
    merkle_damgard = MERKLE_DAMGARD(sys.argv[1])
    print(merkle_damgard.generate())
    