# Python3 code to find largest prime
# factor of number
import math


def maxPrimeFactors(n):
    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2

    # n must be odd at this point
    while n % 3 == 0:
        maxPrime = 3
        n = n / 3

    # now we have to iterate only for integers
    # who does not have prime factor 2 and 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            maxPrime = i
            n = n / i
        while n % (i + 2) == 0:
            maxPrime = i + 2
            n = n / (i + 2)

    # This condition is to handle the
    # case when n is a prime number
    # greater than 4
    if n > 4:
        maxPrime = n

    return int(maxPrime)


if __name__ == "__main__":
    n = 15
    print(maxPrimeFactors(n))

    n = 25698751364526
    print(maxPrimeFactors(n))

    n = 16
    print(maxPrimeFactors(n))

# This code is contributed by Susobhan Akhuli