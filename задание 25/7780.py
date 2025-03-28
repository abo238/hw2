def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def matches_mask(n):
    s = str(n)
    if not s.endswith("49"):
        return False
    if "61" not in s:
        return False
    return len(s) >= 9 and s[0].isdigit()

low = 10**8
high = 10**9

results = []
for p in range(2, int(high**0.5) + 1):  
    if is_prime(p):
        n = p**2
        if n < low:
            continue
        if n > high:
            break
        if matches_mask(n):
            results.append((n, p))  

for num, second_divisor in results:
    print(num, second_divisor)
