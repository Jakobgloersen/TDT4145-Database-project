import sqlite3

# lager db fil hvis ikke allerede eksisterer
f = open("teater.db", "w")
# lager tabeller fra teater.sql
with open("teater.sql", "r") as create_sql:
    create_script = create_sql.read()
con = sqlite3.connect("teater.db")
cursor = con.cursor()
cursor.executescript(create_script)
# leser inn sql script og setter inn i tabeller
with open("insert_teater.sql", "r") as insert_sql:
    insert_script = insert_sql.read()
cursor.executescript(insert_script)

# leser inn postnummer fra txt-fil og setter inn i Poststedertabellen
with open("postnummer.txt", "r", encoding="utf-16") as f:
    postnummer = f.readlines()
for linje in postnummer:
    deler = linje.strip().split("\t")
    postnr1 = deler[0]
    poststed1 = deler[1]

    cursor.execute(
        "INSERT INTO Poststeder (postnr, poststed) VALUES (?, ?)",
        (postnr1, poststed1),
    )

con.commit()
con.close()
