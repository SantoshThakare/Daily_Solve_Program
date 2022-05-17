def wordstr(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)

    return string


if __name__ == '__main__':
    k = 2
    str = "this is the python program "
    print(wordstr(k, str))
