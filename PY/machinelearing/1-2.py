import torch
import numpy as np

date = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(date)
date = np.array(date)
print(
    '\nnumpy', date.dot(date),
    # '\ntorch', tensor.dot(tensor)
)
