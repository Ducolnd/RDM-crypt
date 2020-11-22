from flask import Flask, request, Response, send_file
import numpy as np
import cv2
from PIL import Image
import io


app = Flask(__name__)


@app.route('/stego', methods=['POST'])
def test():
    r = request

    #get message and password from headers
    message = request.headers.get('RDM-message')
    password = request.headers.get('RDM-password')

    np.random.seed(password)

    nparr = np.fromstring(r.data, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # start copy pasta duco code
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
    #end copy pasta duco code

    #create image from array
    im = Image.fromarray(img)

    # create file-object in memory
    file_object = io.BytesIO()

    # write PNG in file-object
    img.save(file_object, 'jpg')

    # move to beginning of file so `send_file()` it will read from start    
    file_object.seek(0)

    #return image
    return send_file(file_object, mimetype='image/PNG')


# start flask app
app.run(host="0.0.0.0", port=8080)