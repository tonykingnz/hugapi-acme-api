import psycopg2
from configparser import ConfigParser

#name = "'Test name cresdate row sadasasdf3sdsdas'"
#address = "'Test address st 3294u23ohrwekidsad'"

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
    
def connect(name, address):
    conn = None
    try:
        #Config conection
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        #Create row
        cur.execute("INSERT INTO store(name, address) VALUES (%s,%s) RETURNING store_id;", (name,address))
        store_id = cur.fetchone()
        print(store_id[0])

        #Check created row
        cur.execute("SELECT %s FROM store;", store_id)
        creation_confirmation = cur.fetchone()
        message_confirmation = "The store id is: "
        print(message_confirmation+str(creation_confirmation[0]))

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
    connect("'Test create 741100920202'", "'random addres 3489hf3bf4i3'")
