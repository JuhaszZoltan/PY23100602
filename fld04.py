osszeg:int = 0
while True:
    szam:int = int(input('írj be egy számot: '))
    osszeg += szam
    if szam % 10 == 0: break
print(f'számok összege: {osszeg}')
