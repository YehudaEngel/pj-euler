import time
import math

def Multiples_of_3_or_5(rangeNum): #pj-euler prob1

    x = 0
    res = 0
    
    while x < rangeNum :
        if ((x % 5 == 0) or (x % 3 == 0)):
            res += x
        x += 1
    
    print ("Sum is:", res)


def Even_Fibonacci_numbers(): #pj-euler prob2
   
    a = 1
    b = 1
    res = 0

    while a+b < 4000000:
        if (a+b) % 2 == 0:
            res += a+b
        b = a+b
        a = b-a
    print (res)

def Largest_prime_factor(num): #pj-euler prob3
    
    lpf = num
    i = 3
    
    while lpf%2 == 0 and lpf != 2: 
            lpf //= 2

    while i < lpf:
        while lpf%i == 0: 
            lpf //= i
            # print(i) print for all prime factor exept the largest
        i+=2
    
    return (lpf) # print the largest prime factor
            
def is_prime(n):

    if n%2 == 0:
        return False
  
    for i in range(3,n,2):
        if n%i == 0:
            return False
    
    return True
    
def Largest_palindrome_product(num_of_dig): #pj-euler prob4
    n = 10**(num_of_dig)-1
    larg_pol = 0
    frst_fctr = 0
    scnd_fctr = 0

    for x in range(n,n//10,-1):
        for y in range(x,n//10,-1):
            if is_polindrom(x*y) and larg_pol < x*y:
                larg_pol = x*y
                frst_fctr = x #for future if will be needed
                scnd_fctr = y #for future if will be needed
    return larg_pol

def is_polindrom(num):
    
    if num == rvrs_num(num):
        return True #num is a polindrom
    return False #num isnt a polindrom

def rvrs_num(num):
    x = num
    rvrs_num = 0
    #count = 0
    
    while x > 0:
        rvrs_num = rvrs_num*10 + x % 10    # rvrs_num += (x % 10) * (10**(-count))    ->  didnt worked beacuase the way python calculating 10**(-6) edg.
        #count += 1
        x = x // 10
        # print(x, rvrs_num, num) # debuging check command
    #print ("num = ", num,", rvrs_num = ", rvrs_num)
    return rvrs_num

def Smallest_Multiple(X): #pj-euler prob5, Smallest_number_evenly_divisible_by_1_to_X
    X_primes = get_primes(X)

    for prime in X_primes:
        count = 2
        if prime**count > X:    
            break
        while prime**count <= X:            #\
            count += 1                      # \
        X_primes.insert(0,prime**(count-1)) # _\/  -> another way: replace 3 rows in that: X_primes.insert(0,prime**math.floor((math.log(X)/math.log(prime))) )
        X_primes.remove(prime)

    return math.prod(X_primes)
    
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes    

def Sum_square_difference(X): #pj-euler prob6
    return int((X**4)/4 + (X**3)/6 - (X**2)/4 - X/6)

start = time.time()

#Multiples_of_3_or_5(5)
#Even_Fibonacci_numbers()
#Largest_prime_factor(16)
#Largest_palindrome_product()
#print(is_polindrom(121211))
#print(Largest_palindrome_product(2))
#print(get_primes(10))
#print(Smallest_Multiple(1000000))
print(Sum_square_difference(100))

end = time.time()
print (end-start)