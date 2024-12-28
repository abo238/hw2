def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def matches_mask(n):
    s = str(n)
    if not s.endswith("21"):
        return False
    if "23" not in s:
        return False
    return len(s) >= 10 and s[0].isdigit()

low = 10**9
high = 10**10

results = []
for p in range(2, int(high**0.25) + 1):  
    if is_prime(p):
        n = p**4
        if n < low:
            continue
        if n > high:
            break
        if matches_mask(n):
            results.append((n, p**2))  

for num, third_divisor in sorted(results):
    print(num, third_divisor)
