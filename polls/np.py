

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False

    return sieve



count = 0
list_of_primes = sieve_of_eratosthenes(1000000)
k = len(list_of_primes)
for x in range(k-1):
    text = list_of_primes[x]
    print(text)
    if(text%100>25 and text%100<50):
        count+=1
