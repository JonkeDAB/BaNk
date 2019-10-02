# inloggning
inloggning = 0

while inloggning == 0:
    inloggning = int(input("Vill du logga in [1], eller skapa konto [2]? "))
    if inloggning == 1: # Logga in
        användarnamn = input("Skriv in ditt användarnamn: ").lower()
        lösenord = input("Skriv in ditt lösenord: ")
    elif inloggning == 2: # Skapa konto
        while True:
            inloggning = 0
            print("Då skapar vi ett konto!")
            användarnamn = input("Skriv in ett användarnamn: ").lower()
            lösenord1 = input("Skriv in ett lösenord: ")
            lösenord2 = input("Skriv in lösenordet igen: ")

            if lösenord1 != lösenord2: # Ifall lösenordet inte överresnstämmer när du skapar kontot
                print("Lösenorden överensstämmer inte, du måste börja om med skapandet av kontot på grund av säkerhetsskäl.")
                inloggning = 2
            
            else:
                break
    else:
        inloggning = 0


# Insättning/ Uttag
saldoFil = open("saldo.txt", "r+")
saldo = float(saldoFil.readline())
menu = 0
while menu == 0:
    menu = int(input("Insättning [1], uttag [2], övrigt [3], avsluta [4]: "))
    if menu == 1: # Insättning
        insättning = float(input("Hur mycket vill du sätta in? "))
        saldo = saldo + insättning

        saldoFil.write(str(saldo))
        saldoFil.close()
        print(saldo)
        menu = 0

    elif menu == 2: # Uttag
        uttag = float(input("Hur mycket vill du ta ut? "))
        balance = saldo = saldo - uttag
        if saldo < 0:
            print("Oops nu har du inga pengar kvar")
            menu = 0
        print(saldo)
        menu = 0
    
    elif menu == 3:
        print("HEJ")

    elif menu == 4: # Stänger av
        print("BYE BYE")
        exit()

    else:
        menu = 0