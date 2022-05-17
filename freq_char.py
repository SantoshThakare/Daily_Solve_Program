def frequency_char():

    test_str = "santosh thakare"

    all_freq = {}

    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    print("Count of all characters in santosh thakare is :\n " +  str(all_freq))


if __name__ == '__main__':

    frequency_char()