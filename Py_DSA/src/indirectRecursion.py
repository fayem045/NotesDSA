def method_a(n: int) -> int:
    if n > 0:
        print(f"Method A: {n}")
        return method_b(n-1)

def method_b(n: int) -> int:
    if n > 0:
        print(f"Method B: {n}")
        return method_a(n-1)

def main() -> None:
    number: int = 5; #type hinting, to know what type nirereturn, yung dagdag
    method_a(number)

if __name__ == "__main__":
    main()