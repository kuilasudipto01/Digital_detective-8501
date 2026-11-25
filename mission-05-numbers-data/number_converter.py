# Number Converter Program
# Converts a decimal number to binary and hexadecimal

def main():
    user_input = input("Enter a positive decimal number: ")
    decimal_number = int(user_input)

    if decimal_number < 0:
        print("Please enter a positive number.")
        return

    binary_result = bin(decimal_number)
    hexadecimal_result = hex(decimal_number)

    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_result}")
    print(f"Hexadecimal: {hexadecimal_result}")

if __name__ == "__main__":
    main()
