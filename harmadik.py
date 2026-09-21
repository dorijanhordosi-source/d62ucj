# nyelvi szerkezetek
felhasznalo_kora = int(input("Hány éves vagy: "))
if felhasznalo_kora <= 18:
    print("Gyerek")
elif felhasznalo_kora <= 25:
    print('Ifjú')
elif felhasznalo_kora <= 65:
    print('Koros')
else:
    print('Nyugger')
uzenet = 'Gyere be' if felhasznalo_kora >= 18 else "Maradj kint"
print(uzenet)

i=1
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
else:
    print('Gond nelkül lefutott!')
print('vége a ciklusnak')

alap = 5
magassag = 3

kerulet = ker_ter(alap , magassag) [0]
terulet = ker_ter(alap , magassag) [1]
print(f'Kerület = {kerulet}\nTerület = {terulet}')

eredmeny = ker_ter(alap , magassag)
print(f'Kerület = {eredmeny[0]}\nTerulet = {eredmeny[1]}')