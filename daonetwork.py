from psycopg2.extras import RealDictCursor

from psycopg2 import connect

def connection():
    cnx = connect(
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432,
        database="social_network",
    )
    return cnx



def get_utilisateur_dao(id_utilisateur: int):
    cnx = connection()
    with cnx:
        with cnx.cursor(cursor_factory=RealDictCursor) as cur:
            sql="""
                SELECT *
                FROM utilisateur
                WHERE id_utilisateur = %(id_utilisateur)s
            """
            cur.execute(sql,{"id_utilisateur": id_utilisateur})
            result = cur.fetchall
    cnx.close
    return result

def create_user(nom: str, mail: str, mdp: str):
    cnx = connection()
    with cnx:
        with cnx.cursor(cursor_factory=RealDictCursor) as cur :
            sql="""
                INSERT INTO utilisateur(
                    nom,
                    mail,
                    motdepasse
                )
                VALUES(
                    %(nom)s,
                    %(mail)s,
                    %(mdp)s
                )
                RETURNING *
            """
            cur.execute(sql,{
                "nom":nom, 
                "mail":mail, 
                "mdp":mdp})
            result = cur.fetchone
    cnx.close()
    return result
