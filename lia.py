import math    
                                                       
k = 5                                                                       
n =  7                                                                       
P = 2**k                                                                       
probability = 0                                                                
for x in range(n, P + 1):                                                      
    prob = (math.factorial(P) / (math.factorial(x) * math.factorial(P - x))) * (0.25**x) * (0.75**(P - x))                                                        
    probability += prob                                                        
print(probability)       