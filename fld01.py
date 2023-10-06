a:int = int(input('=oldalú 3szok oldalának hossza (cm): '))
print(f'kerület hetede: {a*3/7:.2f} cm')

r:int = int(input('kör sugarának hossza (cm): '))
print(f'kerülete: {2*r*3.14:.2f} cm')

cssz:int = int(input('hány csillag legyen: '))
print(f'Béla jutalma: {cssz * "*"}')

print('Béla jutalma:', end=' ')
for _ in range(cssz):
    print('*', end='')

print('\n')
szam:float = 2.4152137
tjsz:int = 2

kerekitett = round(szam)
print(kerekitett)
kerekitett = round(szam, tjsz)
print(kerekitett)

print(f'{szam:.2f}')

print(f'{1000:.2f}')

print(f"szám 3 tizedes jeggyel: {round(3.1234567, 3)}")