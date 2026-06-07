def approximate_pi(n):
    sum = 0
    i = 1
    while i<=n:
        sum += 1/(i**2)
        i += 1
1        if i==n:
            print(f'The sum is {sum}')
    print(f'approximate value of pi is {(sum * 6) ** 0.5}')

approximate_pi(5)
# sum = 1.4636111111111112
# approximate value of pi is: 2.9633877010385707

approximate_pi(10)
# sum = 1.5497677311665408
# approximate value of pi is: 3.04936163598207
