def print_res(common):
    print(common)


def common(str1, str2):
    common = []

    for i in set(str1):
        for j in set(str2):
            if i == j:
                common.append(i)

    return common


def main():
    str1 = "hello"
    str2 = "world"

    common_worlds = common(str1, str2)
    print_res(common_worlds)


if __name__ == "__main__":
    main()
