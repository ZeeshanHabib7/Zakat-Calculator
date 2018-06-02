import math
def main():
    gold=4985.119
    silver=77.33
    dollar=119.35
    na=input("Pls enter your name: ")       #na is the variable for name
    print("Welcome",na.capitalize(),"to Zakat Zalculator")
    print("*********MENU*********")
    s=input(" 1 for gold \n 2 for silver \n 3 for currency\n**********************\n")      #s is the variable for selections
    if(s=='1'):
        a=float(input("How much gold do you have?(in grams)"))                  #a is the variable for amount
        print("You have", a, "gold which cost: ", a * gold)

        if(a>=87.48):
            pay = float(a*gold *0.025)
            print("You have to pay : ", pay)
        else:
            print("\n**********************\n")
            print("You do't have to pay zakat")
    elif(s=='2'):
        a = float(input("How much silver do you have?(in grams)"))  # a is the variable for amount
        print("You have", a, "gm silver which cost: ", a * silver)

        if (a >= 612.36):
            pay = float(a * silver * 0.025)
            print("You have to pay : ", pay)
        else:
            print("\n**********************\n")
            print("You do't have to pay zakat")
    elif (s == '3'):
        a = float(input("How many dollors do you have?"))  # a is the variable for amount
        print("You have", a, "dollors which cost in PK rupees are : ", a * dollar)
        pk=a*dollar
        if (pk >= 47250 ):
            pay = float(pk * 0.025)
            print("You have to pay : ", pay)
        else:
            print("\n**********************\n")
            print("You do't have to pay zakat")


main()
print("\n**********************\n")
print("**********TERMS AND CONDITIONS**********")
print("Nisab. In Sharia (Islamic Law) niṣāb (نِصاب) is the minimum amount that a Muslim must have before being obliged to zakat.\nSeveral hadith have formulas for calculating niṣāb, the most prominent of which declares that No Zakāt is due on wealth until one year passes.")
print("Calculation formula used here is : your amount*gold/silver/dollor*2.5% ")
ex=input("Press 0 for exit ")