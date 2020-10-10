import cv2
import numpy as np
import binascii
import sys

password = int(input("Password to encrypt data (seed): "))
n_read = int(input("How many characters should be read? ")) # How many characters should be read

img = cv2.imread(sys.argv[1])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

flat_img = img.ravel()

np.random.seed(password)

order = np.arange(img.shape[0] * img.shape[1] * img.shape[2])
np.random.shuffle(order)

#print("shape", order.shape, flat_img.shape)

data = np.zeros(img.shape).ravel()
for index, actualindex in np.ndenumerate(order):
    data[actualindex] = flat_img[index]

data.reshape(img.shape)
bits = data

bits[bits % 2 == 1] = 0
bits[(bits % 2 == 0) & (bits > 0)] = 1


byte_array = bits.reshape(-1, 8).tolist()
message = []

for byte in byte_array[:n_read]:
    byte = [str(int(i)) for i in byte]
    b = ''.join(byte)
    
    b = int(b, 2)
    message.append(b.to_bytes((b.bit_length() + 7) // 8, "big").decode(errors="ignore"))

print("".join(message))
print(message)
