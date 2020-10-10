from PIL import Image
import cv2
import numpy as np
import sys

message = input("Message to be encrypted: ")
password = int(input("Password to encrypt data (seed): "))

np.random.seed(password)

img = cv2.imread(sys.argv[1])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def tobits(string):
    byte_array = []
    for character in string:
        bits = bin(ord(character))[2:]
        bits = '00000000'[len(bits):] + bits

        bits = bits.replace("0", "2")
        bits = bits.replace("1", "3")

        byte_array.append([int(b) for b in bits])
    return byte_array

byte_array = np.array(tobits(message))
byte_array.resize(img.shape)


np.random.shuffle(byte_array.ravel()) # Shuffle bits 
byte_array.resize(img.shape)

# For decryption
# print(byte_array.reshape(-1, 8)[:20])

# Even: 1
# Uneven: 0
img[(img % 2 == 0) & (byte_array == 2)] += 1 # Make even number uneven
img[(img % 2 == 1) & (byte_array == 3)] += 1 # Make uneven number evenn

# Error checking
img[img > 255] -= 2

im = Image.fromarray(img)
im.save(sys.argv[2])
