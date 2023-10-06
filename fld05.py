szamlalo:int = 1
while szamlalo <= 10:
    allat:str = input(f'írd be az {szamlalo}. allatot: ')
    szamlalo += 1
    if allat == 'fotel': break
else: print('ügyes vagy, egyik állat sem fotel!')

# ciklushoz tartozó 'else' akkor fut le, ha a ciklusban sosem volt 'break'