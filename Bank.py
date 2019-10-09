# inloggning
inloggning = 0

while inloggning == 0: # Inloggningsmenyn
    inloggning = int(input("Vill du logga in [1], eller skapa konto [2]? ")) # logga in eller skapa konto
    if inloggning == 1: # Logga in, kan inte spara skapade konton är så alla inloggningar fungerar
        användarnamn = input("Skriv in ditt användarnamn: ").lower() # Användarnamn får värdet av inputen, och omvandlas till små bokstäver
        lösenord = input("Skriv in ditt lösenord: ") # lösenordet får värdet av inputen
    elif inloggning == 2: # Skapa konto
        while True: # Loopar tills kontot är klart
            inloggning = 0
            print("Då skapar vi ett konto!")
            användarnamn = input("Skriv in ett användarnamn: ").lower() # Det nya användarnamnet är inputen, kan dock inte spara detta än
            lösenord1 = input("Skriv in ett lösenord: ") 
            lösenord2 = input("Skriv in lösenordet igen: ")

            if lösenord1 != lösenord2: # Lösenord1 och lösenord2 måste överrensstämma, annars måste du göra om hela kontot
                print("Lösenorden överensstämmer inte, du måste börja om med skapandet av kontot på grund av säkerhetsskäl.")
                inloggning = 2 # Startar om kontoskapandet
            
            else:
                break # Bryter loopen när kontot har lyckats skapats
    else:
        inloggning = 0 # Går tillbaka till första menyn där du kan välja att logga in


# Huvudmeny
try: # försöker öppna en befintlig fil med namnet saldo för att läsa in ifrån
    saldoFil = open("saldo.txt", "r")
    saldo = float(saldoFil.readline())
    saldoFil.close()
except: # Finns ingen fil skapar den en ny fil som heter saldo.txt med 0 kronor till en början
    saldoFil = open("saldo.txt", "w+")
    saldoFil.write(str(0))
    saldoFil.close()

menu = 0
while menu == 0:
    menu = int(input("Insättning [1], uttag [2], övrigt [3], avsluta [4]: ")) # Vad du vill göra närdu loggat in, skriver du något annat än ett heltal så går den tillbaka med hjälp av Else satsen längre ned
    if menu == 1: # Insättning
        insättning = float(input("Hur mycket vill du sätta in? ")) # Insättningen är en float, vilket gör att du kan skriva decimaltal
        saldo = saldo + insättning # räknar ut det nya saldot

        saldoFil = open("saldoFil", "w") # Skriver det nya saldot till saldo.txt
        saldoFil.write(str(saldo)) # Försöker skriva det nya saldot till filen
        saldoFil.close() # Stänger saldofilen

        print("Du har nu", saldo, "kronor på ditt konto") # Skriver ut värdet i saldofilen
        menu = 0 # Går tillbaka till huvudmenyn så du kan fortsätta sätta in/ta ut

    elif menu == 2: # Uttag
        uttag = float(input("Hur mycket vill du ta ut? "))
        saldo = saldo - uttag

        saldoFil = open("saldoFil", "w")
        saldoFil.write(str(saldo))
        saldoFil.close()

        if saldo < 0: # Om du har negativt saldo får du en varning om att pengarna är slut
            print("Oops nu har du inga pengar kvar")
            menu = 0
        print("Du har", saldo, "kronor kvar, sätt in mer pengar så att saldot blir positivt!")
        menu = 0
    
    elif menu == 3: # Inte gjort något här än men här kan fler funktioner läggas in
        print("HEJ")

    elif menu == 4: # Stänger av
        print("BYE BYE")
        exit()

    else:
        menu = 0 # Backar tillbaka till huvudmenyn ifall du stavar fel någonstans