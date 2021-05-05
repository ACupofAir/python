def pow_mod(base, pow, mod):
    base %= mod
    result = 1
    while pow > 0:
        if pow & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        pow = pow >> 1
    return result


print(pow_mod(2, 12345, 1000))
