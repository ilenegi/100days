def main():
    # items = list(map(int, input().split()))
    items = [1,-2,3,5,-3,2]
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(overall[0])


if __name__ == '__main__':
    main()