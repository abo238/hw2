file = open("26-152.txt").read()
fileline = file.split('\n')
N = int(fileline[0])
A = fileline[1:-1] if fileline[-1] == "" else fileline[1:]

D = {}
for line in A:
marks, summ, cl = map(int, line.split())
key = (marks, cl)
D[key] = D.get(key, 0) + summ

D_sorted = sorted(D.items(), key=lambda x: x[1], reverse=True)
max_sales = D_sorted[0][1]
max_price = 0
max_count = 0

for key, sales in D_sorted:
marks, cl = key
if sales == max_sales:
if marks > max_price:
max_price = marks
max_count = sales - D[(marks, 0)]
elif marks == max_price:
max_count = min(max_count, sales - D[(marks, 0)])

print(max_price * max_count, max_count)