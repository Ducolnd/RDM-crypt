from PIL import Image
import cv2
import numpy as np

message = "Message to be encrypted"
password = 42

np.random.seed(password)

img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def tobits(string):
    byte_array = []
    for character in string:
        bits = bin(ord(character))[2:]
        bits = '00000000'[len(bits):] + bits
        byte_array.append([int(b) for b in bits])
    return byte_array

byte_array = np.array(tobits(message))
byte_array.resize(img.shape)
#np.random.shuffle(byte_array) # Shuffle bits 

# For decryption
# print(byte_array.reshape(-1, 8)[:20])

# Even: 1
# Uneven: 0
img[(img % 2 == 0) & (byte_array == 0)] += 1 # Make even number uneven
img[(img % 2 == 1) & (byte_array == 1)] += 1 # Make uneven number evenn

# Error checking
img[img > 255] -= 2

im = Image.fromarray(img)
im.save("outfile.png")
