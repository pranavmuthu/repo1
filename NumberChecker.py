import sys

num = input("Please Enter a Number: ")
num = int(num)

if num % 2 == 0:
    print(num, "is an even number!!!")
else:
    print(num, "is an odd number!!!")

if num > 100:
    print(num, "is a large number!!!")
else:
    print(num, "is a small number!!!")

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number!!!")
            break
    else:
        print(num, "is a prime number!!!")
else:
    print(num, "is not a prime number!!!")