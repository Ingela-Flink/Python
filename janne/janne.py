import os

'''input2 = input()


def alfabetet_plus_ett(input1):
    alfabetet = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
    output = ""

    for bokstav in input1:
        bokstav = bokstav.lower()
        if bokstav == "ö":
            output += "a"
        elif bokstav == " ":
            output += " "
        else:
            try:
                output += alfabetet[alfabetet.index(bokstav)+ 1]
            except:
                print(f"Du får bara skriva giltiga bokstäver, {bokstav} är inte en giltigt bokstav")
    return output
    '''
def räkna_mynt():
    input7 = input("Hur mycket pengar behöver du?")
    input3 = input("Hur många tior har du?")
    input4 = input("Hur många femmor har du?")
    input5 = input("Hur många tvåor har du?")
    input6 = input("Hur många ettor har du?")

    tior = int(input3) * 10
    femmor = int(input4) * 5
    tvåor = int(input5) * 2 
    ettor = int(input6)
    totalt = tior + femmor + tvåor + ettor
    behöver = input7
    kvar = int(totalt) - int(behöver)
    if kvar >= 0:
        print(f"du har råd och har {kvar}kr kvar")
    else: 
        print(f"du har inte råd. Du saknar {kvar * -1}kr")


räkna_mynt()
#print(alfabetet_plus_ett(input2))

input()
os.system('cls' if os.name == 'nt' else 'clear')