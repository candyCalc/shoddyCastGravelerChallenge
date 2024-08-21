from os import urandom

def roll():
    bitset = int.from_bytes(urandom(59), 'big')
    bit_slicer = 3450873173395281893717377931138512726225554486085193277581262111899647
    return (bitset & bit_slicer & bitset >> 241).bit_count()

print(max([roll() for _ in range(1000000000)]))
