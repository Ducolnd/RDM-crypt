import cv2
import numpy as np

message = "Message to be encrypted"

img = cv2.imread("image.jpg")

def tobits(string):
    byte_array = []
    for character in string:
        bits = bin(ord(character))[2:]
        bits = '00000000'[len(bits):] + bits
        byte_array.append([int(b) for b in bits])
    return byte_array

byte_array = np.array(tobits(message))
byte_array = np.resize(byte_array, img.shape)

# For decryption
# print(byte_array.reshape(-1, 8)[:20])

conditions = np.where(img % 2 == 0)
conditions2 = np.where(byte_array == 1)
img[] += 1
print(img)

def encrypt(image, data):
    pass
