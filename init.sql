CREATE DATABASE IF NOT EXISTS social_network;
USE social_network;

DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS utilisateur;

CREATE OR REPLACE TABLE utilisateur(
    id_utilisateur SERIAL NOT NULL,
    nom VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    motdepasse VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_utilisateur)
);

CREATE OR REPLACE TABLE publication(
    id_publication SERIAL NOT NULL,
    titre VARCHAR(255),
    img VARCHAR(255),
    contenu VARCHAR(255),
    id_utilisateur BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_publication),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
);