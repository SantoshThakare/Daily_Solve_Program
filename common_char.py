def common(str1, str2):
    lis = []

    for i in set(str1):
        for j in set(str2):
            if i == j:
                lis.append(i)

    return lis

if __name__ == "__main__":
    char = common("hello", "world")
    print(char)
