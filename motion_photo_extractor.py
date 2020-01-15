import binascii

INPUT_JPG_FILE_NAME = "20200115_123802.jpg"
OUTPUT_JPG_FILE_NAME = "output.jpg"
OUTPUT_MPG_FILE_NAME = "output.mpg"
SCALE = 16 ## equals to hexadecimal
NUM_OF_BITS = 8


with open(INPUT_JPG_FILE_NAME, 'rb') as JPG_FILE:
    BINARY_FILE_CONTENT = JPG_FILE.read()
JPG_FILE.close()

HEX_FILE_CONTENT = binascii.hexlify(BINARY_FILE_CONTENT)
HEX_ARRAY = HEX_FILE_CONTENT.upper().split("4D6F74696F6E50686F746F5F44617461")

DECODED_JPG = binascii.unhexlify(HEX_ARRAY[0])
DECODED_MPG = binascii.unhexlify(HEX_ARRAY[1])

with open(OUTPUT_JPG_FILE_NAME, "wb") as JPG_FILE:
    JPG_FILE.write(DECODED_JPG)

with open(OUTPUT_MPG_FILE_NAME, "wb") as MPG_FILE:
    MPG_FILE.write(DECODED_MPG)

BIN_JPG_FILE = bin(int(HEX_ARRAY[0], SCALE))[2:].zfill(NUM_OF_BITS)
BIN_MPG_FILE = bin(int(HEX_ARRAY[1], SCALE))[2:].zfill(NUM_OF_BITS)

with open("TEST.JPG", "wb") as JPG_FILE:
    JPG_FILE.write(BIN_JPG_FILE)

