def find_sum(num):
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The sum of all natural number", sum)


def natural_num(num):
    for item in range(0, num):
        print("the natural number is", item)


def even_odd_num():
    total = 0
    for num in range(2, 45, 2):
        print("it is even number", num)
        total = total + num
        print("the sum of even number", total)

    for num in range(1, 45, 2):
        print("it is odd number", num)
        total = total + num
        print("the sum of odd number", total)


if __name__ == '__main__':
    natural_num(45)
    find_sum(45)
    even_odd_num()