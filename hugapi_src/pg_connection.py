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

class PgConnection():
    def __init__(self):
        connection = None
        try:
            self.params = config()
            self.connection = psycopg2.connect(**params)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot connect to database")

    def create(self, nameStore, addressStore):
        createQuery = ("INSERT INTO store(name, address) VALUES (%s,%s,%s) RETURNING store_id", (nameStore, addressStore))
        self.cursor.execute(createQuery)

if __name__ == '__main__':
    pgConnection = PgConnection()
    pgConnection.create(nameStore, addressStore)
