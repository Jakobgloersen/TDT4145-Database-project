import sqlite3

def create_db():
    # lager db fil hvis ikke allerede eksisterer
    f = open("teater.db", "w")
    # lager tabeller fra teater.sql
    with open("teater.sql", "r") as create_sql:
        create_script = create_sql.read()
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    cursor.executescript(create_script)
    con.commit()
    # leser inn sql script og setter inn i tabeller
    with open("insert_teater.sql", "r") as insert_sql:
        insert_script = insert_sql.read()
    cursor.executescript(insert_script)
    con.commit()
    billetid_count = 0
    # sett inn stoler for Hovedscenen, samt registrer kjøp tilknyttet forestillingen txt-fila representerer
    cursor.execute('''insert into Billettkjop values (0, '2024-03-09', '16:00:00', 0)''') # billettkjøp for å samle opp seter som er tatt i Hovedscenen
    f = open("hovedscenen.txt", "r")
    # henter ut dato for forestilling. kode hentet fra tips.txt
    dato = f.readline()
    words = dato.split()
    for word in words:
        if len(word) == 10 and word[4] == "-" and word[7] == "-":
            dato =  word
    # hente ut riktig forestillings-id
    cursor.execute('''select fid from Forestilling where dato = ? and stykkeid = 0''', (dato,))
    fid = cursor.fetchone()[0]
    stol_count = 524 # holder styr på riktig stolnummer i Hovedscenen
    # galleri seksjonen
    galleri = f.readline().strip()
    for i in range(4, 0, -1):
        line = f.readline()
        for j in range(len(line)-2, -1, -1):
            # setter inn stolen uansett
            cursor.execute('''insert into Stol values ('Trøndelag Teater', 'Hovedscenen', ?, ?, ?)''', (stol_count, i, galleri,))
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == '1':
                cursor.execute('''insert into Billett values(?, ?, ?, ?, 'Hovedscenen', 'Trøndelag Teater', ?, 0, 'Ordinær')''', (billetid_count, stol_count, i, galleri, fid,))
                billetid_count += 1
            stol_count -= 1
    # parkett seksjonen
    parkett = f.readline().strip()
    for i in range(18, 0, -1):
        line = f.readline()
        for j in range(len(line)-2, -1, -1):
            # dersom plassen er markert x trenger vi ikke registrere den
            if line[j] == 'x':
                stol_count -= 1
                continue
            # setter inn stolen uansett
            cursor.execute('''insert into Stol values ('Trøndelag Teater', 'Hovedscenen', ?, ?, ?)''', (stol_count, i, parkett,))
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == '1':
                cursor.execute('''insert into Billett values(?, ?, ?, ?, 'Hovedscenen', 'Trøndelag Teater', ?, 0, 'Ordinær')''', (billetid_count, stol_count, i, parkett, fid,))
                billetid_count += 1
            stol_count -= 1
    f.close()

    # sett inn stoler for Gamle scene, samt registrer tatte stoler i forbindelse med den gitte forestillingen
    cursor.execute('''insert into Billettkjop values (1, '2024-03-09', '16:00:00', 0)''') # billettkjøp for å samle opp seter som er tatt i Hovedscenen
    f = open("gamle-scene.txt", "r")
    # henter ut dato for forestilling. kode hentet fra tips.txt
    dato = f.readline()
    words = dato.split()
    for word in words:
        if len(word) == 10 and word[4] == "-" and word[7] == "-":
            dato =  word
    # hente ut riktig forestillings-id
    cursor.execute('''select fid from Forestilling where dato = ? and stykkeid = 1''', (dato,))
    fid = cursor.fetchone()[0]
    # galleri seksjonen
    galleri = f.readline().strip()
    for i in range(3, 0, -1):
        line = f.readline()
        for j in range(len(line)-1, 0, -1):
            # setter inn stolen uansett
            cursor.execute('''insert into Stol values ('Trøndelag Teater', 'Gamle scene', ?, ?, ?)''', (j, i, galleri,))
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == '1':
                cursor.execute('''insert into Billett values(?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, 0, 'Ordinær')''', (billetid_count, j, i, galleri, fid,))
                billetid_count += 1
    # balkong seksjonen
    balkong = f.readline().strip()
    for i in range(4, 0, -1):
        line = f.readline()
        for j in range(len(line)-1, 0, -1):
            # setter inn stolen uansett
            cursor.execute('''insert into Stol values ('Trøndelag Teater', 'Gamle scene', ?, ?, ?)''', (j, i, balkong,))
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == '1':
                cursor.execute('''insert into Billett values(?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, 0, 'Ordinær')''', (billetid_count, j, i, balkong, fid,))
                billetid_count += 1
    # parkett seksjonen
    parkett = f.readline().strip()
    for i in range(10, 0, -1):
        line = f.readline()
        for j in range(len(line)-1, 0, -1):
            # setter inn stolen uansett
            cursor.execute('''insert into Stol values ('Trøndelag Teater', 'Gamle scene', ?, ?, ?)''', (j, i, parkett,))
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == '1':
                cursor.execute('''insert into Billett values(?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, 0, 'Ordinær')''', (billetid_count, j, i, parkett, fid,))
                billetid_count += 1
    con.commit()
    con.close()

