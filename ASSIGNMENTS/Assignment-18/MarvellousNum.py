def checkPrime(no):
    prime = True
        
    for i in range(1,(no//2)+1):
        if( no == 1 or (no%i == 0 and i!=1 and i!=no)):
            prime = False
            break
    
    return prime