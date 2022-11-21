DROP TABLE IF EXISTS publication;
DROP TABLE IF EXISTS utilisateur;

CREATE TABLE utilisateur(
    id_utilisateur SERIAL NOT NULL,
    nom VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    motdepasse VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_utilisateur)
);

CREATE TABLE publication(
    id_publication SERIAL NOT NULL,
    titre VARCHAR(255),
    img VARCHAR(255),
    contenu VARCHAR(255),
    id_utilisateur BIGINT NOT NULL,
    PRIMARY KEY (id_publication),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
);