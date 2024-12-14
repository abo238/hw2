file = open("26-152.txt").read()
fileline = file.split('\n')
N = int(fileline[0])
A = fileline[1:-1] if fileline[-1] == "" else fileline[1:]

D = {}
for line in A:
    marks, summ, cl = map(int, line.split())
    if cl == 1:
        D[marks] = D.get(marks, 0) + summ

D_sorted = sorted(D.items(), key=lambda x: x[1], reverse=True)
max_sales = D_sorted[0][1]
max_price = 0
max_count = 0

for key, sales in D_sorted:
    if sales == max_sales:
        if key > max_price:
            max_price = key
            max_count = sales
        elif key == max_price:
            max_count = min(max_count, sales)

print(max_price * max_count, max_count)
