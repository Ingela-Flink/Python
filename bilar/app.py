import bil


looping = True

volvo_svart = bil.Bil("Volvo", "Svart", 3)
fiat_vit = bil.Bil ("Fiat", "vit", 10)
bugatti_rosa = bil.Bil ("Bugatti", "Rosa", 1)

billista = [volvo_svart, fiat_vit, bugatti_rosa]


#print(f"tredje bilen i listan = {billista[2].fabrikat}")

while looping:
    print("---------------------------------------------------------------------")
    print ("\n\t -:BilAutomat:- ")

    i=0

    for bil in billista:
        print(f"{i+1} : {bil.fabrikat} : {bil.color} : Antal={bil.lager}")
        i +=1


    bil_nr = input("\nmata in siffra för vald bil: ")
    #Typ omvandlar eller castar till int
    bil_nr_int = int(bil_nr)

    lager_int = billista[bil_nr_int-1].getLager()
    lager_string = str(lager_int)

    if lager_int > 0:
        print(f"\nEn {billista[bil_nr_int-1].color} {billista[bil_nr_int-1].fabrikat} kommer här! \n\t")

        #minskar saldo på lager
        nytt_lagersaldo_int = lager_int - 1
        nytt_lagersaldo_str = int(nytt_lagersaldo_int)
        #minskar lager för bil-objekt
        billista[bil_nr_int-1].setLager(nytt_lagersaldo_int)

    else : 
        print(f"Tyvärr slut på biltypen {billista[bil_nr_int-1].fabrikat}")


    print(f"Lager saldo före: {lager_string} st")
    print(f"Lager saldo efter {nytt_lagersaldo_str}")
    print("--------------------------------------")

    go = input("vill du avsluta programmet? j/n")

    if (go == "j"):
        break