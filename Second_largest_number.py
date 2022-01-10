if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_element = max(arr)
    for i in range(0,n):
        if max_element - arr[i] == 1:
            print(arr[i])
            break
