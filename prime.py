from datetime import datetime
import time


def calc_primes(iteration=100000):
    open("log.txt", "a").write(f"{datetime.now()}\n")

    try:
        primes = [int(i) for i in open("primes.txt", "r").readlines()[0].split(",")[1:]]
        open("log.txt", "a").write("primes.txt loaded\n")
    except FileNotFoundError:
        primes = [2]
        open("log.txt", "a").write("primes.txt FileNotFoundError\n")

    calculation_time = time.time()
    for n in range(
        primes[-1] +1 if primes[-1] % 2 == 0 else primes[-1] +2,
        primes[-1] + iteration +1 if primes[-1]+iteration % 2 == 0 else primes[-1] + iteration,
        2
    ):
        is_prime = True
        for q in primes:
            if n % q == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    open("log.txt", "a").write(f"calculations completed : {time.time()-calculation_time}sec\n")
    open("log.txt", "a").write(f"iteration = {iteration}\n")
    open("log.txt", "a").write(f"len = {len(primes)}\n")

    f = open("primes.txt", "w")
    [f.write(f",{i}") for i in primes]
    open("log.txt", "a").write("primes saved in primes.txt\n")

    open("log.txt", "a").write("\n")


if __name__ == "__main__":
    for i in range(160):
        print(i)
        calc_primes()
