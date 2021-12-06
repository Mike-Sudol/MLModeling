import torch.nn as nn
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Hello")
print(torch.cuda.is_available)
