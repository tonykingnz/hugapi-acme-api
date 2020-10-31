import psycopg2
from PageList import PageList
from pg_connection import EntityManager

entityManager = EntityManager()

def orderItem(storeId, storeOrderId, customerId, confirmationDate, status, item):
    createParams = (storeId, storeOrderId, customerId, confirmationDate, status, item)
    createQuery = "INSERT INTO orders(store_id, store_order_id, customer_id, confirmation_date, status_order, item) VALUES(%s,%s,%s,%s,%s,%s) returning store_order_id"
    return entityManager.executeQuery(createQuery, createParams)


