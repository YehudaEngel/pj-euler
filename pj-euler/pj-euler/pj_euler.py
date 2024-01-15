import time

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

def Largest_prime_factor(): #pj-euler prob3
    
    x = 52 #input from user
    lpf = x
    i = 3
    
    while lpf%2 == 0: 
            lpf //= i

    while i < lpf:
        while lpf%i == 0: 
            lpf //= i
            # print(i) print for all prime factor exept the largest
        i+=2
    
    print (lpf) # print the largest prime factor
            
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

    for x in range(n,n//10,-1):
        for y in range(x,n//10,-1):
            if is_polindrom(x*y) and larg_pol < x*y:
                #print (x," * ",y," = ",x*y)
                larg_pol = x*y
    return larg_pol
                


def is_polindrom(num):
    
    if num == rvrs_num(num):
        #print ("num is a polindrom")
        return True
    #print ("num isnt a polindrom")
    return False

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

   
    
    


start = time.time()

#Multiples_of_3_or_5(5)
#Even_Fibonacci_numbers()
#Largest_prime_factor()
#Largest_palindrome_product()
#print(is_polindrom(121211))
#print(Largest_palindrome_product(2))


end = time.time()
print (end-start)