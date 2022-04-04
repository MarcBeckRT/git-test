i = int
n = int
k = int

for n in range(2, 999, 1):
    prim1 = int(1)
    prim2 = int(1)
    m = n+2
    for i in range(2, int((n/2)+1), 1):
        prim1 = prim1 * (n % i)
    for k in range(2, int((m/2)+1), 1):
        prim2 = prim2 * (m % k)
        
    if(prim1>0 and prim2>0):
            print('(' + str(n) + ',' + str(m) + ')')    
        #if(prim1>0):
         #   print('(' + str(n) + ')')
        
