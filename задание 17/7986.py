with open("17-428.txt") as f:
    numbers = list(map(int, f.readlines()))

min_num = min(numbers)
max_num = max(numbers)

min_mod11 = min_num % 11
max_mod7 = max_num % 7

count = 0
sum_of_sums = 0

for i in range(len(numbers) - 2):
    triple = numbers[i:i+3]

    has_4digit = any(1000 <= x <= 9999 for x in triple)
    mod11_match = sum(1 for x in triple if x % 11 == min_mod11)
    mod7_match = sum(1 for x in triple if x % 7 == max_mod7)

    if has_4digit and mod11_match <= 1 and mod7_match >= 2:
        count += 1
        sum_of_sums += sum(triple)

if count > 0:
    average = sum_of_sums // count
else:
    average = 0

print(count, average)
