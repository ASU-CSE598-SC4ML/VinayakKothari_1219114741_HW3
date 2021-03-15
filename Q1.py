import itertools
import logging
import unittest
from CrypTen.test.multiprocess_test_case import MultiProcessTestCase, get_random_test_tensor

import crypten.communicator as comm
import crypten.mpc as mpc
import crypten
import torch
from crypten.common.tensor_types import is_int_tensor
from crypten.mpc.primitives import BinarySharedTensor, circuit


@mpc.run_multiprocess(world_size=1)
def Yao_Millionaires():
    # Bob's Value
    x = torch.Tensor([10])

    # Alice's Value
    y = torch.Tensor([5])

    enc_x = BinarySharedTensor(x)
    enc_y = BinarySharedTensor(y)

    print("Tensor for BOB" + str(enc_x._tensor))
    print("Tensor for Alice" + str(enc_y._tensor))

    direct_value = x.gt(y).long()
    enctypted = getattr(enc_x, "gt")(enc_y)

    print("Actual comparison value" + str(direct_value))
    print("Actual comparison value" + str(enctypted))


crypten.init()
torch.set_num_threads(1)
Yao_Millionaires()

