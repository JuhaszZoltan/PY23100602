dolgok:list[str] = ['kalap', 'esernyő', 'cickány', 'gesztenyepüré', 'lovaglóostor', 'lakáskulcs', 'pokélabda']

keresett:str = input('mit keresel?: ')

for cucc in dolgok:
    if keresett == cucc:
        print(f'a {keresett} benne van a dolgokban')
        print(f'az intexe: {dolgok.index(keresett)}')
        break
else: print(f'sajnos a {keresett} az nincs meg :(')