def brukerhistorie4(dato):
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # henter ut forestillinger på gitt dato
    cursor.execute('''select fid, tittel from Forestilling join Teaterstykke using(stykkeid) where dato = ?''', (str(dato),))
    plays = cursor.fetchall()
    # sjekker om spørringen gir et svar
    if not plays:
        print("\n\nDet er ingen forestillinger på denne datoen.\n\n")
        return
    # dersom spørringen ikke er tom
    print(f"\n\nForestillinger på {dato}:\n")
    for play in plays:
        # finner solgte billetter for hver forestilling på gitt datp
        cursor.execute('''select count(billettid) from Billett where fid = ?''', (play[0],))
        sold = cursor.fetchone()[0]
        print(f"Forestilling: '{play[1]}'. Solgte billetter: {sold}")
    print("\n")
    con.close()

def brukerhistorie5():
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # henter ut stykke, skuespiller og rolle. distinct for å unngå redundans i output som vi ikke er interessert i
    cursor.execute('''select distinct tittel, navn, rollenavn
                        from SpillerRolle
                        join Teaterstykke using(stykkeid)
                        join Person using(pid)''')
    res = cursor.fetchall()
    if not res:
        print("\n\nFant ingen forestillinger, skuespllere eller roller\n\n")
        return
    print("\n\nListe over skuespillere som opptrer i de ulike stykkene med tilhørende rolle:\n")
    # skriver ut resultatet
    for i in res:
        print(f"Forestilling: '{i[0]}'. Skuespiller: {i[1]}. Rolle: {i[2]}")
    print("\n")
    con.close()

def brukerhistorie6():
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # henter ut hvilke foretillinger som har solgt best, sortert synkende
    cursor.execute(''' select tittel, dato, count(billettid)
                        from Forestilling
                        join Teaterstykke using(stykkeid)
                        left join Billett using(fid)
                        group by fid
                        order by count(billettid) desc''')
    res = cursor.fetchall()
    if not res:
        print("\n\nDet er en feil med spørringen\n\n")
        return
    # skriver ut resultatet
    print("\n\nForetillingene som har solgt best:\n")
    for i in res:
        print(f"Stykke: {i[0]}. Dato: {i[1]}. Solte billetter: {i[2]}")
    print("\n")
    con.close()

if __name__=="__main__":
    create_db()
    # loop som tillater bruker å velge brukerhistorie de ønsker å gjøre
    print()
    while(1):
        print("Brukerhistorie 4 - skriver ut forestilling og antall solgte billetter per forestilling for en gitt dato")
        print("Brukerhistorie 5 - skriver ut teaterstykkene med tilhørende skuespillere og hvilke roller de spiller i stykket")
        print("Brukerhistorie 6 - skriver ut forestillingene som har solgt best i synkende rekkefølge")
        print("Avslutt - skriv 0")
        inp = input("Skriv brukerhistorie du ønsker å utføre: ")
        if inp == "0":
            exit()
        elif inp == "4":
            dato = input("Skriv inn dato du ønsker å se forestillinger for på formatet yyyy-mm-dd: ") # input burde valideres
            brukerhistorie4(dato)
        elif inp == "5":
            brukerhistorie5()
        elif inp == "6":
            brukerhistorie6()
        else:
            print("\nOppgi brukerhistorien som et tall som representerer en av de gitte brukerhistoriene, for eksempel '4'. For å avslutte, skriv inn '0'.\n")
        