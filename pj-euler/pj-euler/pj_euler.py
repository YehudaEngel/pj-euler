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
    
#def Largest_palindrome_product(): #pj-euler prob4


def is_polindrom(num):
    count = 0
    x = num
    rvrs_num = 0

    while x != 0:
        rvrs_num += (x % 10) * (10**(-count))
        count += 1
        x = x // 10
        print(x, count, rvrs_num)

    print((int)(rvrs_num*(10**(count-1))), num)



    
    
    



#Multiples_of_3_or_5(5)
#Even_Fibonacci_numbers()
#Largest_prime_factor()
#Largest_palindrome_product()
#is_polindrom(34343434) #error returning