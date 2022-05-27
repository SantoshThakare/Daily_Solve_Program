
def decimal_to_hex():
    num = int(input("enter any decimal number : "))
    temp = num
    hexa = []
    result = []

    while temp != 0:
        rem=temp%16

        if rem<10:
            hexa.append(char(rem+48))
        else:
            hexa.append(char(rem+55))
        temp= int (temp/16)
        j=1
    for i in hexa:
        result.append(hexa[len(hexa)-j])
        j = j+1
        print(result)

if __name__ == '__main__':

    decimal_to_hex()