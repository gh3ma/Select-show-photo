def add(x ,y ):
    return x + y
def sub(x ,y ):
    return x - y
def div(x ,y):
    return x / y
def multi(x ,y):
    return x * y
def power(x ,y):
    return x**y

#-----------#

print("choose number of the peration")
print("------------------------------------------------------------------------\n"
      "\t 1\t||\t\t2\t\t||\t\t3\t\t||\t\t4\t||\t\t5\t\t||\n"
      "\tAdd\t||\t Subtract\t||\t Multiply\t||\tDivide\t||\t  power \t||\n"
      "------------------------------------------------------------------------")
while True:
    user =  input("Enter the number of opertion :")
    if user in ('1' ,'2','3','4','5'):
            try:
                mum1 = float(input("Enter first num -->"))
                mum2 = float(input("Enter second num -->"))
            except ValueError:
                print("wrong number")
                continue

            if user == '1' :
                print(add(mum1,mum2))
            elif user == '2' :
                print(sub(mum1,mum2))
            elif user == '3' :
                print(multi(mum1,mum2))
            elif user == '4' :
                print(div(mum1,mum2))
            elif user == '5' :
                print(power(mum1,mum2))

            more = input("Do u want make another calculate?\n(y/n):")
            if more == 'n':
                print("--Goodbye--")
                break
            else:
                    print("wrong char")
                    continue