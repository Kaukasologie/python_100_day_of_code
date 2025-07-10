def is_prime(num):
    prime = True
    if num == 1 or (num % 2 == 0 and num != 2):
        prime = False
    else:
        for number in range(3, num, 2):
            if num % number == 0:
                prime = False
    return prime

for i in range(1, 101):
    print(i, is_prime(i))
