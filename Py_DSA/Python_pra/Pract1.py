def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1

def main() -> None:
    arr = [1,2,3,4,5,6,7,8,9,10]
    target = 9
    print(linear_search(arr, target))

if __name__ == '__main__':
    main()