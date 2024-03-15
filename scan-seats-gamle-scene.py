import sqlite3

con = sqlite3.connect("teater.db")
cursor = con.cursor()

cursor.execute("""select max(billettid) from Billett""")
billetid_count = cursor.fetchone()[0] + 1

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
f.close()

con.commit()
con.close()