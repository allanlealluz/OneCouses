def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('false')
                break
        else:
         print('true')
    else:
        print('false')
is_prime(0)
is_prime(73)
is_prime(75)
