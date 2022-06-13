import binascii

file = open(input("PATH TO FILE: "), "rb").read()
offset = int("0xFF528", 16)
lenght = 4
hex_from_offset = binascii.hexlify(file[offset:offset + lenght])
print("HEX from offseg 0xFF528 is " + hex_from_offset.decode("utf-8"))