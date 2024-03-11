import datetime
import sqlite3


def insert_postnummer(con):
    with open("postnummer.txt", "r", encoding="utf-16") as f:
        postnummer = f.readlines()

    cursor = con.cursor()
    for linje in postnummer:
        deler = linje.strip().split("\t")
        postnr1 = deler[0]
        poststed1 = deler[1]

        cursor.execute(
            "INSERT INTO Poststeder (postnr, poststed) VALUES (?, ?)",
            (postnr1, poststed1),
        )

    con.commit()


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

    insert_postnummer(con)

    billetid_count = 0
    # sett inn stoler for Hovedscenen, samt registrer kjøp tilknyttet forestillingen txt-fila representerer
    cursor.execute(
        """insert into Billettkjop values (0, '2024-03-09', '16:00:00', 0)"""
    )  # billettkjøp for å samle opp seter som er tatt i Hovedscenen
    f = open("hovedscenen.txt", "r")
    # henter ut dato for forestilling. kode hentet fra tips.txt
    dato = f.readline()
    words = dato.split()
    for word in words:
        if len(word) == 10 and word[4] == "-" and word[7] == "-":
            dato = word
    # hente ut riktig forestillings-id
    cursor.execute(
        """select fid from Forestilling where dato = ? and stykkeid = 0""", (dato,)
    )
    fid = cursor.fetchone()[0]
    stol_count = 524  # holder styr på riktig stolnummer i Hovedscenen
    # galleri seksjonen
    galleri = f.readline().strip()
    for i in range(4, 0, -1):
        line = f.readline()
        for j in range(len(line) - 2, -1, -1):
            # setter inn stolen uansett
            cursor.execute(
                """insert into Stol values ('Trøndelag Teater', 'Hovedscenen', ?, ?, ?)""",
                (
                    stol_count,
                    i,
                    galleri,
                ),
            )
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == "1":
                cursor.execute(
                    """insert into Billett values(?, ?, ?, ?, 'Hovedscenen', 'Trøndelag Teater', ?, 0, 'Ordinær')""",
                    (
                        billetid_count,
                        stol_count,
                        i,
                        galleri,
                        fid,
                    ),
                )
                billetid_count += 1
            stol_count -= 1
    # parkett seksjonen
    parkett = f.readline().strip()
    for i in range(18, 0, -1):
        line = f.readline()
        for j in range(len(line) - 2, -1, -1):
            # dersom plassen er markert x trenger vi ikke registrere den
            if line[j] == "x":
                stol_count -= 1
                continue
            # setter inn stolen uansett
            cursor.execute(
                """insert into Stol values ('Trøndelag Teater', 'Hovedscenen', ?, ?, ?)""",
                (
                    stol_count,
                    i,
                    parkett,
                ),
            )
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == "1":
                cursor.execute(
                    """insert into Billett values(?, ?, ?, ?, 'Hovedscenen', 'Trøndelag Teater', ?, 0, 'Ordinær')""",
                    (
                        billetid_count,
                        stol_count,
                        i,
                        parkett,
                        fid,
                    ),
                )
                billetid_count += 1
            stol_count -= 1
    f.close()

    # sett inn stoler for Gamle scene, samt registrer tatte stoler i forbindelse med den gitte forestillingen
    f = open("gamle-scene.txt", "r")
    # henter ut dato for forestilling. kode hentet fra tips.txt
    dato = f.readline()
    words = dato.split()
    for word in words:
        if len(word) == 10 and word[4] == "-" and word[7] == "-":
            dato = word
    # hente ut riktig forestillings-id
    cursor.execute(
        """select fid from Forestilling where dato = ? and stykkeid = 1""", (dato,)
    )
    fid = cursor.fetchone()[0]
    # galleri seksjonen
    galleri = f.readline().strip()
    for i in range(3, 0, -1):
        line = f.readline()
        for j in range(len(line) - 1, 0, -1):
            # setter inn stolen uansett
            cursor.execute(
                """insert into Stol values ('Trøndelag Teater', 'Gamle scene', ?, ?, ?)""",
                (
                    j,
                    i,
                    galleri,
                ),
            )
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == "1":
                cursor.execute(
                    """insert into Billett values(?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, 0, 'Ordinær')""",
                    (
                        billetid_count,
                        j,
                        i,
                        galleri,
                        fid,
                    ),
                )
                billetid_count += 1
    # balkong seksjonen
    balkong = f.readline().strip()
    for i in range(4, 0, -1):
        line = f.readline()
        for j in range(len(line) - 1, 0, -1):
            # setter inn stolen uansett
            cursor.execute(
                """insert into Stol values ('Trøndelag Teater', 'Gamle scene', ?, ?, ?)""",
                (
                    j,
                    i,
                    balkong,
                ),
            )
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == "1":
                cursor.execute(
                    """insert into Billett values(?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, 0, 'Ordinær')""",
                    (
                        billetid_count,
                        j,
                        i,
                        balkong,
                        fid,
                    ),
                )
                billetid_count += 1
    # parkett seksjonen
    parkett = f.readline().strip()
    for i in range(10, 0, -1):
        line = f.readline()
        for j in range(len(line) - 1, 0, -1):
            # setter inn stolen uansett
            cursor.execute(
                """insert into Stol values ('Trøndelag Teater', 'Gamle scene', ?, ?, ?)""",
                (
                    j,
                    i,
                    parkett,
                ),
            )
            # dersom stolen er tatt, registrer kjøpet for forestillingen
            if line[j] == "1":
                cursor.execute(
                    """insert into Billett values(?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, 0, 'Ordinær')""",
                    (
                        billetid_count,
                        j,
                        i,
                        parkett,
                        fid,
                    ),
                )
                billetid_count += 1
    con.commit()
    con.close()


