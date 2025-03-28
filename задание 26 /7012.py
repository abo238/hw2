file = open("26-136.txt").read()
filelines = file.strip().split("\n")
N, M = map(int, filelines[0].split())
data = filelines[1:]

expensive = {}
cheap = {}
unsold_expensive = 0
unsold_cheap = 0

for line in data:
    price, status = map(int, line.split())
    if price > M:  
        if status == 1:  
            expensive[price] = expensive.get(price, 0) + 1
        else:  
            unsold_expensive += 1
    else:  
        if status == 1:  
            cheap[price] = cheap.get(price, 0) + 1
        else: 
            unsold_cheap += 1

most_popular_expensive = max(expensive.items(), key=lambda x: x[1], default=(0, 0))
most_popular_cheap = max(cheap.items(), key=lambda x: x[1], default=(0, 0))

total_revenue = most_popular_expensive[0] * most_popular_expensive[1] + \
                most_popular_cheap[0] * most_popular_cheap[1]

unsold_total = unsold_expensive + unsold_cheap

print(total_revenue, unsold_total)
