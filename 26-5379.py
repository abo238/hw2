
file = open("26-90.txt").read()
fileline = file.split("\n")
N = int(fileline[0]) 
prices = list(map(int, fileline[1:-1] if fileline[-1] == "" else fileline[1:]))


sorted_prices_min = sorted(prices)  
expected_sum = sum(sorted_prices_min)
for i in range(3, N, 4):  
    expected_sum -= sorted_prices_min[i] * 0.5


sorted_prices_max = sorted(prices, reverse=True)  
actual_sum = sum(sorted_prices_max)
for i in range(3, N, 4):  
    actual_sum -= sorted_prices_max[i] * 0.5


print(int(expected_sum), int(actual_sum))
