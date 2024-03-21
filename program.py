import os

if __name__ == "__main__":
    print()
    while 1:
        print(
            "Brukerhistorie 3 - kjøper ni billetter på samme rad for 'Størst av alt er kjærligheten' den 3. februar"
        )
        print(
            "Brukerhistorie 4 - skriver ut forestilling og antall solgte billetter per forestilling for en gitt dato"
        )
        print(
            "Brukerhistorie 5 - skriver ut teaterstykkene med tilhørende skuespillere og hvilke roller de spiller i stykket"
        )
        print(
            "Brukerhistorie 6 - skriver ut forestillingene som har solgt best i synkende rekkefølge"
        )
        print(
            "Brukerhistorie 7 - skriver ut hvem som har spilt med en gitt skuespiller i forestillingene den gitte skuespilleren deltar i"
        )
        print("Avslutt - skriv 0")
        inp = input("Skriv brukerhistorie du ønsker å utføre: ")
        if inp == "0":
            exit()
        elif inp == "3":
            os.system('python3 brukerhistorie3.py')
        elif inp == "4":
            os.system('python3 brukerhistorie4.py')
        elif inp == "5":
            os.system('sqlite3 teater.db < brukerhistorie5.sql')
        
        elif inp == "6":
            os.system('sqlite3 teater.db < brukerhistorie6.sql')
        elif inp == "7":
            os.system('python3 brukerhistorie7.py')
        else:
            print(
                "\nOppgi brukerhistorien som et tall som representerer en av de gitte brukerhistoriene, for eksempel '4'. For å avslutte, skriv inn '0'.\n"
            )