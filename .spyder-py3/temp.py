
n = int(input('Primzahl?: '))
i = int 
prim = int
prim = 1

if(n>1):
    for i in range(2, int(n/2) , 1):
        prim = prim * (n % i)

    if (prim > 0):
        print('Es ist eine Primzahl')
    else:
        print('Es ist keine Primzahl')
else:
    print('Es ist keine Primzahl')
