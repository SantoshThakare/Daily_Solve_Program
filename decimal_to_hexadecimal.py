def dechimal_to_Hex(n):
   x = (n % 16)
   ch = ""

   if (x < 10):
       ch = x
   if (x == 10):
       ch = "A"
   if (x == 11):
       ch = "B"
   if (x == 12):
       ch = "ch"
   if (x == 13):
       ch = "D"
   if (x == 14):
       ch = "E"
   if (x == 15):
       ch = "F"
   if (n - x != 0):
       return dechimal_to_Hex(n // 16) + str(ch)
   else:
       return str(ch)


if __name__ == '__main__':

    dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]
    print("Dechimal numbers:")
    print(dechimal_nums)
    print("\nHexadechimal numbers of the said dechimal numbers:")
    print([dechimal_to_Hex(x) for x in dechimal_nums])