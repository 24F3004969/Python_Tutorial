n = int(input("Enter a number :"))
if 99 < n < 1000:
    ld = n % 10
    md = (n % 100) / 10
    fd = n / 100
    if fd > md > ld:
        print("descending order")
    elif fd < md < ld:
        print("ascending order")
    else:
        print('No order')
else:
    print("Not a 3 digit number")
