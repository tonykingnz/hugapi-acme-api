import psycopg2
from configparser import ConfigParser
import xxhash
import random
from datetime import datetime

name = "'Test name create row sadasdsdas'"
address = "'Test address st 3294u23ohrwekidsad'"

actual_date = datetime.now()
actual_date = int(actual_date.strftime('%Y%m%d%H%M%s%f'))

store_id = xxhash.xxh64(name+address, seed=actual_date*random.randint(0,1024)).hexdigest()
store_id = "'{0}'".format(store_id)
print(store_id)

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
    
def connect():
    conn = None
    try:
        #Config conection
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        #Create row
        cur.execute("INSERT INTO store(name, address, store_id) VALUES ({0},{1},{2});".format(name,address,store_id))
        status_confirmation= cur.fetchone()
        print(status_confirmation)

        #Check created row
        cur.execute("SELECT %s FROM store;", store_id)
        creation_confirmation = cur.fetchone()
        print(creation_confirmation)

        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(db_version)

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
