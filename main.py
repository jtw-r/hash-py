# Three requirements:
# 1) Speed (reasonably fast, but not break neck speed for security reasons)
# 2) The avalanche effect (if any characters are changed, the message is entirely different)
# 3) Avoid hash collisions

#
# Steps:
#   Take a string as an input
#   Break that string into 4 parts of equal length
#
#

import math


def break_string(_input, _chunks):
    _temp_array = []
    _chunk_len = math.ceil(len(_input) / _chunks)
    for i in range(0, _chunks):
        _curr_pos = i * _chunk_len
        _temp_array.append(_input[_curr_pos:(_curr_pos + _chunk_len)])
    return _temp_array


def find_divisor(_num, _min=4, _max=10):
    _chosen = 4
    for _d in range(_min, _max+1):
        if math.remainder(_num, _d) == 0:
            _chosen = _d
    print(_chosen)
    return _chosen


full_input = input("Enter the string you wish to be hashed") or "The Quick Brown Fox Jumped Over The Lazy Dog"

_input_length = len(full_input)
broken_input = break_string(full_input, find_divisor(_input_length))
print(broken_input)

