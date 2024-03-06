-- sletter eksisterende tabeller
drop table Teater;
drop table TeaterSal;
drop table Teaterstykke;
drop table Akt;
drop table Person;
drop table Ansatt;
drop table Skuespiller;
drop table Oppgave;
drop table Stol;
drop table Forestilling;
drop table Kundegruppe;
drop table Billettkjop;
drop table Kunde;
drop table Billett;
drop table Harkundegruppe;
drop table Poststeder;
drop table Rolle;
drop table SpillerRolle;
drop table Utforesav;

--Oppretter tabeller

--ENTITETSKLASSER--

create table Teater(
    teaternavn  varchar(40) not null,
    direktorpid integer unique, --unique for å håndtere at det ikke kan være samme direktører for forskjellige teater. 
    constraint teaternavn_pk primary key (teaternavn)
    constraint teater_fk foreign key (direktorpid) references Ansatt(pid)
        on update cascade
        on delete set null
);

CREATE TABLE Teatersal(
    teaternavn varchar(40) not null,
    salnavn varchar(40) not null,
    constraint teaternavn_fk foreign key (teaternavn) references Teater(teaternavn)
        on update cascade
        on delete cascade, -- kan ikke ha en teatersal uten et teater, derfor cascade. kan være farlig. Vurdere restrict?
    constraint teatersal_pk primary key(teaternavn, salnavn)
);

create table Teaterstykke(
    stykkeid  integer not null,
    tittel  varchar(40),
    teaternavn varchar(40),
    salnavn varchar(40),
    constraint teaterstykke_pk primary key (stykkeid),
    constraint teatersal_fk foreign key (teaternavn, salnavn) references Teatersal(teaternavn, salnavn)
        on update cascade
        on delete set null
);

create table Akt(
    stykkeid integer not null,
    aktnr integer not null,
    navn varchar(40),
    constraint akt_pk primary key (stykkeid, aktnr),
    constraint akt_fk foreign key (stykkeid) references Teaterstykke(stykkeid)
        on update cascade
        on delete set null
);


create table Person(
    pid integer not null,
    navn varchar(40),
    constraint person_pk primary key (pid)
);

create table Ansatt(
    pid integer not null,
    epost varchar(40) unique,
    ansattstatus varchar(40),
    constraint ansatt_pk primary key (pid),
    constraint ansatt_fk foreign key (pid) references Person(pid)
        on update cascade
        on delete cascade
);

create table Skuespiller(
    pid integer not null,
    constraint skuespiller_pk primary key (pid),
    constraint skuespiller_fk foreign key (pid) references Person(pid)
        on update cascade
        on delete cascade
);

create table Rolle(
    stykkeid integer not null ,
    aktnr integer not null,
    rollenavn varchar(40) not null,
    constraint rolle_pk primary key (stykkeid, aktnr, rollenavn),
    constraint rolle_fk foreign key (stykkeid, aktnr) references Akt(stykkeid, aktnr)
        on update cascade
        on delete cascade -- sletter roller hvis en akt blir slettet
);

create table Oppgave(
    stykkeid integer not null,
    oppgavenavn varchar(40) not null,
    constraint oppgave_pk primary key (stykkeid, oppgavenavn),
    constraint oppgave_fk foreign key (stykkeid) references Teaterstykke(stykkeid)
        on update cascade
        on delete set null 
);

create table Stol(
    teaternavn varchar(40) not null,
    salnavn varchar(40) not null,
    stolnr integer not null,
    radnr integer not null,
    omrode varchar(40) not null,
    constraint stol_pk primary key (teaternavn, salnavn, stolnr, radnr, omrode),
    constraint stol_fk foreign key (teaternavn, salnavn) references Teatessal(teaternavn,salnavn)
        on update cascade
        on delete set null
);

create table Forestilling(
    fid integer not null,
    dato DATE,
    klokkeslett TIME,
    stykkeid integer not null,
    constraint forestilling_pk primary key (fid),
    constraint forestilling_fk foreign key (stykkeid) references Teaterstykke(stykkeid)
        on update cascade
        on delete set null
);

