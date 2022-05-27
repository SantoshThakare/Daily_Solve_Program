def arr():
    sum = []
    for element in arrayOne:
        sum.append(max([item + element for item in arrayOne]))
    print(max(sum))


if __name__ == '__main__':
    arr()