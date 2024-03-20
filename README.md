TDT4145 - prosjekt

# Oppskrift på kjøring av program

Under er det en detaljert beskrivelse av hvordan databaseapplikasjonen vi har iplementert kan kjøres. 

Det er allerede opprettet en tom database-fil som er kalt teater.db. 

Videre må følgende steg følges: 

1. Åpne et terminalvindu
2. Naviger til riktig mappen i terminalen.
    
    ```
    cd /tdt4145-prosjekt
    ```
4. Brukerhistorie 1 og 2 MÅ kjøres først i den gitte rekkefølgen. 
    
    ```
    python3 brukerhistorie1.py
    
    python3 brukerhistorie2.py
    ```
    
Deretter har man to valg for kjøring av programmet. 

Alternativ 1 er kjøre et program ved bruk av program.py som gir deg muligheten til å velge hvilken brukerhistorie som skal kjøres ved å taste inn et tall som input i terminalen. 

Alternativ 2 er å benytte terminalen for kjøring av hver enkelt brukerhistorie separat i terminalen. 

Begge de to alternativene forutsetter at de fire første stegene over er gjennomført. 

## Alternativ 1

1. Programmet kan startes ved å kjøre program.py-filen med følgende kommando:
    
    ```
    python3 program.py
    ```
2. Du vil da få spørsmålet om hvilken brukerhistorie du ønsker å utføre. Her kan du velge mellom brukerhistorie 3 til brukerhistorie 7 ved å skrive inn et tall mellom 3 og 7. For å avslutte programme skriver du inn ```0```
3.  Ved inntasting av ```4```, vil brukerhistorie 4 spørre om hvilken dato du ønsker å se forestillinger for. Pass på å skrive på riktig format ```yyyy-mm-dd```  

    Eksempeldata til input er: ```2024-02-03``` eller ```2024-02-12```
4. Ved inntasting av 7 vil brukerhistorie 7 spørre om hvilken skuespiller du ønsker .

    Eksempeldata til input er ```Arturo Scotti``` eller ```Madeleine Brandtzæg Nilsen```

5. De resterende brukerhistoriene vil ikke kreve noen input, og vil printe resultatet til terminalen. 


## Alternativ 2

1. Brukerhistorie 3-7 kan nå kjøres i tilfeldig rekkefølge. Under følger en forklaring på hvordan de ulike brukerhistoriene ka gjennomføres. Ved dette alternativet vil du ikke få spørsmål om hvilken brukerhistorie du ønsker å utføre
2. **Brukerhistorie 3**: 
    
    Kjør følgende kommando i terminalen: 
    
    ```
    python3 brukerhistorie3.py
    ```
    
    Brukerhistorien krever ingen input, og vil printe ut de ni bilettene som har blitt kjøpt. 
3. **Brukerhistorie 4**: 

    Kjør følgende kommando i terminalen: 
    
    ```
    python3 brukerhistorie4.py
    ```
    Du vil da få spørmsål om hvilken dato du ønsker å se forestillinger for. Pass på å skrive inputen på riktig format ```yyyy-mm-dd``` .

    Eksempeldata til input er: ```2024-02-03``` eller ```2024-02-12```

4. **Brukerhistorie 5**: 

    Følgende kommandoer må kjøres i terminalen for å utføre brukerhistorie 5:
    
    NB: Krever at sqlite3 er installert

    ```
    sqlite3 teater.db
    ```
    Dersom det er ønskelig at resultatet printes på tabellform, kan man bruke følgende kommando: 
    
    ```
    .mode table
    ```
    Videre vil følgende kommando kjøre brukerhistorien og skrive resultatet til terminalen
    
    ```
    .read brukerhistorie5.sql
    ```
    I terminalen vil dette se slik ut: 
    
    ```
    (base) kaja@Kajas-MacBook-Pro tdt4145-prosjekt 
    % sqlite3 teater.db
    SQLite version 3.41.2 2023-03-22 11:56:21
    Enter ".help" for usage hints.
    sqlite> .mode table
    sqlite> .read brukerhistorie5.sql
    ```
    Dersom man ønsker å avslutte sqlite for å kunne kjøre noen av de andre brukerhistoriene skriver man følgende: 
    
    ```
    .exit
    ```
    Vil se slik ut i terminalen:
    
    ```
    sqlite> .exit
     
    ```


5. **Brukerhistorie 6**: 
    
    Følgende kommandoer må kjøres i terminalen for å utføre brukerhistorie 5: (samme fremgangsmåte som punktet over)
    ```
    sqlite3 teater.db
    ```
    ```
    .mode table
    ```
    ```
    .read brukerhistorie6.sql
    ```
    Kommandoene vil se slik ut i terminalen:
    
    ```
    (base) kaja@Kajas-MacBook-Pro tdt4145-prosjekt 
    % sqlite3 teater.db
    SQLite version 3.41.2 2023-03-22 11:56:21
    Enter ".help" for usage hints.
    sqlite> .mode table
    sqlite> .read brukerhistorie6.sql
    ```

6. **Brukerhistorie 7**
    
    Kjør følgende kommando i terminalen: 
    
    ```
    python3 brukerhistorie7.py
    ```
    Du vil da få spørmsål om hvilken skuespiller du ønsker. 
    
    Eksempeldata til input er ```Arturo Scotti``` eller ```Madeleine Brandtzæg Nilsen```


# Tekstlige resultater 

