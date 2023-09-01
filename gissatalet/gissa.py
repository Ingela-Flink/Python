# Denna uppgift ska vi öva variabler, vilkor och loopar
import random
import os
os.system("cls" if os.name == "nt" else "clear")

print("\n------------------------------------------------------------------")
print(".:GissaTalet:.")

print("gissa ett tal mellan 1 till 10 och pröva lyckan, du får 3st försök!\n")

slumptal = random.randint(1, 10)
#print(slumptal)

i=0
hitta = False

#loop

while i < 3:

        gissatal = input("mata in tal: ")

        if slumptal == int(gissatal):
                hitta = True
                print("\n Rätt svar! \n")
                break
        
        i += 1

if hitta:
    print("\n Bra jobbat, här får du en anka")

else:
    print("Bättre lycka nästa gång")

print("\n---------------------------------------------------------------")
