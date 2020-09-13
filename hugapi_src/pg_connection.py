import psycopg2
from configparser import ConfigParser

nameStore = "John"
addressStore = "Street 9, State, Country"

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Selection {0} not found in the {1} file'.format(section, filename))

    return db

class EntityManager():
    def __init__(self):
        params = config()
        self.connection = psycopg2.connect(**params)
        self.connection.autocommit = True
    
    def executeQuery(self, query, params):
        cursor = None
        try:
            print(query)
            print(params)
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        finally:
            if cursor is not None:
                cursor.close()

    def create(self, nameStore, addressStore):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO store(name, address) VALUES (%s,%s) RETURNING store_id", (nameStore, addressStore))

