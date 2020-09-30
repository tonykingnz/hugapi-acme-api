import psycopg2
from PageList import PageList
from pg_connection import EntityManager

entityManager = EntityManager()

def create(storeId, name, unit, image, category, lastPrice):
    createParams = (storeId, name, unit, image, category, lastPrice)
    createQuery = "INSERT INTO store_item(store_id, name, unit, image, category, last_price) VALUES(%s,%s,%s,%s,%s,%s) returning store_item_id"
    return entityManager.executeQuery(createQuery, createParams)

def list(storeId, categoryTerm, unitTerm, nameTerm, pageSize, pageIndex):
    rs = entityManager.executeQuery("""
        select * from store_item 
        where
            (category like %(categoryTerm)s||'%%')
            and
            (%(nameTerm)s is null or name like %(nameTerm)s||'%%')
            and 
            (%(unitTerm)s is null or unit like %(unitTerm)s||'%%')
            and
            (store_id::text like %(storeId)s||'%%')

        /*
        ORDER BY 
            CASE WHEN %(orderBy)s='storeId asc' THEN store_id END ASC,
            CASE WHEN %(orderBy)s='storeId desc' THEN store_id END DESC,
            CASE WHEN %(orderBy)s='name asc' THEN name END ASC,
            CASE WHEN %(orderBy)s='name desc' THEN name END DESC,
            CASE WHEN %(orderBy)s='address asc' THEN address END ASC,
            CASE WHEN %(orderBy)s='address desc' THEN address END DESC
        */

        limit(%(pageSize)s + 1) offset (%(pageIndex)s * %(pageSize)s)
    """
    ,{'storeId':storeId, 'nameTerm':nameTerm, 'unitTerm':unitTerm, 'categoryTerm':categoryTerm, 'pageSize':pageSize, 'pageIndex':pageIndex}, fetchall=True)
    content = []
    '''
    for item in rs:
        content.append({'storeId':item[0], 'store': item[1], 'address': item[2]})
    lastPage = True
    if len(content) > pageSize:
        lastPage = False
        content.removeLastElement()
    dictionaryPagination = {'content':content, 'pageSize': pageSize, 'pageIndex': pageIndex+1, 'lastPage': lastPage}
    return dictionaryPagination
    '''
    return rs

def update(nameStore, addressStore, storeId):
    updateParams = (nameStore, addressStore, storeId)
    updateQuery = """
        UPDATE store 
            SET name = %s, address = %s 
        WHERE store_id = %s
        RETURNING store_id;
        """
    return entityManager.executeQuery(updateQuery, updateParams)

