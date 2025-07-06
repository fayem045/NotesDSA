def binary_search(arr, target):
    left = 0
    right = len(arr) -1
 #left, right = 0, len(arr) -1

    while left <= right:
        mid = left + (right - left)

        if arr[mid] ==target:
            return mid
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid -1

    return -1

def main() -> None:
    arr = [1,2,3,4,5,6,7,8,9,10]
    target = 9
    print(binary_search(arr, target))

if __name__=='__main__':
    main()