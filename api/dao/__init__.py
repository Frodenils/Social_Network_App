from contextlib import contextmanager, closing

from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from pydantic import BaseSettings, SecretStr


class BddConfig(BaseSettings):
    bdd_host: str
    bdd_port: int
    bdd_name: str
    bdd_user: str
    bdd_pass: SecretStr


# Connection à la BDD
def connection():
    config = BddConfig()

    conn = connect(
        user=config.bdd_user,
        password=config.bdd_pass.get_secret_value(),
        host=config.bdd_host,
        port=config.bdd_port,
        database=config.bdd_name,
    )
    return conn


@contextmanager
def bdd() -> RealDictCursor:
    with closing(connection()) as cnx:
        cnx.autocommit = True
        with cnx.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