def brukerhistorie3():
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()

    # Henter nåværende dato og tid
    naa = datetime.datetime.now()
    dato = naa.strftime("%Y-%m-%d")
    tidspunkt = naa.strftime("%H:%M:%S")

    # finner den nåværende høyeste kjøpid og legge til 1 for det nye kjøpet
    cursor.execute(""" select max(kjopid) FROM Billettkjop""")
    max_id = cursor.fetchone()[0]
    ny_kjopid = (
        max_id + 1 if max_id is not None else 0
    )  # Starter på 0 hvis tabellen er tom

    # opprette et kjøp for de ni billettene med default bruker og bruker ny_kjopid for kjøpet
    cursor.execute(
        """insert into Billettkjop values (?, ?, ?, 0)""", (ny_kjopid, dato, tidspunkt)
    )
    # finner fid
    cursor.execute(
        """select fid from Forestilling where dato = '2024-02-03' and stykkeid = 1"""
    )
    fid = cursor.fetchone()[0]
    # finner rad med ni ledige plasser
    cursor.execute(
        """select Stol.radnr, Stol.omrode
                        from Stol
                        left join Billett
                            on Stol.salnavn = Billett.salnavn
                            and Stol.teaternavn = Billett.teaternavn
                            and Stol.stolnr = Billett.stolnr
                            and Stol.radnr = Billett.radnr
                            and Stol.omrode = Billett.omrode
                            and Billett.fid = ?
                        where Stol.teaternavn = 'Trøndelag Teater' and Stol.salnavn = 'Gamle scene'
                        group by Stol.radnr, Stol.omrode
                        having (count(*)-count(Billett.billettid)) >= 9""",
        (fid,),
    )
    rad = cursor.fetchone()
    if not rad:
        print("\n\nFant ikke ni billetter på samme rad.\n\n")
        return
    # kjøper ni billetter på raden vi fant
    cursor.execute(
        """select stolnr
                        from Stol 
                        where Stol.salnavn = 'Gamle scene' and Stol.omrode = ? and Stol.radnr = ? and not exists(
                            select stolnr
                            from Billett
                            where fid = ?
                                and Billett.stolnr = Stol.stolnr
                                and Billett.radnr = Stol.radnr
                                and Billett.salnavn = Stol.salnavn
                                and Billett.omrode = Stol.omrode)""",
        (
            rad[1],
            rad[0],
            fid,
        ),
    )
    billetter = cursor.fetchmany(9)
    if not billetter:
        print("\n\nFant ikke ni billetter på samme rad.\n\n")
        return
    print("\n\nKjøpte billetter:\n\n")

    # finner den nåværende høyeste billettid og legg til 1 for den første nye billetten
    cursor.execute("""select max(billettid) from Billett""")
    max_billettid = cursor.fetchone()[0]
    ny_billettid = max_billettid + 1 if max_billettid is not None else 0
    for billett in billetter:
        cursor.execute(
            """insert into Billett values (?, ?, ?, ?, 'Gamle scene', 'Trøndelag Teater', ?, ?, 'Ordinær')""",
            (ny_billettid, billett[0], rad[0], rad[1], fid, ny_kjopid),
        )  # antar ordinære billetter
        print(
            f"Billett-id: {ny_billettid}. Stol: {billett[0]} Rad: {rad[0]}. Område: {rad[1]}"
        )
        ny_billettid += 1

    cursor.execute(
        """select pris from Harkundegruppe where stykkeid = 1 and kundegruppe = 'Ordinær'"""
    )
    pris = cursor.fetchone()[0]
    print(f"\nPrisen er totalt {9*pris} kr.")
    con.commit()
    con.close()
    print("\n")


