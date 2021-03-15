import crypten
import torch
from crypten.mpc.primitives import BinarySharedTensor

class Bob:
    x = None
    m1 =4
    m2=5
    def __init__(self):
        self.x = torch.tensor(4)
        print("Tensor Threshold of Bob"+ str(self.x))
        print("valye of Bob"+ str(self.m1))
        print("valye of Bob"+ str(self.m2))

class ALice:
    x = None
    def __init__(self):
        self.x = torch.tensor(6)
        print("Tensor valye of Alice"+ str(self.x))

    def coupon_value(self , value):
        print("Value  of Coupon returned" + str(value))
class circuit:

    def compute(self):
        alice = ALice()
        bob = Bob()
        b1 = BinarySharedTensor(alice.x)
        b2 = BinarySharedTensor(bob.x)
        m1 =bob.m1
        m2 = bob.m2
        value = b1.gt(b2)
        value = value.get_plain_text()
        alice.coupon_value(value * m1 +(1-value) *m2)

crypten.init()
c=circuit()
c.compute()

