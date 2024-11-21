
low = int(input("Enter your lowest number"))
hi = int(input("Enter your highest number"))

for i in range(low , hi+1):
    if i > 1:
     for j in range(2,i):
        if i%j == 0:
           break
     else:
        print(i)
