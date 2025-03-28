def read_numbers(filename):
    with open(filename) as f:
        return list(map(int, f.readlines()))

def count_valid_triplets(numbers):
    min_elem = min(numbers)
    max_elem = max(numbers)
    min_remainder = min_elem % 5
    min_remainder_7 = min_elem % 7
    max_remainder = max_elem % 7
    max_remainder_5 = max_elem % 5
    
    count = 0
    sum_triplets = 0
    
    for i in range(len(numbers) - 2):
        triplet = numbers[i:i+3]

        if not any(100 <= x <= 999 for x in triplet):
            continue

        count_s1 = sum(1 for x in triplet if x % 5 == min_remainder_7)
        if count_s1 > 1:
            continue

        count_s2 = sum(1 for x in triplet if x % 7 == max_remainder_5)
        if count_s2 < 2:
            continue
        
        count += 1
        sum_triplets += sum(triplet)
    
    avg_sum_triplets = sum_triplets // count if count > 0 else 0
    return count, avg_sum_triplets

numbers = read_numbers("17-428.txt")
count_triplets, avg_sum_triplets = count_valid_triplets(numbers)
print(count_triplets, avg_sum_triplets)
