CREATE  SCHEMA mabdd;
 
USE mabdd;
 
create table super (
    id int primary key,
    nom varchar(30)
);
 
create table addresse (
    id int primary key,
    ville varchar(30),
    codepostale int,
    rue varchar(30),
    numero int
);
 
INSERT INTO addresse (id, ville, codepostale, rue, numero)
VALUES (1, "lille", 59000,"bg",20);
 
INSERT INTO addresse (id, ville, codepostale, rue, numero)
VALUES (2, "roubaix", 59100,"bg",23);
 
create table utilisateurs (
    id int primary key,
    nom varchar(30),
    prenom varchar(30),
    Idville int not null,
    index ville_id (Idville),
    FOREIGN KEY (Idville) REFERENCES addresse(id)
);
 
INSERT INTO utilisateurs (id, nom, prenom,Idville)
VALUES (1, "Balkiss", "Hamad",1);
 
INSERT INTO utilisateurs (id, nom, prenom,Idville)
VALUES (2, "Martial", "Ndika",2);
 
INSERT INTO utilisateurs (id, nom, prenom,Idville)
VALUES (3, "Pierre", "Capellari",1);
 
INSERT INTO utilisateurs (id, nom, prenom,Idville)
VALUES (4, "Julien", "Decot",2);