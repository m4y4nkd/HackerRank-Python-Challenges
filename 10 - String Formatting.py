def print_formatted(number):
    width = len(str(bin(number))[2:])
    for i in range(1,number+1):
        s1 = str(i)
        s2 = str(oct(i))[2:]
        s3 = "%X" % i
        s4 = str(bin(i))[2:]
        print(s1.rjust(width),s2.rjust(width),s3.rjust(width),s4.rjust(width))