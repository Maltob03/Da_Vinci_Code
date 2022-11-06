#TODO: 
#Tradurre in italiano

import cryptocode
from getpass import getpass
from PIL import Image

str_encoded=0


def crypto():
    password = getpass("Inserisci la password da cifrare ")
    print()
    passkey = getpass("inserisci la chiave ")
    print()
    str_encoded = cryptocode.encrypt(password, passkey)
    y=input("Seleziona un opzione: \n 1. Visualizza stringa codificata \n 2. Salva stringa codificata su un file \n 3. Codifica stringa all'interno di una foto")
    if(y=="1"):
        print(str_encoded)
    elif(y=="2"):
        try:
            with open('crypted password.txt', 'w') as f:
                f.write(str_encoded)
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
    elif(y=="3"):
        encode(str_encoded)
    
    



def decrypto():
    keypass= getpass("inserisci la chiave ")
    str_encoded = getpass("inserisci la stringa codificata ")
    print()
    str_decoded = cryptocode.decrypt(str_encoded, keypass)
    print(str_decoded)
    input()


# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):

        # list of binary codes
        # of given data
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):

    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# Encode data into image
def encode(str_encoded):
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    k=input("Do you want to use the string encoded y/n")
    if(k=="y"):
        data = str_encoded
    else:
        data = input("Enter data to be encoded : ")
    
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = input("Enter the name of new image(with extension) : ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

# Decode the data in the image
def decode():
    img = input("Enter image name(with extension) : ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data





x=input("Benvenuto, scegli una tra le seguenti opzioni \n 1. Cripta la tua password\n 2. Decodifica una stringa codificata \n 3. Codifica all'interno di un immagine una stringa \n 4. Decodifica da un immagine la stringa segreta \n")
if(x=="1"):
    crypto()
elif(x=="2"):
    decrypto()
elif(x=="3"):
    encode(str_encoded)
elif(x=="4"):
    print("Decoded Word :  " + decode())

