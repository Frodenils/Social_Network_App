CREATE DATABASE IF NOT EXISTS social_network;
USE social_network;

DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS utilisateur;

CREATE TABLE utilisateur(
    id SERIAL NOT NULL,
    nom VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    motdepasse VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE publication(
    id SERIAL NOT NULL,
    titre VARCHAR(255),
    img VARCHAR(255),
    contenu VARCHAR(255),
    id_utilisateur INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id)
);