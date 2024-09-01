import psycopg2
from psycopg2 import sql
from decouple import config

connection = psycopg2.connect(
        host = config('PGSQL_HOST'),
        port = config('PGSQL_PORT'),
        database = config('PGSQL_DATABASE'),
        user = config('PGSQL_USER'),        
        password = config('PGSQL_PASSWORD')
    )

connection.set_session(autocommit=True)

def main():
    

    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM edbuser.users')
        result = cursor.fetchone()
    print(result)

#Bad example, don't do this!
def is_admin_BAD(username: str)-> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT admin
            FROM users
            WHERE username = '%s'
    """ % username)
        result = cursor.fetchone()

    if result is None:
        return False
    
    admin, = result
    return admin

#Good example!
def is_admin(username: str)-> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT admin
            FROM users
            WHERE username = %(username)s
    """, {
        'username': username
    })
        result = cursor.fetchone()

    if result is None:
        return False
    
    admin, = result
    return admin

#Bad example!
def count_rows_BAD(table_name: str) -> int:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                count(*)
            FROM
                %(table_name)s
        """, {
            'table_name': table_name,
        })
        result = cursor.fetchone()

    rowcount, = result
    return rowcount
 

# Good example!
def count_rows(schema: str, table_name: str) -> int:
    with connection.cursor() as cursor:
        stmt = sql.SQL("""
            SELECT
                count(*)
            FROM
                {schema}.{table_name}
        """).format(
            schema = sql.Identifier(schema),
            table_name = sql.Identifier(table_name), #Especificar que es un identificador (esquema, tabla, columna)
        )
        # Puede implementarse literales: sql.Literal(variable)

        print(stmt.as_string(connection))
        cursor.execute(stmt)
        
        result = cursor.fetchone()

    rowcount, = result
    return rowcount

if __name__ == '__main__':
    #main();
    #print(is_admin_BAD('edenflo'))
    #print(is_admin_BAD('mimi'))
    #print(is_admin_BAD("'; select true --"))
    #print(is_admin_BAD("'; update users set admin = 'true' where username = 'mimi'; select true; --"))
    #print(is_admin_BAD('mimi'))
    #print(is_admin('chaid'))
    #print(is_admin('mimi'))
    #print(is_admin("'; select true;--"))

    #print(count_rows_BAD('edbuser.users'))
    print(count_rows('edbuser', 'users'))
    