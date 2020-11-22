import torch
from torch.autograd import variable

tensor = torch.FloatTensor([[1, 2], [3, 4]])
# variable = variable(tensor, requires_grad=True)
print(tensor)
# print(variable)
