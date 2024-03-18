import sqlite3

skuespiller = input("Skriv inn skuespilleren du ønsker: ")

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
    exit(0)
# skriver ut resultater
print(
    f"\n\nSkuespillere som har spilt i samme akt i samme teaterstykke som {skuespiller}:\n"
)
for i in res:
    print(f"{i[1]} spiller sammen med {i[2]} i '{i[0]}'.")
print("\n")
con.close()