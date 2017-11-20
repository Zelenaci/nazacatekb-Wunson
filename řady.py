def radaf(rada):
    rada = rada.split()
    i = 0
    for x in rada:
        rada[i] = int(rada[i])
        i += 1        
    return rada

def suda(rada):         #počet sudých x
    pocet = 0
    for x in rada:
        if (x % 2) == 0:
            pocet += 1
    print("počet sudých:\n",pocet)

def vetsimensi(rada):   #vypisuje x vetsi 11 a mensi 19
    print("větší než 11 a menší než 19:",)
    for x in rada:
        if x>11 and x<19:     
            print(x,end = " ")

def trictyri(rada):      #vypisuje x dělitelné 4 a 3
    print("dělitelné 4 a 3:")
    for x in rada:
        if (x % 3) == 0 and (x % 4) == 0:
            print(x,end = " ")

def zaporna(rada):      #součet kladných a záporných čísel
    zaporna = 0
    kladna = 0
    print("součet kladných a záporných:")
    for x in rada:
        if x < 0:
            zaporna += x
        else:
            kladna += x
    print(">>>",zaporna)
    print(">>>",kladna)
    
def mocniny(rada):  # scítá 2. mocniny čísel v řadě      
    soucet = 0
    for x in rada:
        soucet += (x**2)
    print("součet 2 mocnin:\n",soucet)

def prumer(rada):      #prumer
    soucet = 0
    for x in rada: soucet += x
    print("průměr:\n",soucet/len(rada))

# rada = (5,3,11,19,12,64,35,17,4,-3,-5,-11,-19,-4) 

rada = radaf(input("napiš řadu celých čisel s mezerami:"))
print()
vetsimensi(rada)
print()
suda(rada)
print()
trictyri(rada)
print()
zaporna(rada)
print()
mocniny(rada)
print()
prumer(rada)
print()

        