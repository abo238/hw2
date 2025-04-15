def last_digit(n):
    return abs(n) % 10

with open("17-426.txt") as f:
    numbers = list(map(int, f.readlines()))

max_abs = max(numbers, key=abs)
max_val = max(numbers)

max_abs_end = last_digit(max_abs)
max_end = last_digit(max_val)

count = 0
sum_of_sums = 0

for i in range(len(numbers) - 2):
    triple = numbers[i:i+3]

    has_4digit = any(1000 <= abs(x) <= 9999 for x in triple)
    ends_with_abs = sum(1 for x in triple if last_digit(x) == max_abs_end)
    ends_with_val = sum(1 for x in triple if last_digit(x) == max_end)

    if has_4digit and ends_with_abs <= 1 and ends_with_val >= 1:
        count += 1
        sum_of_sums += sum(triple)

if count > 0:
    avg = sum_of_sums // count
else:
    avg = 0

print(count, avg)
