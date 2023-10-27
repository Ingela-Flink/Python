def main():
    glosLista = {}

    print("GLOSOR!")
    while True:
        svGlosa = input("Ange en svnesk glosa: ")
        enGlosa = input("Ange den engelska översättningen: ")

        glosLista.update({svGlosa : enGlosa})

        fortsatt = input("Vill du ange Fler? j/n: ")
        if  fortsatt == "n":
            break

    while True:


        print("\n Nu startar glosförhöret!")

        for glosa in glosLista:
            svar = input(f"\n {glosa} : ")

            if svar == glosLista[glosa]:
                print("Rätt svar!")
            else :
                print(f"\n Fel svar, rätt svar är {glosLista[glosa]}")

        fortsatt2 = input("Vill du köra om? j/n: ")
        if fortsatt2 == "n":
            break

main()