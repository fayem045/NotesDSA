def tailRecusion(n:int, sum_value:int) -> int:#'-> int' irereturn na int
    if n <= 0: #need satisfy this condition
        return sum_value #may ginawa muna dito
    return tailRecusion(n-1, sum_value + n)#before call this main func "tailRecusion(n-1, sum_value + n)", may ginawa muna na palitan sum_value


def main() -> None:
    number: int = 5
    sum_value: int = 0
    print(f"Sum of numbers from 1 to {number} is {tailRecusion(number, sum_value)}") # print lagay para magprint


if __name__ == '__main__':
    main()