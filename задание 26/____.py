def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

with open("17-428.txt") as f:
    numbers = [int(line.strip()) for line in f]

count_13 = count_25 = 0
sum_13 = sum_25 = 0  

for num in numbers:
    if num % 13 == 0:
        count_13 += 1
        if count_13 == 13:
            sum_13 = sum_of_digits(num)

    if num % 25 == 0:
        count_25 += 1
        if count_25 == 25:
            sum_25 = sum_of_digits(num)

    if count_13 >= 13 and count_25 >= 25:
        break

triple_count = 0
total_sum = 0

for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i+1], numbers[i+2]
    triple = [a, b, c]

    has_three_digit = any(100 <= x <= 999 for x in triple)

    count_sum_13 = sum(1 for x in triple if sum_of_digits(x) == sum_13)

    count_sum_25 = sum(1 for x in triple if sum_of_digits(x) == sum_25)

    if has_three_digit and count_sum_13 <= 1 and count_sum_25 >= 2:
        triple_count += 1
        total_sum += sum(triple)

avg_sum = total_sum // triple_count if triple_count > 0 else 0
print(triple_count, avg_sum)
