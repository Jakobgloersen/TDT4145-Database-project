import datetime
import sqlite3

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
    exit(0)
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
    exit(0)
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
