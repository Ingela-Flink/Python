import os
def vokal_lika_med_E():

    text = input().upper()
    
    vokaler = ["A", "O", "U", "Å", "E", "I", "Y", "Ä", "Ö"]

    output = ""

    for bokstav in text:
        bokstav = bokstav.upper()

        if bokstav in vokaler:
            output += "E"
        else:
            output += bokstav
    if output.isalpha():
        print(output)
    else:
        print("Använd bara bokstäver!")


vokal_lika_med_E()
input()
os.system('cls' if os.name == 'nt' else 'clear')
