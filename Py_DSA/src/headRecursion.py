def headRecursion(n: int) -> int:
    if n > 0:
        print(n) #nagcall lang, no ginawang iba
        return headRecursion(n-1) #call agad na nagooverflow prone

def main() -> None:
    number: int = 5
    headRecursion(number)

if __name__ == '__main__':
    main()
