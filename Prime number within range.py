from posixpath import split

initial = int(input("Provide lower number for range to find out prime number \n"))
later = int(input("Provide higher number for range to find out prime number \n"))

def prime_num_range(num1, num2):
    list = []
    primeNum = []
    el = num2 + 1
    for i in range(num1, el):
        if (i == 0 or i == 1):
            list.append(i)

        for j in range(2, num2):
            if (i == j):
                break
            elif (i % j == 0 and i != 0):
                list.append(i)
                break
    for de in range(num1,el):
        if (de not in list):
            primeNum.append(de)

    print(f"Following is the list of numbers which are not prime {list} \n")
    print(f"Following is the list of prime numbers {primeNum} \n")
    return primeNum

ai = prime_num_range(initial, later)
print(f"prime numbers are {ai} \n")

for l in range(len(ai)):

    ai[l] = str(ai[l])

newer = ".".join(ai)
print(f"concat prime numbers using dot is {newer} \n")
lp = newer.split(".")
print(f"splitting prime numbers again using dot {lp} \n")


