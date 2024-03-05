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

--Oppretter tabeller

--ENTITETSKLASSER--

create table Teater(
    teaternavn  varchar(40) not null,
    constraint teaternavn_pk primary key (teaternavn)
);


CREATE TABLE TeaterSal(
    teaternavn varchar(40) not null,
    salnavn varchar(40) not null,
    constraint teaternavn_fk foreign key (teaternavn)
        references teater(teaternavn)
        on update cascade
        on delete cascade,
    constraint teaternavn_salnavn_pk primary key(teaternavn, salnavn)
    
);

create table Teaterstykke(
    stykkeid  integer not null,
    tittel  varchar(40),
    teaternavn varchar(40) not null,
    salnavn varchar(40) not null,
    constraint stykkeid_pk primary key (stykkeid),
    constraint teatersal_fk foreign key (teaternavn, salnavn) references TeaterSal(teaternavn, salnavn)(teaternavn,salnavn)
        on update cascade
        on delete set null
);

create table Akt(
    stykkeid integer not null,
    aktnr integer not null,
    navn varchar(40),
    constraint akt_pk primary key (stykkeid, aktnr),
    constraint akt_fk foreign key (stykkeid) references Teaterstykke(stykkeid)(stykkeid)
        on update cascade
        on delete set null
);


create table Person(
    pid integer not null,
    navn varchar(40),
    ansattstatus varchar(40),
    constraint pid_pk primary key (pid)
);

create table Ansatt(
    pid integer not null,
    epost varchar (40),
    constraint ansatt_pk primary key (pid),
    constraint ansatt_fk foreign key (pid) references Person(pid)
        on update cascade
        on delete set null
);


create table Rolle(
    stykkeid integer not null 
    aktnr integer not null
    rollenavn varchar(40) not null
    constraint rolle_pk primary key (stykkeid, aktnr, rollenavn)
    constraint akt_fk foreign key (stykkeid, aktnr) references Akt(stykkeid, aktnr)
        on update cascade
        on delete cascade
    
    
);

create table Skuespiller(
    pid integer not null,
    constraint skuespiller_pk primary key (pid),
    constraint skuespiller_fk foreign key (pid) references Person(pid)(pid)
        on update cascade
        on delete set null -- kanskje cascade
);

create table Oppgave(
    stykkeid integer not null,
    oppgavenavn varchar(40),
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
    constraint stol_fk foreign key (teaternavn, salnavn) references TeaterSal(teaternavn,salnavn)
        on update cascade
        on delete set null
);

create table Forestilling(
    fid integer not null,
    dato DATE,
    klokkeslett TIME,
    stykkeid integer not null,
    constraint forestilling_pk primary key (fid),
    constraint stykkeid_fk foreign key (stykkeid) references Teaterstykke(stykkeid)
        on update cascade
        on delete set null,
);

create table Kundegruppe(
    navn varchar(40) not null,
    minimumantall integer,
    constraint kundegruppe_pk primary key (navn)
);

create table Billettkjop(
    kjopid integer not null,
    dato DATE,
    tid TIME, 
    kundeid integer not null,
    constraint billettkjop primary key (kjopid),
    constraint kundeid_fk foreign key (kundeid) references Kunde(kundeid)
        on update cascade
        on delete set null,
);

create table Kunde(
    kundeid integer,
    navn VARCHAR(30) not null,
    mobilnummer integer(8),
    postnummer integer(4) not null,
    gatenavn varchar(40),
    gatenummer integer,
    constraint kunde_pk primary key (kundeid),
    constraint kunde_fk1 foreign key (postnr) references poststeder(postnr)
		on update cascade
		on delete set null

);
create table poststeder(
    postnr 		char(4),
	poststed 	varchar(30) not null,
	constraint 	poststeder_pk primary key (postnr) 
    
);

-- RELASJONSKLASSER --

CREATE TABLE UtforesAv (
    stykkeid INTEGER NOT NULL,
    oppgavenavn VARCHAR(40) NOT NULL,
    pid INTEGER NOT NULL,
    
    CONSTRAINT utforesav_pk PRIMARY KEY (stykkeid, oppgavenavn, pid),
    CONSTRAINT fk_UtforesAv_oppgavenavn FOREIGN KEY (stykkeid, oppgavenavn) REFERENCES Oppgave(stykkeid, oppgavenavn) 
        on update cascade
        on delete set null,
    CONSTRAINT fk_UtforesAv_Pid FOREIGN KEY (pid) REFERENCES Ansatt(pid)
        on update cascade
        on delete set null,
);


CREATE TABLE HarKundeGruppe (
    kundegruppe INTEGER NOT NULL,
    stykkeID INTEGER NOT NULL,
    pris DECIMAL(10, 2) NOT NULL,
    
    CONSTRAINT pk_HarKundeGruppe PRIMARY KEY (Kundegruppe, StykkeID),
    CONSTRAINT fk_HarKundeGruppe_Kundegruppe FOREIGN KEY (Kundegruppe) REFERENCES Kundegruppe(Kundegruppe)
        on update cascade
        on delete set null,
    CONSTRAINT fk_HarKundeGruppe_StykkeID FOREIGN KEY (StykkeID) REFERENCES TeaterStykke(StykkeID)
        on update cascade
        on delete set null,
);



create table SkuespillerIRolle(
    pid integer not null,
    stykkeid integer not null,
    aktnr integer not null,
    rollenavn varchar(40) not null,
    constraint skuespillerirolle_pk primary key (pid, stykkeid, aktnr, rollenavn)
    constraint rolle_fk foreign key (stykkeid, aktnr, rollenavn) references Rolle(stykkeid, aktnr, rollenavn)
        on update cascade
        on delete set null,
    constraint pid_fk foreign key references Skuespiller(pid)
        on update cascade
        on delete set null
);


