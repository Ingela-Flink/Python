#value = input() 

input = input()
length = len(input)

person_nummer_utan_sista_siffran = input[:-1]

print(person_nummer_utan_sista_siffran)

person_nummer = []
summa = 0


for siffra in person_nummer_utan_sista_siffran:
    person_nummer.append(int(siffra))

for i in range(len(person_nummer)):

    if person_nummer[i] % 2 == 0:
        if person_nummer[i] * 2 >= 10:
            temp = person_nummer[i] * 2
            
            for siffra in str(temp):
                summa += int(siffra)
            
        else:            
            summa += person_nummer[i] * 2

    else:
        summa += person_nummer[i]


print((10-(summa%10))%10)

if length == 10:
    print("JA")
else:
    print("NEJ")
    exit()
