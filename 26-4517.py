
# Чтение данных из файла
file = open("26-62.txt").read()
lines = file.strip().split("\n")
N, M = map(int, lines[0].split())  # Количество товаров и бюджет
items = [line.split() for line in lines[1:]]

# Разделяем товары по типам и сортируем по цене
Q_items = sorted([int(price) for price, t in items if t == "Q"])
Z_items = sorted([int(price) for price, t in items if t == "Z"])


max_total_count = 0
max_z_count = 0
min_remaining = M

for z_count in range(len(Z_items) + 1):
    z_cost = sum(Z_items[:z_count])
    if z_cost > M:
        break

    remaining = M - z_cost

    q_count = 0
    q_cost = 0
    for price in Q_items:
        if q_cost + price <= remaining:
            q_cost += price
            q_count += 1
        else:
            break

    total_count = z_count + q_count

    if (
        total_count > max_total_count or
        (total_count == max_total_count and z_count > max_z_count) or
        (total_count == max_total_count and z_count == max_z_count and remaining - q_cost < min_remaining)
    ):
        max_total_count = total_count
        max_z_count = z_count
        min_remaining = remaining - q_cost

print(max_z_count, min_remaining)
