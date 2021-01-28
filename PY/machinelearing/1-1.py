import torch
import torchvision
import numpy as np

np_date = np.arange(6).reshape((2, 3))
torch_date = torch.from_numpy(np_date)
tensor2array = torch_date.numpy()
print(
    '\nnumpy', np_date,
    '\ntorch', torch_date,
    '\ntensor2array', tensor2array,
)
# print(torch.__version__)
# print(torch.cuda.is_available())
# a = torch.tensor([123, 456])
# print(a)
