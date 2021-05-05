def pow_mod(pow, mod):
    base = 3
    base %= mod
    result = 1
    while pow > 0:
        if pow & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        pow = pow >> 1
    return result

line = input()
arg = list(map(int, line.split()))
K = arg[0]
n = arg[1]
print(pow_mod(K, n))
