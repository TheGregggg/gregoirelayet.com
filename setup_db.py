# Gregoire Layet
# Idempotent script for seting up the postgres Database for the django app
#
import psycopg
from psycopg.sql import SQL, Identifier, Literal
from psycopg.abc import Query
from psycopg.cursor import Cursor
from psycopg.errors import DuplicateDatabase, DuplicateObject, DuplicateSchema
from pathlib import Path
import os


def get_secret_content(secret_name):
    with open(
        os.path.join(Path(__file__).resolve().parent, f"secrets/{secret_name}.txt")
    ) as f:
        content = f.read().strip()
    return content


root_db_name = "postgres"
db_root_name = "gerg_db_admin"
db_root_password = get_secret_content("db_root_user_password")

db_user_name = "gerg"
db_user_password = get_secret_content("db_user_password")

setup_db_conn = f"dbname={root_db_name} user={db_root_name} password={db_root_password} host=127.0.0.1"
setup_main_db_conn = f"dbname=gregoirelayet.com user={db_user_name} password={db_user_password} host=127.0.0.1"
setup_test_db_conn = f"dbname=test_gregoirelayet.com user={db_user_name} password={db_user_password} host=127.0.0.1"


def create_if_not_exist(cur: Cursor, query: Query, if_exist_message: str):
    try:
        cur.execute(query)
    except (DuplicateDatabase, DuplicateObject, DuplicateSchema):
        print(if_exist_message)


def create_role(cur: Cursor):
    query = SQL("""CREATE ROLE {0} WITH LOGIN PASSWORD {1}""").format(
        Identifier(db_user_name), Literal(db_user_password)
    )
    create_if_not_exist(cur, query, "Role already created")


def set_django_recommendation(cur: Cursor):
    query = SQL(
        """ALTER ROLE {name} SET client_encoding TO 'utf8';
ALTER ROLE {name} SET default_transaction_isolation TO 'read committed';
ALTER ROLE {name} SET timezone TO 'UTC';"""
    ).format(name=Identifier(db_user_name))
    cur.execute(query)


def give_role_all_perm(cur: Cursor):
    query = SQL(
        """
GRANT ALL PRIVILEGES ON DATABASE "gregoirelayet.com" TO {name};
GRANT ALL PRIVILEGES ON DATABASE "test_gregoirelayet.com" TO {name};"""
    ).format(name=Identifier(db_user_name))
    cur.execute(query)


if __name__ == "__main__":
    with psycopg.connect(
        setup_db_conn,
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            create_role(cur)
            set_django_recommendation(cur)

            create_if_not_exist(
                cur,
                'CREATE DATABASE "gregoirelayet.com"',
                "gregoirelayet.com database already exists",
            )

            create_if_not_exist(
                cur,
                'CREATE DATABASE "test_gregoirelayet.com"',
                "test_gregoirelayet.com database already exists",
            )

            give_role_all_perm(cur)

    with psycopg.connect(
        setup_main_db_conn,
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            query = SQL(
                """CREATE SCHEMA "gregoirelayet.com.schema" AUTHORIZATION {name};"""
            ).format(name=Identifier(db_user_name))
            create_if_not_exist(
                cur, query, "gregoirelayet.com.schema is already created"
            )

    with psycopg.connect(
        setup_test_db_conn,
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            query = SQL(
                """CREATE SCHEMA "gregoirelayet.com.schema" AUTHORIZATION {name};"""
            ).format(name=Identifier(db_user_name))
            create_if_not_exist(
                cur, query, "gregoirelayet.com.schema is already created"
            )
