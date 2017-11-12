prime_factors = []
n = 0
end_number = 600851475143
while (n * n <= 20):
    n = n+1
    if n % 2 != 0 and n % 3 != 0 or n == 2:
        prime_factors = 0
        prime_factors = prime_factors + n
        print prime_factors
