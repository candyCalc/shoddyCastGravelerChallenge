# You could just use porbability to generate an answer instantly, but that's no fun,
# so I limited myself. Only python, only built-in modules, and all rolls must be generated and checked.

from os import urandom

# n = number of rolls (each containing 231d4)
n = 1000000000

def roll():
    # creates 59 random bytes (472 bits, closest multiple of 8 to 2*231, the extra 10 will be discarded later)
    bitset = int.from_bytes(urandom(59), 'big')
    # 231 consecutive 1s
    bit_mask = 0b111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    # & the bitset and mask to get the first 231 bits, shift the bitset right 241 times (extra 10 are discarded here) to get the last 231 bits, then & the two together
    # result is that we have 231 pairs of 2 bits being &'d. It has a 1/4 change of coming out as a 1
    result = (bitset & bit_mask) & (bitset >> 241)
    # return how many 1's are in the result
    return result.bit_count()

rolls = [roll() for _ in range(n)]
print('max roll:', max(rolls),'\nmin roll:', min(rolls))
