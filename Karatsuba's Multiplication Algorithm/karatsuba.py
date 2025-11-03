# Author: Jigesh Sheoran
# SAP ID: 590025428


def karatsuba_multiplication(x, y):
    
    # base case - if numbers are small, use normal multiplication
    if x < 10 or y < 10:
        return x * y

    # convert no. to strings for splitting
    str_x = str(x)
    str_y = str(y)

    n = max(len(str_x), len(str_y))
    m = n // 2  # split halfway

    # powers of 10 for splitting
    power_m = 10 ** m
    power_2m = 10 ** (2 * m)

    # split the no.s into two halves
    a = x // power_m
    b = x % power_m
    c = y // power_m
    d = y % power_m

    # recursive multiplication
    Z2 = karatsuba_multiplication(a, c)
    Z0 = karatsuba_multiplication(b, d)
    Z1 = karatsuba_multiplication(a + b, c + d) - Z2 - Z0

    # combine results
    result = Z2 * power_2m + Z1 * power_m + Z0

    return result


if __name__ == "__main__":
    print("***** Karatsuba Multiplication Algorithm *****\n")

    # Taking input from user
    num1 = int(input("Enter first number (A): "))
    num2 = int(input("Enter second number (B): "))

    # Perform Karatsuba Multiplication
    karatsuba_result = karatsuba_multiplication(num1, num2)
    standard_result = num1 * num2

    # Display Results
    print("\n---------------------- Result ----------------------")
    print(f"Number 1 (A): {num1}")
    print(f"Number 2 (B): {num2}")
    print(f"\nKaratsuba Result: {karatsuba_result}")
    print(f"Standard Result:  {standard_result}")
    print(f"\nVerification (Both Match?): {karatsuba_result == standard_result}")
    
    print("\n Program executed successfully \n")