Under vises de tekstlige resultatene (output) fra brukerhistoriene sine spørringer. For de brukerhistoriene som krever input, er det også beskrevet hvilken input som er benyttet til det tekstlige resultatet som er gitt. 


## Brukerhistorie 3

*(spørringen krever ingen input)*

**Output:**

Kjøpte billetter:


Billett-id: 89. Stol: 28 Rad: 1. Område: Balkong

Billett-id: 90. Stol: 27 Rad: 1. Område: Balkong

Billett-id: 91. Stol: 26 Rad: 1. Område: Balkong

Billett-id: 92. Stol: 25 Rad: 1. Område: Balkong

Billett-id: 93. Stol: 24 Rad: 1. Område: Balkong

Billett-id: 94. Stol: 23 Rad: 1. Område: Balkong

Billett-id: 95. Stol: 22 Rad: 1. Område: Balkong

Billett-id: 96. Stol: 21 Rad: 1. Område: Balkong

Billett-id: 97. Stol: 20 Rad: 1. Område: Balkong

Prisen er totalt 3150 kr.

## Brukerhistorie 4

**Input:** ```2024-02-03```

**Output:**

Forestillinger på 2024-02-03:

Forestilling: 'Kongsemnene'. Solgte billetter: 65

Forestilling: 'Størst av alt er kjærligheten'. Solgte billetter: 33

*NB: Output viser solgte biletter etter at brukerhistorie 3 er utført èn gang*

## Brukerhistorie 5
*(spørringen krever ingen input)*

**Output:** (Skriver ut navn på teaterstykke | Navn på skuespiller | Navn på rolle)

Kongsemnene|Arturo Scotti|Håkon Haakonssønn

Kongsemnene|Emil Olafsson|Dagfinn Bonde

Kongsemnene|Hans Petter Nilsen|Skurle Jarl

Kongsemnene|Isak Holmen Sørensen|Paal Flida

Kongsemnene|Per Bogstad Gulliksen|Gregorius Jonsson

Kongsemnene|Synnøve Fossum Eriksen|Margrete

Kongsemnene|Emil Olafsson|Jatgeir Skald

Kongsemnene|Emma Caroline Deichmann|Sigrid

Kongsemnene|Emma Caroline Deichmann|Ingeborg

Kongsemnene|Snorre Ryen Tøndel|Guttorm Ingesson

Kongsemnene|Ingunn Beate Strige Øyen|Inga frå Vartejg

Kongsemnene|Madeleine Brandtzæg Nilsen|Ragnhild

Kongsemnene|Thomas Jensen Takyi|Biskop Nikolas

Kongsemnene|Snorre Ryen Tøndel|Peter

Kongsemnene|Fabian Heidelberg Lunde|Baard Bratte

Størst av alt er kjærligheten|Sunniva Du Mond Nordal|
Sunniva Du Mond Nordal

Størst av alt er kjærligheten|Jo Saberniak|Jo Saberniak

Størst av alt er kjærligheten|Marte M. Steinholt|Marte M. Steinholt

Størst av alt er kjærligheten|Tor Ivar Hagen|Tor Ivar Hagen

Størst av alt er kjærligheten|Trond-Ove Skrødal|Trond-Ove Skrødal

Størst av alt er kjærligheten|Natalie Grøndahl Tangen|Natalie Grøndahl Tangen

Størst av alt er kjærligheten|Åsmund Flaten|Åsmund Flaten

## Brukerhistorie 6

*(spørringen krever ingen input)*

**Output:** (Skriver ut Navn på forestilling | Dato | Antall solgte biletter)

*NB: Output viser antall solgte biletter etter at brukerhistorie 3 er utført èn gang*

Kongsemnene|2024-02-03|65

Størst av alt er kjærligheten|2024-02-03|33

Kongsemnene|2024-02-01|0

Kongsemnene|2024-02-02|0

Kongsemnene|2024-02-05|0

Kongsemnene|2024-02-06|0

Størst av alt er kjærligheten|2024-02-06|0

Størst av alt er kjærligheten|2024-02-07|0

Størst av alt er kjærligheten|2024-02-12|0

Størst av alt er kjærligheten|2024-02-13|0

Størst av alt er kjærligheten|2024-02-14|0

## Brukerhistorie 7

**Input:** ```Arturo Scotti```

**Output:**

Skuespillere som har spilt i samme akt i samme teaterstykke som Arturo Scotti:

Arturo Scotti spiller sammen med Emil Olafsson i 'Kongsemnene'.

Arturo Scotti spiller sammen med Hans Petter Nilsen i 'Kongsemnene'.

Arturo Scotti spiller sammen med Isak Holmen Sørensen i 'Kongsemnene'.

Arturo Scotti spiller sammen med Per Bogstad Gulliksen i 'Kongsemnene'.

Arturo Scotti spiller sammen med Synnøve Fossum Eriksen i 'Kongsemnene'.

Arturo Scotti spiller sammen med Emma Caroline Deichmann i 'Kongsemnene'.

Arturo Scotti spiller sammen med Snorre Ryen Tøndel i 'Kongsemnene'.

Arturo Scotti spiller sammen med Ingunn Beate Strige Øyen i 'Kongsemnene'.

Arturo Scotti spiller sammen med Madeleine Brandtzæg Nilsen i 'Kongsemnene'.

Arturo Scotti spiller sammen med Thomas Jensen Takyi i 'Kongsemnene'.

Arturo Scotti spiller sammen med Fabian Heidelberg Lunde i 'Kongsemnene'.

