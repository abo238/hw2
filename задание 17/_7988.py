def sum_of_digits(n):
    return sum(int(d) for d in str(n))

with open("17-428.txt") as f:
    numbers = list(map(int, f.readlines()))

count_531 = sum(1 for x in numbers if x % 531 == 0)
count_773 = sum(1 for x in numbers if x % 773 == 0)

sum_digits = {x: sum_of_digits(x) for x in numbers}

valid_triplets = []

for i in range(len(numbers) - 2):
    triplet = numbers[i:i+3]

    if not any(100 <= x <= 999 for x in triplet):
        continue

    count_s1 = sum(1 for x in triplet if sum_digits[x] == count_531)
    if count_s1 > 1:
        continue

    count_s2 = sum(1 for x in triplet if sum_digits[x] == count_773)
    if count_s2 < 2:
        continue
    
    valid_triplets.append(sum(triplet))

count_triplets = len(valid_triplets)

avg_sum_triplets = sum(valid_triplets) // count_triplets if count_triplets > 0 else 0

print(count_triplets, avg_sum_triplets)

