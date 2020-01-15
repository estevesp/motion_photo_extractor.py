import binascii

INPUT_JPG_FILE_NAME = "input.jpg"
OUTPUT_JPG_FILE_NAME = "output.jpg"
OUTPUT_MPG_FILE_NAME = "output.mpg"

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
