def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n -1)

def main() -> None:
    number = 5
    factorial(number)
    print(f"Factorial of {number} is {factorial(number)} ")

if __name__ == "__main__":
    main()