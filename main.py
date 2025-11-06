"""
This module prints the prime numbers between 0 and 99.
"""
from math import sqrt
def isprime(p):
    """
    Return True if the number is prime or False if not

    Args:
        p (int): number to test

    Returns: 
        bool: True if the number is prime, False if not
    """
    if p < 2:
        return False
    for n in range(2, int(sqrt(p)) + 1):
        if p % n == 0:
            return False
    return True
def main():
    """
    Print prime numbers from 0 to 99.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