create table Kundegruppe(
    kundegruppe varchar(40) not null, -- vurdere å endre dette til å hete kundegruppe? ikke så intuitivt. (Endret)
    minimumAntall integer,
    constraint kundegruppe_pk primary key (kundegruppe)
);

create table Billett(
    billettid integer not null,
    stolnr integer,
    radnr integer,
    omrode varchar(40),
    salnavn varchar(40),
    teaternavn varchar(40),
    fid integer not null,
    kjopid integer, -- 
    kundegruppe varchar(40), 
    constraint billett_pk primary key (billettid),
    constraint billett_stol_fk foreign key (stolnr, radnr, omrode, salnavn, teaternavn) references Stol(stolnr, radnr, omrode, salnavn, teaternavn)
        on update cascade
        on delete set null,
    constraint billett_kjop_fk foreign key (kjopid) references Billettkjop(kjopid)
        on update cascade
        on delete set null,
    constraint billett_forestilling_fk foreign key (fid) references Forestilling(fid)
        on update cascade
        on delete set null,
    constraint billett_kundegruppe_fk foreign key (kundegruppe) references Kundegruppe(kundegruppe)
        on update cascade
        on delete set null
);

create table Billettkjop(
    kjopid integer not null,
    dato DATE,
    tidspunkt TIME, 
    kundeid integer not null,
    constraint billettkjop_pk primary key (kjopid),
    constraint kundeid_fk foreign key (kundeid) references Kunde(kundeid)
        on update cascade
        on delete set null
);

create table Kunde(
    kundeid integer not null,
    navn varchar(40),
    mobilnummer integer(8) unique,
    postnr integer(4) not null,
    gatenavn varchar(40),
    gatenr varchar(10), -- må gjøre mulig med bokstaver
    constraint kunde_pk primary key (kundeid),
    constraint kunde_fk foreign key (postnr) references Poststeder(postnr)
		on update cascade
		on delete set null
);

create table Poststeder(
    postnr 		char(4),
	poststed 	varchar(30) not null,
	constraint 	poststeder_pk primary key (postnr) 
);

-- RELASJONSKLASSER --

create table Utforesav (
    stykkeid integer not null,
    oppgavenavn varchar(40) not null,
    pid integer not null,
    constraint utforesav_pk primary key (stykkeid, oppgavenavn, pid),
    constraint utforesav_oppgave_fk foreign key (stykkeid, oppgavenavn) references Oppgave(stykkeid, oppgavenavn) 
        on update cascade
        on delete set null,
    constraint utforesav_pid_fk foreign key (pid) references Ansatt(pid)
        on update cascade
        on delete set null
);

create table Harkundegruppe (
    kundegruppe varchar(40) not null, -- greit at dette bare heter kundegruppe, og ikke har samme navn som i kundegruppe?
    stykkeid integer not null,
    pris decimal(10, 2) not null,
    constraint harkundegruppe_pk primary key (kundegruppe, stykkeid),
    constraint har_kundegruppe_fk foreign key (kundegruppe) references Kundegruppe(kundegruppe)
        on update cascade
        on delete set null,
    constraint stykke_har_kundegruppe_fk foreign key (stykkeid) references Teaterstykke(stykkeid)
        on update cascade
        on delete set null
);

create table SpillerRolle(
    pid integer not null,
    stykkeid integer not null,
    aktnr integer not null,
    rollenavn varchar(40) not null,
    constraint spillerRolle_pk primary key (pid, stykkeid, aktnr, rollenavn)
    constraint rolle_fk foreign key (stykkeid, aktnr, rollenavn) references Rolle(stykkeid, aktnr, rollenavn)
        on update cascade
        on delete set null,
    constraint pid_i_rolle_fk foreign key (pid) references Skuespiller(pid)
        on update cascade
        on delete set null
);


