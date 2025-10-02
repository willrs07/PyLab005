def decimal_to_binary(n:int) -> str:
    if n == 0:
        return 'b'
    q, r = divmod(n,2)
    return decimal_to_binary(q) + str(r)

def binary_to_decimal(b:str) -> int:
    if b == '':
        return 0
    n = len(b) - 1
    pv = 2 ** n
    d = int(b[0])
    v = pv * d
    return v + binary_to_decimal(b.removeprefix(b[0]))

binary_to_decimal('1010')
#print(decimal_to_binary(10))   # "1010"
#print(decimal_to_binary(255))  # "11111111"
#print(decimal_to_binary(1))    # "1"
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("1"))         # 1
