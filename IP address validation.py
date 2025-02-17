get_ip = input("kindly enter the IP address in x.x.x.x format \n")

def validate_ip_addr(ip):
    addr = ip.split(".")
    count = 1
    for bit in addr:
        if int(bit) > 255 or len(addr) > 4:
            print(f"Incorrect IP address as {count} bit is above 255 or length of IP address is {len(addr)} more than 4. Exiting program \n")
            exit()
        count +=1
    return True

def increment_bit(ai,num,siz):
    num = int(num)
    siz = int(siz)
    ai = ai.split(".")
    if int(num) > 3 or int(num) < 0:
        print(f"Incorrect bit choosen, kindly enter any number between 0 & 3 \n")
        exit()
    el = ai[num]
    el = int(el)
    el += siz
    if el > 255:
        print(f"Incorrect IP address will be created after adding {num} bit of value {ai[num]} with {siz}. Exiting program \n")
        exit()
    ai[num] = str(el)
    print(ai)
    new_ip = ".".join(ai)
    print(new_ip)
    return new_ip

if validate_ip_addr(get_ip):
    print(f"IP address {get_ip} is successfully validated \n")
else:
    print(f"IP address {get_ip} is not correct. Try again \n")


while 1:
    mun = int(input("Kindly enter the bit number between 0 - 3 to be modified \n"))
    size = int(input("Kindly enter the increment size for the bit \n"))
    nip = increment_bit(get_ip,mun,size)
    print(f"Here is the new updated ip address {nip} \n")
    arg = input("Do you want to try again with same IP? (Y/N) \n")
    if arg.lower() == "y":
        print(f"trying again \n")
    elif arg.lower() == "n":
        print(f"Exiting program \n")
        exit()
    else:
        print(f"Incorrect input. Exiting program \n")
        exit()

