from os import urandom

def r():
    x = int.from_bytes(urandom(59), 'big')
    y = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    return (x & y & x >> 241).bit_count()

print(max([r() for _ in range(1000000000)]))