def brukerhistorie4(dato):
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # henter ut forestillinger på gitt dato
    cursor.execute(
        """select fid, tittel from Forestilling join Teaterstykke using(stykkeid) where dato = ?""",
        (str(dato),),
    )
    plays = cursor.fetchall()
    # sjekker om spørringen gir et svar
    if not plays:
        print("\n\nDet er ingen forestillinger på denne datoen.\n\n")
        return
    # dersom spørringen ikke er tom
    print(f"\n\nForestillinger på {dato}:\n")
    for play in plays:
        # finner solgte billetter for hver forestilling på gitt datp
        cursor.execute(
            """select count(billettid) from Billett where fid = ?""", (play[0],)
        )
        sold = cursor.fetchone()[0]
        print(f"Forestilling: '{play[1]}'. Solgte billetter: {sold}")
    print("\n")
    con.close()


def brukerhistorie5():
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # henter ut stykke, skuespiller og rolle. distinct for å unngå redundans i output som vi ikke er interessert i
    cursor.execute(
        """select distinct tittel, navn, rollenavn
                        from SpillerRolle
                        join Teaterstykke using(stykkeid)
                        join Person using(pid)"""
    )
    res = cursor.fetchall()
    if not res:
        print("\n\nFant ingen forestillinger, skuespllere eller roller\n\n")
        return
    print(
        "\n\nListe over skuespillere som opptrer i de ulike stykkene med tilhørende rolle:\n"
    )
    # skriver ut resultatet
    for i in res:
        print(f"Forestilling: '{i[0]}'. Skuespiller: {i[1]}. Rolle: {i[2]}")
    print("\n")
    con.close()


def brukerhistorie6():
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # henter ut hvilke foretillinger som har solgt best, sortert synkende
    cursor.execute(
        """ select tittel, dato, count(billettid)
                        from Forestilling
                        join Teaterstykke using(stykkeid)
                        left join Billett using(fid)
                        group by fid
                        order by count(billettid) desc"""
    )
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


def brukerhistorie7(skuespiller):
    con = sqlite3.connect("teater.db")
    cursor = con.cursor()
    # hente ut hvilke skuespillere den gitte skuespilleren har spilt med i samme akt, og i hvilket stykke
    cursor.execute(
        """select distinct t.tittel, s1.navn, s2.navn
                        from SpillerRolle as sr
                        join Person as s1 using(pid)
                        join Teaterstykke as t using(stykkeid) 
                        join (select * 
                                from SpillerRolle as sr2
                                join Person as p using(pid)
                                join Teaterstykke as t2 using(stykkeid)) as s2
                            on s2.stykkeid = t.stykkeid
                        where s1.navn = ? and s1.navn != s2.navn and sr.aktnr = s2.aktnr""",
        (skuespiller,),
    )
    res = cursor.fetchall()
    if not res:
        print(f"\n\nFant ikke skuespillere som spiller med {skuespiller}\n\n")
        return
    # skriver ut resultater
    print(
        f"\n\nSkuespillere som har spilt i samme akt i samme teaterstykke som {skuespiller}:\n"
    )
    for i in res:
        print(f"{i[1]} spiller sammen med {i[2]} i '{i[0]}'.")
    print("\n")
    con.close()


if __name__ == "__main__":
    create_db()  # brukerhistorie 1 og 2
    # loop som tillater bruker å velge brukerhistorie de ønsker å gjøre
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
            brukerhistorie3()
        elif inp == "4":
            dato = input(
                "Skriv inn dato du ønsker å se forestillinger for på formatet yyyy-mm-dd: "
            )  # input burde valideres
            brukerhistorie4(dato)
        elif inp == "5":
            brukerhistorie5()
        elif inp == "6":
            brukerhistorie6()
        elif inp == "7":
            skuespiller = input("Skriv inn skuespilleren du ønsker: ")
            brukerhistorie7(skuespiller)
        else:
            print(
                "\nOppgi brukerhistorien som et tall som representerer en av de gitte brukerhistoriene, for eksempel '4'. For å avslutte, skriv inn '0'.\n"
            )
