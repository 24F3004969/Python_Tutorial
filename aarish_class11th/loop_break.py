c = 0
n = int(input("Enter a numebrs \n"))
for i in range(0, n + 1):
    if i * i == n:
        c = 1
        break
if c == 1:
    print("Perfect sq")
else:
    print("Not a perfect sq")
