def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_number():
    while True:
        start = int(input("Enter the starting range (0 to terminate):  "))

        if start < 0:
            print("Enter a non-negative number.")
            print()
            continue

        if start == 0:
            print("Program terminated.\n")
            break

        end = int(input("Enter the end range: "))

        if end <= start:
            print("\nEnter a number greater than the starting range.")
         
            continue

        print("\nPrime numbers in the range {} to {}:".format(start, end))
        for num in range(start, end + 1):
            if is_prime(num):
                print(num, end=" ")

        print("\n")


def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"The smallest factor of {n} other than 1 is {i}.")
            return

    print(f"The smallest factor of {n} other than 1 is {n}")

def smallest_factor():
    while True:
        try:
            num = int(input("Enter a number greater than or equal to 2: "))
            factor = find_smallest_factor(num)
            print()
            
            if factor is not None:
                print(f"The smallest factor of {number} other than 1 is {factor}\n")

            if num < 2:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


while True:
    print("[1] Find the prime numbers in a range.")
    print("[2] Find the smallest factor of a number.")
    print("[0] Terminate")
    choice = int(input("\nEnter the number of your choice: "))
    print()
    
    if choice == 1:
        prime_number()
    elif choice == 2:
        smallest_factor()
    elif choice == 0:
        break
    else:
        print("Choice not included. Pls try again.")
