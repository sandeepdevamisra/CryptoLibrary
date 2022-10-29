import sys
sys.path.insert(0, '../DLP_HASH')
import dlp_hash

class HMAC:
    def __init__(self, msg, seed):
        self.msg = msg
        self.n_chunk = 16
        self.seed = seed.zfill(self.n_chunk)
        self.ipad = "01011100"
        self.opad = "00110110"

    def generate(self):

        padded_ipad = self.ipad
        padded_opad = self.opad

        for i in range(8, self.n_chunk):
            padded_ipad += self.ipad[i-8]

        for i in range(8, self.n_chunk):
            padded_opad += self.opad[i-8]

        xor_bits = ""
        for i in range(self.n_chunk):
            xor_bits += str(int(self.seed[i]) ^ int(padded_ipad[i]))

        dlp_hash_obj = dlp_hash.DLP_HASH(int(xor_bits, 2), 0)
        output = int(dlp_hash_obj.generate(),2)

        i=0
        while i<len(self.msg):
            temp_msg = int(self.msg[i:i+self.n_chunk], 2)    
            dlp_hash_obj = dlp_hash.DLP_HASH(temp_msg, output)
            output = int(dlp_hash_obj.generate(),2)
            i+=self.n_chunk

        dlp_hash_obj = dlp_hash.DLP_HASH(len(self.msg), output)
        output = int(dlp_hash_obj.generate(),2)

        xor_bits = ""
        for i in range(self.n_chunk):
            xor_bits += str(int(self.seed[i]) ^ int(padded_opad[i]))

        dlp_hash_obj = dlp_hash.DLP_HASH(int(xor_bits,2), 0)
        output2 = int(dlp_hash_obj.generate(),2)

        dlp_hash_obj = dlp_hash.DLP_HASH(output, output2)
        output = dlp_hash_obj.generate()

        return output

if __name__=="__main__": 
    hmac = HMAC(sys.argv[1], sys.argv[2])
    print(hmac.generate())