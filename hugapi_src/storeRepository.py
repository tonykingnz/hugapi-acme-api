import psycopg2
from PageList import PageList
from pg_connection import EntityManager

entityManager = EntityManager()

def create(name, address):
    createParams = (name, address)
    createQuery = "INSERT INTO store(name, address) VALUES(%s,%s) returning store_id"
    return entityManager.executeQuery(createQuery, createParams)

def list(storeId, name, address, pageSize, pageIndex, orderBy):
    rs = entityManager.executeQuery("""
        select * from store 
        where
            (%(name)s is null or name like %(name)s||'%%')
            and 
            (%(address)s is null or address like %(address)s||'%%')
            and
            (%(storeId)s is null or store_id::text like %(storeId)s||'%%')
        
        ORDER BY 
            CASE WHEN %(orderBy)s='storeId asc' THEN store_id END ASC,
            CASE WHEN %(orderBy)s='storeId desc' THEN store_id END DESC,
            CASE WHEN %(orderBy)s='name asc' THEN name END ASC,
            CASE WHEN %(orderBy)s='name desc' THEN name END DESC,
            CASE WHEN %(orderBy)s='address asc' THEN address END ASC,
            CASE WHEN %(orderBy)s='address desc' THEN address END DESC

        limit(%(pageSize)s + 1) offset (%(pageIndex)s * %(pageSize)s)
    """
    ,{'storeId':storeId, 'name':name, 'address':address, 'pageSize':pageSize, 'pageIndex':pageIndex, 'orderBy':orderBy}, fetchall=True)
    content = []
    for item in rs:
        content.append({'storeId':item[0], 'name': item[1], 'address': item[2]})
    lastPage = True
    if len(content) > pageSize:
        lastPage = False
        content.removeLastElement()
    dictionaryPagination = {'content':content, 'pageSize': pageSize, 'pageIndex': pageIndex+1, 'lastPage': lastPage}
    return dictionaryPagination

def update(nameStore, addressStore, storeId):
    updateParams = (nameStore, addressStore, storeId)
    updateQuery = """
        UPDATE store 
            SET name = %s, address = %s 
        WHERE store_id = %s
        RETURNING store_id;
        """
    return entityManager.executeQuery(updateQuery, updateParams)

