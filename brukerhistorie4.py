import sqlite3

dato = input("Skriv inn dato du ønsker å se forestillinger for på formatet yyyy-mm-dd: ")  

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
    exit(0)
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
