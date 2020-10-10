import cv2
import numpy as np
import binascii

password = 42

img = cv2.imread("outfile.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

flat_img = img.ravel()

#np.random.seed(password)

#order = np.arange(img.shape[0] * img.shape[1] * img.shape[2])
#np.random.shuffle(order)

#data = np.zeros(img.shape).ravel()
#for index, actualindex in np.ndenumerate(order):
    #data[actualindex] = flat_img[index]

#print(data.reshape(img.shape))
bits = np.copy(img)

bits[bits % 2 == 1] = 0
bits[(bits % 2 == 0) & (bits > 0)] = 1

byte_array = bits.reshape(-1, 8).tolist()
by = []

for byte in byte_array[:100]:
    byte = [str(i) for i in byte]
    b = ''.join(byte)

    by.append(b)
print(by)
print(''.join([chr(int(x, 2)) for x in by]))
