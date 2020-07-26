import sys

def find_prime_factors(number):
    prime_factors = list()
    
    divisor = 2
    while divisor <= number:
        if number == 1:
            break
        if number % divisor == 0:
            prime_factors.append(divisor)
            number /= divisor
        else:
            divisor += 1

    return prime_factors


def main():
    try:
        print(find_prime_factors(int(sys.argv[1])))
    except ValueError:
        print("Non integer input")


if __name__ == "__main__":
    main()

