osszeg:int = 0
szam:int = 3456
while szam % 10 != 0:
    szam = int(input('írj be egy számot: '))
    osszeg += szam
print(f'számok összzege: {osszeg}')