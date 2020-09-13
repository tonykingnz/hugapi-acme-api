import psycopg2
from pg_connection import EntityManager

entityManager = EntityManager()

def create(name, address):
    createParams = (name, address)
    createQuery = "INSERT INTO store(name, address) VALUES(%s,%s) returning store_id"
    return entityManager.executeQuery(createQuery, createParams)

def list(name, address, pageSize, pageIndex, orderBy):
    rs = entityManager.executeQuery("""
        select * from store 
        where 
            (%(name)s is null or name like %(name)s||'%%')
            and 
            (%(address)s is null or address like %(address)s||'%%')
        limit(%(pageSize)s + 1) offset (%(pageIndex)s * %(pageSize)s)
    """,{'name':name, 'address':address, 'pageSize':pageSize, 'pageIndex':pageIndex})
    content = []
    print(rs)
    for item in rs:
        content[i] = rs.resolve()
    lastPage = true
    if content.size > pageSize:
        lastPage = false
        content.removeLastElement()
    return PageList(content, pageSize, pageIndex. lastPage)
