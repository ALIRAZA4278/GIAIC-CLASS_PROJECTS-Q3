def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

# This line ensures main runs when the script is executed
if __name__ == '__main__':
    main()
