class arithmatic:

    def add(self, a ,b):
        w = a + b
        return w

    def sub(self,a , b):
        x = a - b
        return x

    def mul(self,a, b):
        y = a * b
        return y

    def div(self,a, b):
        z = a // b
        return z

if __name__ == '__main__':
    a = int(input("enter the first number :"))
    b= int(input("enter the second number :"))
    obj = arithmatic()
    w = obj.add(a,b)
    x = obj.sub(a,b)
    y = obj.mul(a,b)
    z = obj.div(a, b)
    print("addition  is", w)
    print("substraction is", x)
    print("multiplication is", y)
    print("division is", z)