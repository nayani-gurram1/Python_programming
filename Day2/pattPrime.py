def print_prime_grid(rows, cols):
    num = 2
    count = 0
    r = 0
    while r < rows:
        c = 0
        while c < cols:
            is_prime = True
            i = 2
            while i * i <= num:
                if num % i == 0:
                    is_prime = False
                    break
                i += 1
            if is_prime:
                print(f"{num:3}", end=" ")
                c += 1
                count += 1
            num += 1
        print() 
        r += 1
print_prime_grid(6, 6)
