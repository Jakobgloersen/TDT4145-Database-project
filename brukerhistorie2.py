import sqlite3


con = sqlite3.connect("teater.db")
cursor = con.cursor()


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
