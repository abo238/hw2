def generate_numbers():
    results = []
    divisor = 206
    
    for x in range(10):  
        for y in range(10):  
            for z in range(10):  #
                number_str = f"12{x}345{y}67089{z}"
                number = int(number_str)
                
               
                if number % divisor == 0:
                    results.append((number, number // divisor))
    
    return sorted(results)

numbers = generate_numbers()
for num, quotient in numbers:
    print(f"{num} {quotient}")
