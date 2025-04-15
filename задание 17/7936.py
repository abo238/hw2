with open("17-426.txt") as f:
    numbers = list(map(int, f.readlines()))

target_numbers = [x for x in numbers if 10000 <= abs(x) <= 99999 and abs(x) % 100 == 43]

max_target = max(target_numbers)
max_square = max_target ** 2

count = 0
min_sum_squares = None

for i in range(len(numbers) - 2):
    triple = numbers[i:i+3]

    has_target = any(10000 <= abs(x) <= 99999 and abs(x) % 100 == 43 for x in triple)
    sum_squares = sum(x ** 2 for x in triple)

    if has_target and sum_squares <= max_square:
        count += 1
        if min_sum_squares is None or sum_squares < min_sum_squares:
            min_sum_squares = sum_squares

print(count, min_sum_squares)
