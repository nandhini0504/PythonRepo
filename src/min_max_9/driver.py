import numpy as np
from src.min_max_9.utils import minimum
row=int(input("Enter the no of rows:"))
columns=int(input("Enter the no of columns:"))
new_array=([])
new_array =np.array([input("Elements:").split() for i in range(row)],int)
minimum(new_array)