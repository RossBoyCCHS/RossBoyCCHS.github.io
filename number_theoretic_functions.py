n = int(input("Enter a number: "))
print('n = ' + str(n))

def tau_function(n):
    print('The tau function for the number n gives the number of all the divisors of n.')
    number_of_divisors = 0
    string = ''
    for i in range(1,n+1):
        if (n % i == 0):
            number_of_divisors += 1
            string = string + str(i) + ', '
    print('The divisors of n are: ' + string + 'Therefore ...')
    print('tau(' + str(n) + ') = ' + str(number_of_divisors))

def sigma_function(n):
    print('The sigma function for the number n gives the sum of all divisors for n.')
    sum = 0
    string = ''
    for i in range(1,n+1):
        if (n % i == 0):
            string = string + str(i)
            sum += i
            if (i != n):
                string = string + ' + '
    print('sigma(' + str(n) + ') = ' + string + ' = ' + str(sum))

def sum_of_proper_divisors(n):
    number_of_divisors = 0
    for i in range(1,n):
        if (n % i == 0):
            number_of_divisors += 1
    sum = 0
    string = ''
    proper_divisor_counter = 0
    for i in range(1,n):
        if (n % i == 0):
            string = string + str(i)
            sum += i
            proper_divisor_counter += 1
            if (proper_divisor_counter != number_of_divisors):
                string = string + ' + '
    print('The sum of the proper divisors of n is ' + string + ' = ' + str(sum))

tau_function(n)
sigma_function(n)
sum_of_proper_divisors(n)
