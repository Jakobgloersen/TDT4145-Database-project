-- direktør
insert into Person
values (0, 'Lars Kirksæther'); --Hentet direktør fra Trøndelag teater sine nettsider
insert into Ansatt
values (0, 'lars@gmail.com', 'fulltid');
-- teater
insert into Teater
values ('Trøndelag Teater', 0);
-- teatersal
insert into Teatersal
values ('Trøndelag Teater', 'Hovedscenen', 516);
insert into Teatersal
values ('Trøndelag Teater', 'Gamle scene', 332);
-- teaterstykker
insert into Teaterstykke
values (
        0,
        'Kongsemnene',
        'Trøndelag Teater',
        'Hovedscenen'
    );
insert into Teaterstykke
values (
        1,
        'Størst av alt er kjærligheten',
        'Trøndelag Teater',
        'Gamle scene'
    );
-- kundegrupper
insert into Kundegruppe(kundegruppe)
values ('Ordinær');
insert into Kundegruppe(kundegruppe)
values ('Honnør');
insert into Kundegruppe(kundegruppe)
values ('Student');
insert into Kundegruppe(kundegruppe)
values ('Barn');
insert into Kundegruppe
values ('Gruppe 10', 10);
insert into Kundegruppe
values ('Gruppe honnør 10', 10);
-- Kundegrupper for teaterstykkene
insert into Harkundegruppe
values ('Ordinær', 0, 450.00);
insert into Harkundegruppe
values ('Honnør', 0, 380.00);
insert into Harkundegruppe
values ('Student', 0, 280.00);
insert into Harkundegruppe
values ('Gruppe 10', 0, 420.00);
insert into Harkundegruppe
values ('Gruppe honnør 10', 0, 360.00);
insert into Harkundegruppe
values ('Ordinær', 1, 350.00);
insert into Harkundegruppe
values ('Honnør', 1, 300.00);
insert into Harkundegruppe
values ('Student', 1, 220.00);
insert into Harkundegruppe
values ('Barn', 1, 220.00);
insert into Harkundegruppe
values ('Gruppe 10', 1, 320.00);
insert into Harkundegruppe
values ('Gruppe honnør 10', 1, 270.00);
-- akter, fant ingen navn på aktene umiddelbart
insert into Akt(stykkeid, aktnr)
values (0, 1);
insert into Akt(stykkeid, aktnr)
values (0, 2);
insert into Akt(stykkeid, aktnr)
values (0, 3);
insert into Akt(stykkeid, aktnr)
values (0, 4);
insert into Akt(stykkeid, aktnr)
values (0, 5);
insert into Akt(stykkeid, aktnr)
values (1, 1);
-- antar at Størst av alt er kjærligheten har en akt
-- forestillinger
insert into Forestilling
values (0, '2024-02-01', '19:00:00', 0);
insert into Forestilling
values (1, '2024-02-02', '19:00:00', 0);
insert into Forestilling
values (2, '2024-02-03', '19:00:00', 0);
insert into Forestilling
values (3, '2024-02-05', '19:00:00', 0);
insert into Forestilling
values (4, '2024-02-06', '19:00:00', 0);
insert into Forestilling
values (5, '2024-02-03', '18:30:00', 1);
insert into Forestilling
values (6, '2024-02-06', '18:30:00', 1);
insert into Forestilling
values (7, '2024-02-07', '18:30:00', 1);
insert into Forestilling
values (8, '2024-02-12', '18:30:00', 1);
insert into Forestilling
values (9, '2024-02-13', '18:30:00', 1);
insert into Forestilling
values (10, '2024-02-14', '18:30:00', 1);
-- skuespillere for Kongsemnene 
insert into Person
values (1, 'Arturo Scotti');
insert into Skuespiller
values (1);
insert into Person
values (2, 'Ingunn Beate Strige Øyen');
insert into Skuespiller
values (2);
insert into Person
values (3, 'Hans Petter Nilsen');
insert into Skuespiller
values (3);
insert into Person
values (4, 'Madeleine Brandtzæg Nilsen');
insert into Skuespiller
values (4);
insert into Person
values (5, 'Synnøve Fossum Eriksen');
insert into Skuespiller
values (5);
insert into Person
values (6, 'Emma Caroline Deichmann');
insert into Skuespiller
values (6);
insert into Person
values (7, 'Thomas Jensen Takyi');
insert into Skuespiller
values (7);
insert into Person
values (8, 'Per Bogstad Gulliksen');
insert into Skuespiller
values (8);
insert into Person
values (9, 'Isak Holmen Sørensen');
insert into Skuespiller
values (9);
insert into Person
values (10, 'Fabian Heidelberg Lunde');
insert into Skuespiller
values (10);
insert into Person
values (11, 'Emil Olafsson');
insert into Skuespiller
values (11);
insert into Person
values (12, 'Snorre Ryen Tøndel');
insert into Skuespiller
values (12);
-- roller for Kongsemnene
insert into Rolle
values (0, 1, 'Håkon Haakonssønn');
insert into Rolle
values (0, 2, 'Håkon Haakonssønn');
insert into Rolle
values (0, 3, 'Håkon Haakonssønn');
insert into Rolle
values (0, 4, 'Håkon Haakonssønn');
insert into Rolle
values (0, 5, 'Håkon Haakonssønn');
insert into Rolle
values (0, 1, 'Dagfinn Bonde');
insert into Rolle
values (0, 2, 'Dagfinn Bonde');
insert into Rolle
values (0, 3, 'Dagfinn Bonde');
insert into Rolle
values (0, 4, 'Dagfinn Bonde');
insert into Rolle
values (0, 5, 'Dagfinn Bonde');
insert into Rolle
values (0, 1, 'Skurle Jarl');
insert into Rolle
values (0, 2, 'Skurle Jarl');
insert into Rolle
values (0, 3, 'Skurle Jarl');
insert into Rolle
values (0, 4, 'Skurle Jarl');
insert into Rolle
values (0, 5, 'Skurle Jarl');
insert into Rolle
values (0, 1, 'Paal Flida');
insert into Rolle
values (0, 2, 'Paal Flida');
insert into Rolle
values (0, 3, 'Paal Flida');
insert into Rolle
values (0, 4, 'Paal Flida');
insert into Rolle
values (0, 5, 'Paal Flida');
insert into Rolle
values (0, 1, 'Gregorius Jonsson');
insert into Rolle
values (0, 2, 'Gregorius Jonsson');
insert into Rolle
values (0, 3, 'Gregorius Jonsson');
insert into Rolle
values (0, 4, 'Gregorius Jonsson');
insert into Rolle
values (0, 5, 'Gregorius Jonsson');
insert into Rolle
values (0, 1, 'Margrete');
insert into Rolle
values (0, 2, 'Margrete');
insert into Rolle
values (0, 3, 'Margrete');
insert into Rolle
values (0, 4, 'Margrete');
insert into Rolle
values (0, 5, 'Margrete');
insert into Rolle
values (0, 4, 'Jatgeir Skald');
insert into Rolle
values (0, 1, 'Sigrid');
insert into Rolle
values (0, 2, 'Sigrid');
insert into Rolle
values (0, 5, 'Sigrid');
insert into Rolle
values (0, 4, 'Ingeborg');
insert into Rolle
values (0, 1, 'Guttorm Ingesson');
insert into Rolle
values (0, 1, 'Inga frå Vartejg');
insert into Rolle
values (0, 3, 'Inga frå Vartejg');
insert into Rolle
values (0, 1, 'Ragnhild');
insert into Rolle
values (0, 5, 'Ragnhild');
insert into Rolle
values (0, 1, 'Biskop Nikolas');
insert into Rolle
values (0, 2, 'Biskop Nikolas');
insert into Rolle
values (0, 3, 'Biskop Nikolas');
insert into Rolle
values (0, 3, 'Peter');
insert into Rolle
values (0, 4, 'Peter');
insert into Rolle
values (0, 5, 'Peter');
insert into Rolle
values (0, 1, 'Baard Bratte'); -- antar at Baard Bratte rollen kun er med i akt 1
-- SpillerRolle for Kongsemnene
insert into SpillerRolle
values (1, 0, 1, 'Håkon Haakonssønn');
insert into SpillerRolle
values (1, 0, 2, 'Håkon Haakonssønn');
insert into SpillerRolle
values (1, 0, 3, 'Håkon Haakonssønn');
insert into SpillerRolle
values (1, 0, 4, 'Håkon Haakonssønn');
insert into SpillerRolle
values (1, 0, 5, 'Håkon Haakonssønn');
insert into SpillerRolle
values (11, 0, 1, 'Dagfinn Bonde');
insert into SpillerRolle
values (11, 0, 2, 'Dagfinn Bonde');
insert into SpillerRolle
values (11, 0, 3, 'Dagfinn Bonde');
insert into SpillerRolle
values (11, 0, 4, 'Dagfinn Bonde');
insert into SpillerRolle
values (11, 0, 5, 'Dagfinn Bonde');
insert into SpillerRolle
values (3, 0, 1, 'Skurle Jarl');
insert into SpillerRolle
values (3, 0, 2, 'Skurle Jarl');
insert into SpillerRolle
values (3, 0, 3, 'Skurle Jarl');
insert into SpillerRolle
values (3, 0, 4, 'Skurle Jarl');
insert into SpillerRolle
values (3, 0, 5, 'Skurle Jarl');
insert into SpillerRolle
values (9, 0, 1, 'Paal Flida');
insert into SpillerRolle
values (9, 0, 2, 'Paal Flida');
insert into SpillerRolle
values (9, 0, 3, 'Paal Flida');
insert into SpillerRolle
values (9, 0, 4, 'Paal Flida');
insert into SpillerRolle
values (9, 0, 5, 'Paal Flida');
insert into SpillerRolle
values (8, 0, 1, 'Gregorius Jonsson');
insert into SpillerRolle
values (8, 0, 2, 'Gregorius Jonsson');
insert into SpillerRolle
values (8, 0, 3, 'Gregorius Jonsson');
insert into SpillerRolle
values (8, 0, 4, 'Gregorius Jonsson');
insert into SpillerRolle
values (8, 0, 5, 'Gregorius Jonsson');
insert into SpillerRolle
values (5, 0, 1, 'Margrete');
insert into SpillerRolle
values (5, 0, 2, 'Margrete');
insert into SpillerRolle
values (5, 0, 3, 'Margrete');
insert into SpillerRolle
values (5, 0, 4, 'Margrete');
insert into SpillerRolle
values (5, 0, 5, 'Margrete');
insert into SpillerRolle
values (11, 0, 4, 'Jatgeir Skald');
insert into SpillerRolle
values (6, 0, 1, 'Sigrid');
insert into SpillerRolle
values (6, 0, 2, 'Sigrid');
insert into SpillerRolle
values (6, 0, 5, 'Sigrid');
insert into SpillerRolle
values (6, 0, 4, 'Ingeborg');
insert into SpillerRolle
values (12, 0, 1, 'Guttorm Ingesson');
insert into SpillerRolle
values (2, 0, 1, 'Inga frå Vartejg');
insert into SpillerRolle
values (2, 0, 3, 'Inga frå Vartejg');
insert into SpillerRolle
values (4, 0, 1, 'Ragnhild');
insert into SpillerRolle
values (4, 0, 5, 'Ragnhild');
insert into SpillerRolle
values (7, 0, 1, 'Biskop Nikolas');
insert into SpillerRolle
values (7, 0, 2, 'Biskop Nikolas');
insert into SpillerRolle
values (7, 0, 3, 'Biskop Nikolas');
insert into SpillerRolle
values (12, 0, 3, 'Peter');
insert into SpillerRolle
values (12, 0, 4, 'Peter');
insert into SpillerRolle
values (12, 0, 5, 'Peter');
insert into SpillerRolle
values (10, 0, 1, 'Baard Bratte');
-- skuespillere for Størst av alt er kjærlighete
insert into Person
values (13, 'Sunniva Du Mond Nordal');
insert into Skuespiller
values (13);
insert into Person
values (14, 'Jo Saberniak');
insert into Skuespiller
values (14);
insert into Person
values (15, 'Marte M. Steinholt');
insert into Skuespiller
values (15);
insert into Person
values (16, 'Tor Ivar Hagen');
insert into Skuespiller
values (16);
insert into Person
values (17, 'Trond-Ove Skrødal');
insert into Skuespiller
values (17);
insert into Person
values (18, 'Natalie Grøndahl Tangen');
insert into Skuespiller
values (18);
insert into Person
values (19, 'Åsmund Flaten');
insert into Skuespiller
values (19);
-- roller i Størst av alt er kjærligheten. Antar at de spiller seg selv
insert into Rolle
values (1, 1, 'Sunniva Du Mond Nordal');
insert into Rolle
values (1, 1, 'Jo Saberniak');
insert into Rolle
values (1, 1, 'Marte M. Steinholt');
insert into Rolle
values (1, 1, 'Tor Ivar Hagen');
insert into Rolle
values (1, 1, 'Trond-Ove Skrødal');
insert into Rolle
values (1, 1, 'Natalie Grøndahl Tangen');
insert into Rolle
values (1, 1, 'Åsmund Flaten');
-- SpillerRolle for Størst av alt er kjærligheten
insert into SpillerRolle
values (13, 1, 1, 'Sunniva Du Mond Nordal');
insert into SpillerRolle
values (14, 1, 1, 'Jo Saberniak');
insert into SpillerRolle
values (15, 1, 1, 'Marte M. Steinholt');
insert into SpillerRolle
values (16, 1, 1, 'Tor Ivar Hagen');
insert into SpillerRolle
values (17, 1, 1, 'Trond-Ove Skrødal');
insert into SpillerRolle
values (18, 1, 1, 'Natalie Grøndahl Tangen');
insert into SpillerRolle
values (19, 1, 1, 'Åsmund Flaten');
-- oppgaver
insert into Oppgave
values (0, 'Regi og musikkutvelgelse');
insert into Oppgave
values (0, 'Scenografi og kostymer');
insert into Oppgave
values (0, 'Lysdesign');
insert into Oppgave
values (0, 'Dramaturg');
insert into Oppgave
values (1, 'Regi');
insert into Oppgave
values (1, 'Scenografi og kostymer');
insert into Oppgave
values (1, 'Lysdesign');
insert into Oppgave
values (1, 'Dramaturg');
insert into Oppgave
values (1, 'Musikalsk ansvarlig');
-- ansatte og oppgaven de utfører. antar email og ansettelsesstatus
insert into Person
values (20, 'Yury Butusov');
insert into Ansatt
values(20, 'yury@gmail.com', 'fulltid');
insert into Utforesav
values (0, 'Regi og musikkutvelgelse', 20);
insert into Person
values (21, 'Aleksandr Shishkin-Hokusai');
insert into Ansatt
values(21, 'aleksandr@gmail.com', 'fulltid');
insert into Utforesav
values (0, 'Scenografi og kostymer', 21);
insert into Person
values (22, 'Eivind Myren');
insert into Ansatt
values(22, 'eivind@gmail.com', 'fulltid');
insert into Utforesav
values (0, 'Lysdesign', 22);
insert into Person
values (23, 'Mina Rype Stokke');
insert into Ansatt
values(23, 'mina@gmail.com', 'fulltid');
insert into Utforesav
values (0, 'Dramaturg', 23);
insert into Person
values (24, 'Jonas Corell Petersen');
insert into Ansatt
values(24, 'jonas@gmail.com', 'fulltid');
insert into Utforesav
values (1, 'Regi', 24);
insert into Person
values (25, 'David Gehrt');
insert into Ansatt
values(25, 'david@gmail.com', 'fulltid');
insert into Utforesav
values (1, 'Scenografi og kostymer', 25);
insert into Person
values (26, 'Magnus Mikaelsen');
insert into Ansatt
values(26, 'magnus@gmail.com', 'fulltid');
insert into Utforesav
values (1, 'Lysdesign', 26);
insert into Person
values (27, 'Kristoffer Spender');
insert into Ansatt
values(27, 'kristoffer@gmail.com', 'fulltid');
insert into Utforesav
values (1, 'Dramaturg', 27);
insert into Person
values (28, 'Gaute Tønder');
insert into Ansatt
values(28, 'gaute@gmail.com', 'fulltid');
insert into Utforesav
values (1, 'Musikalsk ansvarlig', 28);
-- fiktiv kunde for å representere de allerede kjøpte stolene
insert into Kunde
values (0, 'bruker', '00000000', '1476', 'Gate', '1');
-- vurdere å sette inn flere poststeder