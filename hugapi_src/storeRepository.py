import psycopg2
from connect import connect

def create(name, address):
    connect(name, address)
def list(name, address, pageSize, pageIndex, orderBy):
    connection = psycopg2.connect(user = "postgres", password = "postgres", host = "hug-acme-api-store_acme-db-postgres_1", port = "5432", database = "acme-db")
    rs = connection.query("""
        select 
            * 
        from 
            store 
        where 
            (${name} is null or name like ${name}||'%')
            and 
            (${address} is null or name like ${address}||'%')
            and
            (${storeId} is null or storeId = ${storeId})
        limit ${pageSize} + 1 offset ${pageIndex} * ${pageSize}
    """)
    content = []
    for item in rs:
        content[i] = rs.resolve()
    lastPage = true
    if content.size > pageSize:
        lastPage = false
        content.removeLastElement()
    return PageList(content, pageSize, pageIndex. lastPage)
