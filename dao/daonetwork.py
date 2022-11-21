from psycopg2.extras import RealDictCursor

from psycopg2 import connect
def connection():
    cnx = connect(
        user = "root",
        password = "root",
        host = "localhost",
        port = ""
    )



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
            result = cur.fetchone
    cnx.close
    return result

def get_all_utilisateur_dao():
    cnx = connection()
    with cnx:
        with cnx.cursor(cursor_factory=RealDictCursor) as cur:
            sql="""
                SELECT *
                FROM utilisateur
                """
            cur.execute(sql)
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