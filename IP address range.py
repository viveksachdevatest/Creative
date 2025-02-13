# this program prints all the IP addresses seperated by comma
a = 0
b = 0
c = 0
d = 0
sub = input("Kindly enter count of IP address needed \n")
num = int(sub)
ty = type(num)
print(num,ty)

count = 0
for i in range(256):
    for j in range(256):
        for k in range(256):
            for l in range(256):
                print(f"{a}.{b}.{c}.{d}", end=", ")
                d += 1
                count += 1
                if count == num:
                    print(f"\nPrinting {num} of IP addresses")
                    exit()
                if d == 256:
                    d = 0
                    break
            c += 1

            if c == 256:
                c = 0
                break
        b += 1

        if b == 256:
            b = 0
            break
    if a == 256:
        a = 0
        break

