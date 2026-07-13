from scipy.io import loadmat
import numpy as np

mat = loadmat("C:\\Users\\Asus\\OneDrive\\Desktop\\Projects\\CWRU\\CWRU\\raw\\B007_1_123.mat")

de_key = [k for k in mat.keys() if k.endswith("_DE_time")][0]

signal = mat[de_key].flatten()

WINDOW_SIZE = 1024

windows = []

for i in range(0, len(signal) - WINDOW_SIZE, WINDOW_SIZE):
    window = signal[i:i + WINDOW_SIZE]
    windows.append(window)

windows = np.array(windows)

print("Shape of windows:", windows.shape)