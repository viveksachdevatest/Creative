import math

def compound_interest(prin,rate, num_years):
    interest = (1 + (rate/100))
    int = math.pow(interest,num_years)
    final_value = prin * int
    return final_value

def cagr(final,initial,years):
    cag = math.pow((final / initial), (1 / years))
    cagr = (cag - 1) * 100
    return cagr

get_inp = input("Do you want to calucate Compound Interest or CAGR? (Compound Interest/CAGR) \n")

if get_inp.lower() == "compound interest":
    while 1:
        amount = int(input("Enter Principal amount\n"))
        rate = float(input("Enter rate of Interest\n"))
        num_years = int(input("Enter number of years of investment\n"))
        final_amount = compound_interest(amount,rate,num_years)
        print(f"Final amount with compounded interest at {rate} is {final_amount:.2f} \n")
        cag = math.pow((final_amount/amount),(1/num_years))
        cagr1 = (cag - 1)*100
        print(f"CAGR growth is {cagr1:.2f}% \n")

        ans = input("Do you want to check compound interest again for another data? (Y/N) \n")
        if ans.lower() == "n":
            break
        elif ans.lower() != "n" and ans.lower() != "y":
            print(f"incorrect input, hence closing the program")
            break

elif get_inp.lower() == "cagr":
    while 1:
        amtt1 = int(input("Provide the final amount received for CAGR \n"))
        amtt2 = int(input("Provide the initial amount invested for CAGR \n"))
        tim = int(input("Provide the number of years the amount was invested \n"))
        growth = cagr(amtt1,amtt2,tim)
        print(f"CAGR amount is {growth:.2f} \n")
        ent = input("Do you want to Check CAGR for another data? (Y/N) \n")
        if ent.lower() == "n":
            break
        elif ent.lower() != "n" and ent.lower() != "y" :
            print(f"Incorrect Input, hence closing this program")
            break

else:
    print(f"Incorrect choice, exiting the program")
    exit()