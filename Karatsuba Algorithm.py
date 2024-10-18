def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    a, b = divmod(x, 10**half)
    c, d = divmod(y, 10**half)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * 10**(2 * half) + ad_plus_bc * 10**half + bd


x = 1234
y = 5678
result = karatsuba(x, y)

print(f"The product of {x} and {y} is: {result}")
