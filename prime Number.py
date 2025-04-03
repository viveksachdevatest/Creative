
get_number_range = input("Kindly input the number for finding prime number in the range between 0 and your input number \n")
number_range = int(get_number_range)
print(f"User input is {get_number_range} \n")

def prime_number(num):
    print(f"calling function with {num} with type {type(num)} \n")
    n = int(num) + 1
    list = []
    prime = []
    list.append(0)
    list.append(1)
    for i in range(2,n):
        for j in range(2,int(num)):
            if (i == j):
                break
            elif (i % j == 0):
                list.append(i)
                break

    print(f"Following numbers are not prime {list} \n")
    #print(f"Following numbers are prime {prime} \n")
    for de in range(2,n):
        if (de not in list):
            prime.append(de)
    print(f"Following numbers are prime {prime} \n")
    return prime
# prime_number(number_range)
Primelist = prime_number(get_number_range)
print(f"Following prime numbers {Primelist}")
