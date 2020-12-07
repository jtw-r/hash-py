def xor(_a, _b):
    return (_a and not _b) or (not _a and _b)


def str2bin(_input, _type="utf-8"):
    a_byte_array = bytearray(_input, _type)

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_representation)

    return ''.join(format(i, 'b') for i in bytearray(_input, encoding ='utf-8'))


def bin2str(_input, _type="utf-8"):
    str_data = ' '
    for i in range(0, len(_input), 7):
        # slicing the bin_data from index range [0, 6]
        # and storing it in temp_data
        temp_data = _input[i:i + 7]

        # passing temp_data in BinarytoDecimal() function
        # to get decimal value of corresponding temp_data
        decimal_data = int(temp_data, 2)

        # Deccoding the decimal value returned by
        # BinarytoDecimal() function, using chr()
        # function which return the string corresponding
        # character for given ASCII value, and store it
        # in str_data
        str_data = str_data + chr(decimal_data)

    return str_data


print(str2bin(input("1: ")))

print(bin2str(input("2: ")))

1000001100001010000111000100
1000001100001010000111000100