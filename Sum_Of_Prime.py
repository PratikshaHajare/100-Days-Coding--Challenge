n=int(input("How Many Values :"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    #Take Nos From User
    lst=list()
    for i in range(1,n+1):
        v=int(input("Enter {i} Value: "))
        lst.append(v)
    print(f"content of list : {lst}")
    
    #code for primes:
    l1=list()
    for num in lst:
        if(num<=1):
            print(f"{num} invalid input")
        else:
            res=True
            for k in range(2,num):
                #not prime
                if(num%k==0):
                    res=False
                    break
            if(res):
                l1.append(num)
                
    #Sum Of Primes            
    print(f"Prime list: ",l1)
    prime_sum=0
    for k in l1:
        prime_sum=prime_sum+k
    print("Sum Of Prime : ",prime_sum)        
            
