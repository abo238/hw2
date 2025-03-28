def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def matches_mask(num, mask):
    num = str(num)
    i, j = 0, 0
    while i < len(num) and j < len(mask):
        if mask[j] == '*':
            if j == len(mask) - 1:  
                return True
            j += 1
            while i < len(num) and (mask[j] != num[i] and mask[j] not in '?*'):
                i += 1
        elif mask[j] == '?':
            i += 1
            j += 1
        elif mask[j] == num[i]:
            i += 1
            j += 1
        else:
            return False
    return i == len(num) and all(c == '*' for c in mask[j:])

def digit_sum(n):
    return sum(map(int, str(n)))

mask = "7*53?3*1"
divisor = 2627

results = []
for n in range(divisor, 10**9, divisor):
    if matches_mask(n, mask):  
        if is_prime(digit_sum(n)):  
            results.append((n, n // divisor))

for number, quotient in results:
    print(number, quotient)
