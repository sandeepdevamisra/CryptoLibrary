import sys
sys.path.insert(0, '../MAC')
sys.path.insert(0, '../CPA')
import mac
import cpa

class CCA:
    def __init__(self, inp_msg, seed1, seed2, counter):
        self.inp_msg = inp_msg
        self.msg = self.inp_msg.split(",")[0]
        if len(self.inp_msg.split(",")) == 2:
            self.tag = self.inp_msg.split(",")[1]
        self.seed1 = seed1
        self.seed2 = seed2
        self.counter = counter
    
    def encrypt(self):
        result = ""
        cpa_obj = cpa.CPA(self.msg, self.seed1, self.counter) 
        cpa_out = cpa_obj.generate() 
        result += cpa_out + ","

        mac_obj = mac.MAC(cpa_out, self.seed2) 
        mac_out = mac_obj.generate() 
        result += mac_out
        return result

    def decrypt(self):
        mac_obj = mac.MAC(self.msg, self.seed2)
        mac_out = mac_obj.generate()
        if mac_out == self.tag:
            cpa_obj = cpa.CPA(self.msg, self.seed1, self.counter) 
            cpa_out = cpa_obj.generate()
            return cpa_out
        else:
            return ""

    def handler(self):
        if len(self.inp_msg.split(",")) == 2:
            return self.decrypt()
        elif len(self.inp_msg.split(",")) == 1:
            return self.encrypt()
        else:
            return ""

    
if __name__=="__main__":      
    cca = CCA(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(cca.handler())
  




