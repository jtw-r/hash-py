def xor(_a, _b):
    return (_a and not _b) or (not _a and _b)


_input = input("enter anything")

a_byte_array = bytearray(_input, 'utf-8')

byte_list = ''

for byte in a_byte_array:
    binary_representation = bin(byte)
    # byte_list.append(binary_representation)
    byte_list += binary_representation


print(byte_list)
